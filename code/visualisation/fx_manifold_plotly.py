#!/usr/bin/env python3
"""
Interactive 3D FX Market Manifold Visualisation
================================================
Uses Plotly for full browser-based interactivity:
- Rotate, zoom, pan with mouse
- Hover to see timestamp, currency weights, curvature
- Toggle layers (manifold path, minimal surface, per-pair highlights)
- Multiple colour schemes (time, curvature, velocity, deviation)

Opens in your default browser. No server needed.

Copyright Saxon Nicholls 2026 MIT Licence

Usage:
    pip install plotly
    python fx_manifold_plotly.py
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.interpolate import griddata

ROOT = Path(__file__).parent.parent.parent
DATA_DIR = ROOT / "data" / "processed"
GAL_DIR = ROOT / "code" / "visualisation" / "gallery"

try:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
except ImportError:
    print("ERROR: plotly not installed. Run: pip install plotly")
    sys.exit(1)


FX_COLORS = {
    "EURUSD": "#1f77b4", "GBPUSD": "#d62728", "JPYUSD": "#ff7f0e",
    "CHFUSD": "#2ca02c", "AUDUSD": "#9467bd", "CADUSD": "#8c564b",
    "NZDUSD": "#e377c2",
}


def load_and_compute():
    """Load FX data and compute manifold, surface, curvature."""
    returns = pd.read_parquet(DATA_DIR / "fx_futures_1min_returns.parquet").dropna()
    T, d = returns.shape
    pairs = returns.columns.tolist()
    timestamps = returns.index

    # Portfolio weights on the simplex
    gross = (1 + returns).cumprod()
    weights = gross.div(gross.sum(axis=1), axis=0).values

    # Bhattacharyya embedding
    embedded = np.sqrt(np.maximum(weights, 1e-10))
    norms = np.linalg.norm(embedded, axis=1, keepdims=True)
    embedded = embedded / np.maximum(norms, 1e-10)

    # PCA → 3D manifold
    mean = embedded.mean(axis=0)
    centered = embedded - mean
    cov = np.cov(centered.T)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    V_r = eigenvectors[:, :3]
    projected = centered @ V_r
    var_exp = eigenvalues[:3] / eigenvalues.sum() * 100

    # Curvature (Frenet)
    dp = np.diff(projected, axis=0)
    ddp = np.diff(dp, axis=0)
    dp = np.vstack([dp, dp[-1:]])
    ddp = np.vstack([ddp, ddp[-1:], ddp[-1:]])
    speed = np.linalg.norm(dp, axis=1)
    cross = np.cross(dp, ddp)
    cross_norm = np.linalg.norm(cross, axis=1)
    curvature = cross_norm / np.maximum(speed ** 3, 1e-15)
    kernel = np.ones(20) / 20
    curvature = np.convolve(curvature, kernel, mode="same")

    # Minimal surface (interpolated)
    sub = np.arange(0, T, 10)
    x_sub, y_sub, z_sub = projected[sub, 0], projected[sub, 1], projected[sub, 2]
    xi = np.linspace(x_sub.min(), x_sub.max(), 60)
    yi = np.linspace(y_sub.min(), y_sub.max(), 60)
    xi_grid, yi_grid = np.meshgrid(xi, yi)
    zi_grid = griddata((x_sub, y_sub), z_sub, (xi_grid, yi_grid), method="cubic")

    # Deviation from surface
    z_surface = griddata((x_sub, y_sub), z_sub,
                          (projected[:, 0], projected[:, 1]), method="linear")
    deviation = projected[:, 2] - np.nan_to_num(z_surface, 0)

    return {
        "projected": projected, "weights": weights, "returns": returns,
        "pairs": pairs, "timestamps": timestamps, "var_exp": var_exp,
        "curvature": curvature, "deviation": deviation, "speed": speed,
        "xi_grid": xi_grid, "yi_grid": yi_grid, "zi_grid": zi_grid,
        "T": T,
    }


def build_interactive_figure(data):
    """Build the full interactive Plotly figure."""

    proj = data["projected"]
    curv = data["curvature"]
    dev = data["deviation"]
    speed = data["speed"]
    weights = data["weights"]
    pairs = data["pairs"]
    timestamps = data["timestamps"]
    var_exp = data["var_exp"]
    T = data["T"]

    # Subsample for performance (plotly struggles with >50k points)
    step = max(1, T // 20000)
    idx = np.arange(0, T, step)

    x, y, z = proj[idx, 0], proj[idx, 1], proj[idx, 2]
    c_time = np.linspace(0, 1, len(idx))
    c_curv = curv[idx]
    c_dev = dev[idx]
    c_speed = speed[idx]

    # Build hover text
    hover = []
    for i in idx:
        ts = str(timestamps[i])[:19] if i < len(timestamps) else ""
        w_str = " | ".join([f"{p[:3]}:{weights[i, j]:.3f}"
                             for j, p in enumerate(pairs)])
        hover.append(f"Time: {ts}<br>κ: {curv[i]:.4f}<br>"
                      f"Dev: {dev[i]:.6f}<br>Weights: {w_str}")

    fig = go.Figure()

    # ── Layer 1: Manifold path coloured by curvature ─────────
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode="markers",
        marker=dict(
            size=1.5,
            color=c_curv,
            colorscale="Hot",
            cmin=0,
            cmax=np.percentile(c_curv, 95),
            colorbar=dict(title="Curvature |κ|", x=1.0),
            opacity=0.6,
        ),
        text=hover,
        hoverinfo="text",
        name="Manifold (curvature)",
        visible=True,
    ))

    # ── Layer 2: Manifold path coloured by time ──────────────
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode="markers",
        marker=dict(
            size=1.5,
            color=c_time,
            colorscale="Viridis",
            colorbar=dict(title="Time", x=1.0),
            opacity=0.6,
        ),
        text=hover,
        hoverinfo="text",
        name="Manifold (time)",
        visible=False,
    ))

    # ── Layer 3: Manifold coloured by deviation from surface ──
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode="markers",
        marker=dict(
            size=1.5,
            color=c_dev,
            colorscale="RdBu_r",
            cmid=0,
            colorbar=dict(title="Deviation H", x=1.0),
            opacity=0.6,
        ),
        text=hover,
        hoverinfo="text",
        name="Manifold (deviation)",
        visible=False,
    ))

    # ── Layer 4: Manifold coloured by velocity ───────────────
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode="markers",
        marker=dict(
            size=1.5,
            color=c_speed,
            colorscale="YlOrRd",
            cmin=0,
            cmax=np.percentile(c_speed, 95),
            colorbar=dict(title="Speed", x=1.0),
            opacity=0.6,
        ),
        text=hover,
        hoverinfo="text",
        name="Manifold (velocity)",
        visible=False,
    ))

    # ── Layer 5: Minimal surface ─────────────────────────────
    xi_grid = data["xi_grid"]
    yi_grid = data["yi_grid"]
    zi_grid = data["zi_grid"]

    fig.add_trace(go.Surface(
        x=xi_grid, y=yi_grid, z=zi_grid,
        colorscale=[[0, "rgba(100,149,237,0.2)"], [1, "rgba(100,149,237,0.2)"]],
        showscale=False,
        opacity=0.25,
        name="Minimal surface",
        visible=True,
        hoverinfo="skip",
    ))

    # ── Layer 6-12: Per-pair highlights ──────────────────────
    returns_arr = data["returns"].values
    for j, pair in enumerate(pairs):
        pair_ret = returns_arr[idx, j]
        # Colour by this pair's return
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode="markers",
            marker=dict(
                size=1.5,
                color=pair_ret,
                colorscale="RdBu_r",
                cmid=0,
                cmax=np.percentile(np.abs(pair_ret), 95),
                cmin=-np.percentile(np.abs(pair_ret), 95),
                colorbar=dict(title=f"{pair} return", x=1.0),
                opacity=0.6,
            ),
            name=f"{pair}",
            visible=False,
            hoverinfo="text",
            text=[f"{pair}: {pair_ret[k]:+.4f}" for k in range(len(idx))],
        ))

    # ── Dropdown menu for colour scheme ──────────────────────
    n_pairs = len(pairs)
    # Traces: 0=curvature, 1=time, 2=deviation, 3=velocity, 4=surface, 5..11=pairs
    n_traces = 5 + n_pairs

    def make_visible(active_idx, show_surface=True):
        vis = [False] * n_traces
        vis[active_idx] = True
        vis[4] = show_surface  # surface always optional
        return vis

    buttons = [
        dict(label="Curvature (|κ|)", method="update",
             args=[{"visible": make_visible(0)}]),
        dict(label="Time", method="update",
             args=[{"visible": make_visible(1)}]),
        dict(label="Deviation from surface (H)", method="update",
             args=[{"visible": make_visible(2)}]),
        dict(label="Velocity", method="update",
             args=[{"visible": make_visible(3)}]),
    ]
    for j, pair in enumerate(pairs):
        buttons.append(
            dict(label=pair, method="update",
                 args=[{"visible": make_visible(5 + j)}])
        )
    # Toggle surface
    buttons.append(
        dict(label="Toggle Surface", method="restyle",
             args=[{"visible": [not fig.data[4].visible]}, [4]])
    )

    fig.update_layout(
        updatemenus=[dict(
            type="dropdown",
            direction="down",
            x=0.0, y=1.15,
            showactive=True,
            buttons=buttons,
        )],
        scene=dict(
            xaxis_title=f"PC1 ({var_exp[0]:.1f}%)",
            yaxis_title=f"PC2 ({var_exp[1]:.1f}%)",
            zaxis_title=f"PC3 ({var_exp[2]:.1f}%)",
            aspectmode="data",
        ),
        title=dict(
            text=(f"FX Market Manifold — Interactive<br>"
                  f"<sub>7 currencies, 1-min, Dec 2024 | "
                  f"PC1={var_exp[0]:.0f}% PC2={var_exp[1]:.0f}% PC3={var_exp[2]:.0f}% | "
                  f"Drag to rotate, scroll to zoom, dropdown to change colour</sub>"),
            x=0.5,
        ),
        width=1200,
        height=800,
        margin=dict(l=0, r=0, t=80, b=0),
    )

    return fig


def main():
    print("=" * 60)
    print("  Interactive FX Market Manifold (Plotly)")
    print("=" * 60)

    data = load_and_compute()
    print(f"\n  {data['T']} bars × {len(data['pairs'])} pairs")
    print(f"  PC1={data['var_exp'][0]:.1f}%, PC2={data['var_exp'][1]:.1f}%, "
          f"PC3={data['var_exp'][2]:.1f}%")

    print("\n  Building interactive figure...")
    fig = build_interactive_figure(data)

    # Save as interactive HTML
    html_path = GAL_DIR / "fx_manifold_interactive.html"
    fig.write_html(str(html_path), include_plotlyjs=True)
    print(f"  Saved: {html_path}")
    print(f"  Open in browser to interact!")

    # Also save a static high-res image
    try:
        fig.write_image(str(GAL_DIR / "fx_manifold_plotly_static.png"),
                         width=1600, height=1000, scale=2)
        print(f"  Static PNG: {GAL_DIR / 'fx_manifold_plotly_static.png'}")
    except Exception:
        print("  (Static PNG export requires kaleido: pip install kaleido)")

    # Open in browser
    print("\n  Opening in browser...")
    fig.show()


if __name__ == "__main__":
    main()
