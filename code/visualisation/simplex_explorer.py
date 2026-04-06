#!/usr/bin/env python3
"""
Interactive N-Dimensional Simplex Explorer
============================================
Visualises the d-dimensional portfolio simplex projected to 3D,
with overlays for curvature, MUP weights, lightcones, and more.

Features:
- Dimension selector (d = 3 to 25)
- Bhattacharyya embedding (√b maps simplex to sphere)
- Stereoscopic 3D (side-by-side for VR/cross-eye viewing)
- Quantity overlays: curvature, weights, Willmore, lightcone
- MUP posterior visualisation
- Reusable: call make_simplex_figure() from any script

Usage:
    python simplex_explorer.py [--dim 5] [--stereo]

Copyright Saxon Nicholls 2026 MIT Licence
"""

import sys
import argparse
from pathlib import Path
import numpy as np

import plotly.graph_objects as go
from plotly.subplots import make_subplots

GAL_DIR = Path(__file__).parent / "gallery"
GAL_DIR.mkdir(exist_ok=True)


# ── Core simplex geometry ────────────────────────────────────

def simplex_vertices(d):
    """Generate the d vertices of Δ_{d-1} as standard basis vectors in R^d."""
    return np.eye(d)


def bhattacharyya_embed(points):
    """Map points on the simplex to the Bhattacharyya sphere: b → √b."""
    embedded = np.sqrt(np.maximum(points, 1e-12))
    norms = np.linalg.norm(embedded, axis=1, keepdims=True)
    return embedded / np.maximum(norms, 1e-12)


def project_to_3d(points_high_d):
    """Project high-dimensional points to 3D via PCA."""
    mean = points_high_d.mean(axis=0)
    centered = points_high_d - mean
    if centered.shape[0] < 3:
        # Pad with zeros
        padded = np.zeros((max(3, centered.shape[0]), centered.shape[1]))
        padded[:centered.shape[0]] = centered
        centered = padded
    U, S, Vt = np.linalg.svd(centered, full_matrices=False)
    return centered @ Vt[:3].T


def sample_simplex_uniform(d, n=5000, seed=42):
    """Sample n points uniformly from Δ_{d-1} via Dirichlet(1,...,1)."""
    rng = np.random.default_rng(seed)
    return rng.dirichlet(np.ones(d), n)


def sample_simplex_edges(d, n_per_edge=50):
    """Sample points along all edges of the simplex."""
    verts = simplex_vertices(d)
    points = []
    for i in range(d):
        for j in range(i + 1, d):
            for t in np.linspace(0, 1, n_per_edge):
                points.append((1 - t) * verts[i] + t * verts[j])
    return np.array(points)


def sample_simplex_faces(d, n_per_face=200, seed=42):
    """Sample points on all 2-faces (triangles) of the simplex."""
    rng = np.random.default_rng(seed)
    verts = simplex_vertices(d)
    points = []
    for i in range(d):
        for j in range(i + 1, d):
            for k in range(j + 1, d):
                # Random points on the triangle (i, j, k)
                u = rng.random((n_per_face, 2))
                u.sort(axis=1)
                s, t = u[:, 0], u[:, 1] - u[:, 0]
                r = 1 - u[:, 1]
                for idx in range(n_per_face):
                    points.append(s[idx] * verts[i] + t[idx] * verts[j] + r[idx] * verts[k])
    return np.array(points)


# ── Quantity computation ─────────────────────────────────────

def fisher_rao_curvature(points):
    """Compute the Fisher-Rao curvature at each point. K = 1/4 everywhere on the sphere,
    but the EXTRINSIC curvature (how the manifold bends in the ambient space) varies."""
    # For points on the Bhattacharyya sphere, the sectional curvature is constant 1/4.
    # The quantity that varies is the WEIGHT of each point — how concentrated the portfolio is.
    # Use the concentration (max weight) as a proxy for curvature-relevant behaviour.
    return np.max(points, axis=1)


def fisher_rao_distance_from_center(points):
    """Fisher-Rao distance from each point to the centroid (equal weight)."""
    d = points.shape[1]
    center = np.ones(d) / d
    # Bhattacharyya distance
    bc = np.sum(np.sqrt(points * center), axis=1)
    bc = np.clip(bc, -1, 1)
    return 2 * np.arccos(bc)


def mup_weights(points, returns=None, T=252):
    """Compute MUP posterior weights (wealth-weighted) for visualisation.
    If no returns provided, use synthetic Kelly weights."""
    n, d = points.shape
    if returns is None:
        # Synthetic: points near the centroid get higher weight
        dist = fisher_rao_distance_from_center(points)
        log_w = -T * dist ** 2  # Gaussian posterior centred at centroid
    else:
        # Real: compute log-wealth for each portfolio
        gross = 1.0 + returns
        log_w = np.array([np.sum(np.log(np.maximum(gross @ b, 1e-15))) for b in points])

    log_w -= log_w.max()
    w = np.exp(log_w)
    w /= w.sum()
    return w


def lightcone_points(center_3d, c_M=0.3, n_steps=20, n_angles=50):
    """Generate the lightcone surface from a point in 3D."""
    # Future cone: expanding sphere at speed c_M
    cone_points = []
    for t in np.linspace(0.01, 0.5, n_steps):
        radius = c_M * t
        for theta in np.linspace(0, 2 * np.pi, n_angles):
            for phi in np.linspace(0, np.pi, n_angles // 2):
                x = center_3d[0] + radius * np.sin(phi) * np.cos(theta)
                y = center_3d[1] + radius * np.sin(phi) * np.sin(theta)
                z = center_3d[2] + radius * np.cos(phi)
                cone_points.append([x, y, z, t])
    return np.array(cone_points)


# ── The main visualisation builder ───────────────────────────

def make_simplex_figure(d=5, stereo=False, overlay="curvature",
                         market_data=None, title_suffix=""):
    """
    Build the interactive simplex figure.

    Args:
        d: dimension of the simplex (number of assets)
        stereo: if True, create side-by-side stereoscopic view
        overlay: "curvature", "distance", "mup", "lightcone", "weights"
        market_data: optional (T, d) return matrix for real MUP
        title_suffix: extra text for the title

    Returns:
        plotly Figure
    """

    # ── Generate simplex points ──────────────────────────────
    # Vertices
    verts = simplex_vertices(d)
    verts_emb = bhattacharyya_embed(verts)

    # Edges
    edges = sample_simplex_edges(d, n_per_edge=30)
    edges_emb = bhattacharyya_embed(edges)

    # Interior samples
    interior = sample_simplex_uniform(d, n=8000)
    interior_emb = bhattacharyya_embed(interior)

    # Project everything to 3D
    all_points = np.vstack([verts_emb, edges_emb, interior_emb])
    all_3d = project_to_3d(all_points)

    n_verts = len(verts)
    n_edges = len(edges)
    verts_3d = all_3d[:n_verts]
    edges_3d = all_3d[n_verts:n_verts + n_edges]
    interior_3d = all_3d[n_verts + n_edges:]

    # ── Compute overlay quantity ─────────────────────────────
    if overlay == "curvature":
        colors = fisher_rao_curvature(interior)
        colorscale = "Hot"
        colorbar_title = "Max weight<br>(curvature proxy)"
    elif overlay == "distance":
        colors = fisher_rao_distance_from_center(interior)
        colorscale = "Viridis"
        colorbar_title = "d_FR from<br>centroid"
    elif overlay == "mup":
        weights = mup_weights(interior, returns=market_data)
        colors = np.log(weights + 1e-15)
        colorscale = "YlOrRd"
        colorbar_title = "log(MUP<br>weight)"
    elif overlay == "weights":
        # Color by the weight of the first asset
        colors = interior[:, 0]
        colorscale = "RdBu_r"
        colorbar_title = f"Weight of<br>asset 1"
    else:
        colors = fisher_rao_distance_from_center(interior)
        colorscale = "Viridis"
        colorbar_title = "d_FR"

    # ── Build figure ─────────────────────────────────────────

    def build_scene(eye_offset=0):
        """Build one 3D scene (used twice for stereo)."""
        traces = []

        # Interior points
        traces.append(go.Scatter3d(
            x=interior_3d[:, 0], y=interior_3d[:, 1], z=interior_3d[:, 2],
            mode="markers",
            marker=dict(size=1.5, color=colors, colorscale=colorscale,
                        opacity=0.4, colorbar=dict(title=colorbar_title) if eye_offset == 0 else None),
            name="Simplex interior",
            hovertemplate="(%{x:.3f}, %{y:.3f}, %{z:.3f})<extra></extra>",
        ))

        # Edges (wireframe)
        traces.append(go.Scatter3d(
            x=edges_3d[:, 0], y=edges_3d[:, 1], z=edges_3d[:, 2],
            mode="markers",
            marker=dict(size=1, color="gray", opacity=0.3),
            name="Edges",
        ))

        # Vertices (labeled)
        labels = [f"e{i+1}" for i in range(d)]
        traces.append(go.Scatter3d(
            x=verts_3d[:, 0], y=verts_3d[:, 1], z=verts_3d[:, 2],
            mode="markers+text",
            marker=dict(size=8, color="red", symbol="diamond"),
            text=labels,
            textposition="top center",
            textfont=dict(size=10),
            name="Vertices",
        ))

        # Centroid
        centroid = np.ones(d) / d
        centroid_emb = bhattacharyya_embed(centroid.reshape(1, -1))
        centroid_3d = project_to_3d(np.vstack([all_points, centroid_emb]))[-1]
        traces.append(go.Scatter3d(
            x=[centroid_3d[0]], y=[centroid_3d[1]], z=[centroid_3d[2]],
            mode="markers+text",
            marker=dict(size=10, color="green", symbol="cross"),
            text=["1/d"],
            textposition="bottom center",
            name="Centroid (equal weight)",
        ))

        # Lightcone overlay
        if overlay == "lightcone":
            cone = lightcone_points(centroid_3d, c_M=0.15)
            traces.append(go.Scatter3d(
                x=cone[:, 0], y=cone[:, 1], z=cone[:, 2],
                mode="markers",
                marker=dict(size=1, color=cone[:, 3], colorscale="Reds",
                            opacity=0.15),
                name="Future lightcone",
            ))

        return traces

    if stereo:
        fig = make_subplots(
            rows=1, cols=2,
            specs=[[{"type": "scatter3d"}, {"type": "scatter3d"}]],
            subplot_titles=["Left Eye", "Right Eye"],
            horizontal_spacing=0.02,
        )
        for trace in build_scene(eye_offset=-0.03):
            fig.add_trace(trace, row=1, col=1)
        for trace in build_scene(eye_offset=+0.03):
            fig.add_trace(trace, row=1, col=2)

        # Offset the camera for stereo effect
        ipd = 0.06  # interpupillary distance
        fig.update_layout(
            scene=dict(
                camera=dict(eye=dict(x=1.5 - ipd, y=1.5, z=0.8)),
                aspectmode="data",
            ),
            scene2=dict(
                camera=dict(eye=dict(x=1.5 + ipd, y=1.5, z=0.8)),
                aspectmode="data",
            ),
        )
    else:
        fig = go.Figure(data=build_scene())

    # ── Dropdown for overlays ────────────────────────────────
    overlay_buttons = [
        dict(label="Curvature", method="update",
             args=[{"marker.color": [fisher_rao_curvature(interior)],
                     "marker.colorscale": ["Hot"]}]),
        dict(label="Distance from center", method="update",
             args=[{"marker.color": [fisher_rao_distance_from_center(interior)],
                     "marker.colorscale": ["Viridis"]}]),
        dict(label="MUP weight", method="update",
             args=[{"marker.color": [np.log(mup_weights(interior) + 1e-15)],
                     "marker.colorscale": ["YlOrRd"]}]),
        dict(label="Asset 1 weight", method="update",
             args=[{"marker.color": [interior[:, 0]],
                     "marker.colorscale": ["RdBu_r"]}]),
    ]

    # ── Layout ───────────────────────────────────────────────
    fig.update_layout(
        title=dict(
            text=(f"Δ<sub>{d-1}</sub> Simplex Explorer ({d} assets) "
                  f"— Bhattacharyya Embedding to S<sup>{d-1}</sup><sub>+</sub>"
                  f"{title_suffix}<br>"
                  f"<sub>Drag to rotate · Scroll to zoom · "
                  f"{'Stereo: cross your eyes for 3D' if stereo else 'Dropdown to change overlay'}</sub>"),
            x=0.5,
        ),
        updatemenus=[dict(
            type="dropdown", x=0.0, y=1.12,
            buttons=overlay_buttons, showactive=True,
        )] if not stereo else [],
        width=1400 if stereo else 900,
        height=700,
        scene=dict(
            xaxis_title="PC1",
            yaxis_title="PC2",
            zaxis_title="PC3",
            aspectmode="data",
        ),
    )

    return fig


# ── Dimension sweep: generate figures for d = 3, 4, 5, 10, 25 ──

def generate_gallery():
    """Generate the complete gallery of simplex visualisations."""

    print("Generating simplex explorer gallery...")

    # Standard view for multiple dimensions
    for d in [3, 4, 5, 10, 25]:
        print(f"  d = {d}...", end="", flush=True)
        fig = make_simplex_figure(d=d, overlay="distance",
                                   title_suffix=f" | d={d}")
        fig.write_html(str(GAL_DIR / f"simplex_d{d}.html"), include_plotlyjs=True)
        print(f" saved")

    # Stereoscopic view for d = 5
    print("  Stereo d=5...", end="", flush=True)
    fig_stereo = make_simplex_figure(d=5, stereo=True, overlay="curvature",
                                      title_suffix=" | STEREOSCOPIC")
    fig_stereo.write_html(str(GAL_DIR / "simplex_d5_stereo.html"), include_plotlyjs=True)
    print(" saved")

    # MUP overlay
    print("  MUP overlay d=5...", end="", flush=True)
    fig_mup = make_simplex_figure(d=5, overlay="mup",
                                    title_suffix=" | MUP Posterior")
    fig_mup.write_html(str(GAL_DIR / "simplex_d5_mup.html"), include_plotlyjs=True)
    print(" saved")

    # Lightcone overlay
    print("  Lightcone d=5...", end="", flush=True)
    fig_lc = make_simplex_figure(d=5, overlay="lightcone",
                                   title_suffix=" | Lightcone from centroid")
    fig_lc.write_html(str(GAL_DIR / "simplex_d5_lightcone.html"), include_plotlyjs=True)
    print(" saved")

    print(f"\nGallery: {GAL_DIR}/")
    print("Files:")
    for f in sorted(GAL_DIR.glob("simplex_*.html")):
        print(f"  {f.name} ({f.stat().st_size / 1024 / 1024:.1f} MB)")


def main():
    parser = argparse.ArgumentParser(description="Interactive Simplex Explorer")
    parser.add_argument("--dim", type=int, default=5, help="Simplex dimension")
    parser.add_argument("--stereo", action="store_true", help="Stereoscopic 3D")
    parser.add_argument("--overlay", default="distance",
                        choices=["curvature", "distance", "mup", "lightcone", "weights"])
    parser.add_argument("--gallery", action="store_true", help="Generate full gallery")
    args = parser.parse_args()

    if args.gallery:
        generate_gallery()
    else:
        fig = make_simplex_figure(d=args.dim, stereo=args.stereo, overlay=args.overlay)
        out = GAL_DIR / f"simplex_d{args.dim}{'_stereo' if args.stereo else ''}.html"
        fig.write_html(str(out), include_plotlyjs=True)
        print(f"Saved: {out}")
        fig.show()


if __name__ == "__main__":
    main()
