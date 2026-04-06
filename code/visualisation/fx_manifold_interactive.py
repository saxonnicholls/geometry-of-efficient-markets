#!/usr/bin/env python3
"""
Interactive 3D Visualisation of the FX Market Manifold
=======================================================
Projects the 7-currency FX simplex onto its 3-dimensional market
manifold via PCA, then renders as interactive 3D scatter + paths.

Also generates static gallery images from multiple angles.

Copyright Saxon Nicholls 2026 MIT Licence

Usage:
    python fx_manifold_interactive.py [--interactive]
    # Without --interactive: generates static PNGs for the gallery
    # With --interactive: opens a matplotlib 3D rotation window
"""

import sys
import argparse
from pathlib import Path
import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import Normalize
import matplotlib.cm as cm

ROOT = Path(__file__).parent.parent.parent
DATA_DIR = ROOT / "data" / "processed"
GAL_DIR = ROOT / "code" / "visualisation" / "gallery"
GAL_DIR.mkdir(parents=True, exist_ok=True)

# Colour map for each FX pair
FX_COLORS = {
    "EURUSD": "#1f77b4",  # blue
    "GBPUSD": "#d62728",  # red
    "JPYUSD": "#ff7f0e",  # orange
    "CHFUSD": "#2ca02c",  # green
    "AUDUSD": "#9467bd",  # purple
    "CADUSD": "#8c564b",  # brown
    "NZDUSD": "#e377c2",  # pink
}


def load_fx_data():
    """Load and prepare FX data."""
    path = DATA_DIR / "fx_futures_1min_returns.parquet"
    if not path.exists():
        print(f"ERROR: {path} not found. Run download_databento_batch1.py first.")
        sys.exit(1)

    returns = pd.read_parquet(path)
    returns = returns.dropna()
    return returns


def compute_manifold(returns, r=3):
    """
    Project the FX simplex onto the r-dimensional market manifold via PCA.

    Steps:
    1. Compute portfolio weights (normalise cumulative returns to simplex)
    2. Apply Bhattacharyya embedding: w → √w
    3. PCA on the embedded points to get the r-dimensional manifold
    """
    T, d = returns.shape

    # Cumulative gross returns → portfolio weight evolution
    gross = (1 + returns).cumprod()
    # Normalise each row to sum to 1 → point on the simplex
    weights = gross.div(gross.sum(axis=1), axis=0).values

    # Bhattacharyya embedding: w → √w (maps simplex to sphere)
    embedded = np.sqrt(np.maximum(weights, 1e-10))
    # Normalise to unit sphere
    norms = np.linalg.norm(embedded, axis=1, keepdims=True)
    embedded = embedded / np.maximum(norms, 1e-10)

    # PCA to extract the r-dimensional manifold
    mean = embedded.mean(axis=0)
    centered = embedded - mean
    cov = np.cov(centered.T)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # Project onto top r PCs
    V_r = eigenvectors[:, :r]
    projected = centered @ V_r  # T × r

    # Variance explained
    var_explained = eigenvalues[:r] / eigenvalues.sum() * 100
    total_explained = var_explained.sum()

    return projected, weights, var_explained, total_explained, V_r, mean


def compute_velocity_colors(projected, window=10):
    """Compute the 'velocity' (speed of movement on the manifold) for colouring."""
    dp = np.diff(projected, axis=0)
    speed = np.linalg.norm(dp, axis=1)
    # Smooth
    kernel = np.ones(window) / window
    speed_smooth = np.convolve(speed, kernel, mode="same")
    # Pad to match length
    speed_full = np.concatenate([[speed_smooth[0]], speed_smooth])
    return speed_full


def compute_curvature_colors(projected, window=20):
    """
    Estimate local curvature from the path on the manifold.
    Curvature = |d²x/dt²| / |dx/dt|³ (Frenet formula for 3D curves).
    """
    if projected.shape[1] < 3:
        return np.zeros(len(projected))

    dp = np.diff(projected, axis=0)  # velocity
    ddp = np.diff(dp, axis=0)  # acceleration

    # Pad
    dp = np.vstack([dp, dp[-1:]])
    ddp = np.vstack([ddp, ddp[-1:], ddp[-1:]])

    speed = np.linalg.norm(dp, axis=1)
    accel = np.linalg.norm(ddp, axis=1)

    # Curvature κ = |a × v| / |v|³ (for 3D)
    cross = np.cross(dp, ddp)
    cross_norm = np.linalg.norm(cross, axis=1) if cross.ndim > 1 else np.abs(cross)
    curvature = cross_norm / np.maximum(speed ** 3, 1e-15)

    # Smooth
    kernel = np.ones(window) / window
    curvature_smooth = np.convolve(curvature, kernel, mode="same")
    return curvature_smooth


def generate_static_gallery(projected, weights, returns, var_explained,
                             total_explained):
    """Generate static PNG images from multiple angles."""

    T = len(projected)
    pairs = returns.columns.tolist()

    # Colour by time (early → late)
    time_colors = np.linspace(0, 1, T)

    # Colour by velocity
    velocity = compute_velocity_colors(projected)
    vel_norm = Normalize(vmin=np.percentile(velocity, 5),
                          vmax=np.percentile(velocity, 95))

    # Colour by curvature
    curvature = compute_curvature_colors(projected)
    curv_norm = Normalize(vmin=np.percentile(curvature, 5),
                           vmax=np.percentile(curvature, 95))

    # ── Figure 1: Four angles of the manifold, coloured by time ──
    fig = plt.figure(figsize=(20, 16))
    angles = [(30, 45), (30, 135), (60, 0), (10, 90)]
    titles = ["View 1: Front-right", "View 2: Front-left",
              "View 3: Top-down", "View 4: Side"]

    for i, (elev, azim) in enumerate(angles):
        ax = fig.add_subplot(2, 2, i + 1, projection="3d")
        scatter = ax.scatter(projected[:, 0], projected[:, 1], projected[:, 2],
                              c=time_colors, cmap="viridis", s=1, alpha=0.5)
        # Draw the path as a thin line
        ax.plot(projected[::5, 0], projected[::5, 1], projected[::5, 2],
                color="gray", linewidth=0.3, alpha=0.3)
        ax.view_init(elev=elev, azim=azim)
        ax.set_xlabel(f"PC1 ({var_explained[0]:.1f}%)")
        ax.set_ylabel(f"PC2 ({var_explained[1]:.1f}%)")
        ax.set_zlabel(f"PC3 ({var_explained[2]:.1f}%)")
        ax.set_title(titles[i])

    fig.suptitle(f"FX Market Manifold (7 currencies, 1-min, {total_explained:.1f}% variance)\n"
                 f"Coloured by time: blue (start) → yellow (end)",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(GAL_DIR / "fx_manifold_4angles.png", dpi=150)
    plt.close()
    print(f"  Saved: fx_manifold_4angles.png")

    # ── Figure 2: Coloured by velocity (speed on the manifold) ──
    fig = plt.figure(figsize=(16, 6))

    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    scatter = ax1.scatter(projected[:, 0], projected[:, 1], projected[:, 2],
                           c=velocity, cmap="hot", norm=vel_norm, s=1, alpha=0.5)
    ax1.view_init(elev=30, azim=45)
    ax1.set_xlabel("PC1"); ax1.set_ylabel("PC2"); ax1.set_zlabel("PC3")
    ax1.set_title("Velocity on the Manifold\n(bright = fast, dark = slow)")
    plt.colorbar(scatter, ax=ax1, shrink=0.6, label="Speed")

    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    scatter2 = ax2.scatter(projected[:, 0], projected[:, 1], projected[:, 2],
                            c=curvature, cmap="coolwarm", norm=curv_norm,
                            s=1, alpha=0.5)
    ax2.view_init(elev=30, azim=45)
    ax2.set_xlabel("PC1"); ax2.set_ylabel("PC2"); ax2.set_zlabel("PC3")
    ax2.set_title("Curvature on the Manifold\n(red = high curvature = alpha)")
    plt.colorbar(scatter2, ax=ax2, shrink=0.6, label="Curvature |κ|")

    fig.suptitle("FX Manifold: Velocity and Curvature", fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.savefig(GAL_DIR / "fx_manifold_velocity_curvature.png", dpi=150)
    plt.close()
    print(f"  Saved: fx_manifold_velocity_curvature.png")

    # ── Figure 3: Per-pair contribution to manifold movement ──
    fig = plt.figure(figsize=(20, 6))

    # Project each pair's returns onto the 3 PCs individually
    for idx, pair in enumerate(pairs):
        ax = fig.add_subplot(1, len(pairs), idx + 1, projection="3d")

        # Colour by this pair's return (positive = one colour, negative = another)
        pair_ret = returns[pair].values
        pair_colors = np.where(pair_ret > 0, 1.0, 0.0)

        ax.scatter(projected[:, 0], projected[:, 1], projected[:, 2],
                   c=pair_colors, cmap="RdBu_r", s=1, alpha=0.4)
        ax.view_init(elev=30, azim=45)
        ax.set_title(pair, fontsize=10, color=FX_COLORS.get(pair, "black"),
                     fontweight="bold")
        ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])

    fig.suptitle("FX Manifold: Each Pair's Contribution\n"
                 "(red = pair up, blue = pair down)",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.90])
    plt.savefig(GAL_DIR / "fx_manifold_per_pair.png", dpi=150)
    plt.close()
    print(f"  Saved: fx_manifold_per_pair.png")

    # ── Figure 4: Simplex weights trajectory (2D projection) ──
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Weight evolution over time
    for pair in pairs:
        idx_p = pairs.index(pair)
        axes[0].plot(weights[:, idx_p], label=pair, linewidth=0.5,
                      color=FX_COLORS.get(pair, None), alpha=0.8)
    axes[0].set_title("Currency Simplex Weights Over Time")
    axes[0].set_xlabel("Minute")
    axes[0].set_ylabel("Weight w_i")
    axes[0].legend(fontsize=7, ncol=2)

    # 2D scatter: PC1 vs PC2 coloured by time
    axes[1].scatter(projected[:, 0], projected[:, 1], c=time_colors,
                     cmap="viridis", s=1, alpha=0.3)
    axes[1].set_xlabel(f"PC1 ({var_explained[0]:.1f}%)")
    axes[1].set_ylabel(f"PC2 ({var_explained[1]:.1f}%)")
    axes[1].set_title("Manifold (PC1 vs PC2)")

    # Curvature time series
    axes[2].plot(curvature[:2000], linewidth=0.5, color="steelblue", alpha=0.7)
    axes[2].set_xlabel("Minute")
    axes[2].set_ylabel("|κ| (curvature)")
    axes[2].set_title("Manifold Curvature Over Time\n(spikes = alpha opportunities)")

    plt.tight_layout()
    plt.savefig(GAL_DIR / "fx_manifold_2d_analysis.png", dpi=150)
    plt.close()
    print(f"  Saved: fx_manifold_2d_analysis.png")

    # ── Figure 5: The Bhattacharyya sphere with the manifold ──
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection="3d")

    # Draw a translucent sphere (the Bhattacharyya sphere)
    u = np.linspace(0, np.pi / 2, 30)  # positive octant only
    v = np.linspace(0, np.pi / 2, 30)
    x = np.outer(np.sin(u), np.cos(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.cos(u), np.ones_like(v))
    ax.plot_surface(x * 0.3, y * 0.3, z * 0.3, alpha=0.05, color="gray")

    # The manifold path on the sphere
    # Scale projected to fit inside the sphere visualisation
    scale = 0.25 / np.max(np.abs(projected))
    ax.scatter(projected[:, 0] * scale, projected[:, 1] * scale,
               projected[:, 2] * scale,
               c=curvature, cmap="hot", s=2, alpha=0.5,
               norm=curv_norm)

    ax.view_init(elev=25, azim=40)
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.set_zlabel("PC3")
    ax.set_title("FX Market Manifold in the Bhattacharyya Sphere\n"
                 "Coloured by curvature (bright = high |H| = alpha)",
                 fontsize=12, fontweight="bold")

    plt.tight_layout()
    plt.savefig(GAL_DIR / "fx_manifold_bhattacharyya.png", dpi=200)
    plt.close()
    print(f"  Saved: fx_manifold_bhattacharyya.png")


def run_interactive(projected, var_explained, velocity, curvature):
    """Open an interactive matplotlib 3D window for rotation."""
    matplotlib.use("TkAgg")  # Switch to interactive backend
    import matplotlib.pyplot as plt

    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection="3d")

    scatter = ax.scatter(projected[:, 0], projected[:, 1], projected[:, 2],
                          c=curvature, cmap="hot", s=2, alpha=0.5)
    ax.set_xlabel(f"PC1 ({var_explained[0]:.1f}%)")
    ax.set_ylabel(f"PC2 ({var_explained[1]:.1f}%)")
    ax.set_zlabel(f"PC3 ({var_explained[2]:.1f}%)")
    ax.set_title("FX Market Manifold — Interactive\n"
                 "Drag to rotate, scroll to zoom")
    plt.colorbar(scatter, ax=ax, shrink=0.6, label="Curvature |κ|")
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="FX Market Manifold Visualisation")
    parser.add_argument("--interactive", action="store_true",
                        help="Open interactive 3D rotation window")
    args = parser.parse_args()

    print("=" * 60)
    print("  FX Market Manifold Visualisation")
    print("  7 currencies, 1-minute resolution, Dec 2024")
    print("=" * 60)

    returns = load_fx_data()
    print(f"\n  Data: {returns.shape[0]} bars × {returns.shape[1]} pairs")
    print(f"  Pairs: {returns.columns.tolist()}")

    # Compute the 3D manifold
    projected, weights, var_explained, total_explained, V_r, mean = \
        compute_manifold(returns, r=3)

    print(f"\n  PCA variance explained:")
    for i, v in enumerate(var_explained):
        print(f"    PC{i+1}: {v:.1f}%")
    print(f"    Total (3 PCs): {total_explained:.1f}%")

    # Velocity and curvature
    velocity = compute_velocity_colors(projected)
    curvature = compute_curvature_colors(projected)

    print(f"\n  Manifold statistics:")
    print(f"    Mean velocity: {np.mean(velocity):.6f}")
    print(f"    Mean curvature: {np.mean(curvature):.4f}")
    print(f"    Max curvature: {np.max(curvature):.4f}")
    print(f"    Curvature 95th pctl: {np.percentile(curvature, 95):.4f}")

    if args.interactive:
        print("\n  Opening interactive 3D window...")
        run_interactive(projected, var_explained, velocity, curvature)
    else:
        print("\n  Generating static gallery images...")
        generate_static_gallery(projected, weights, returns, var_explained,
                                 total_explained)

    print(f"\n  Gallery: {GAL_DIR}/")
    print("  Done.")


if __name__ == "__main__":
    main()
