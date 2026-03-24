# Copyright Saxon Nicholls 2026 MIT Licence
"""
Visualisation of the three classified market manifold types
in the Bhattacharyya sphere S^{d-1}_+.

For d=3 assets, the portfolio simplex Δ₂ maps via φ: b → √b
to the positive octant of S² (curvature K=1/4 in Bhattacharyya normalisation).

The three market types:
  1. CAPM great sphere S^r_+  — Jacobi diffusion, GOE (β=1)
  2. Clifford torus T²        — flat torus BM, GUE (β=2)
  3. Pseudo-Anosov (hyperbolic) — McKean kernel, GSE (β=4)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from mpl_toolkits.mplot3d.art3d import Line3DCollection

# ---------------------------------------------------------------------------
# Bhattacharyya embedding: b ∈ Δ_{d-1} → √b ∈ S^{d-1}_+
# ---------------------------------------------------------------------------

def bhattacharyya(b):
    """Map portfolio weights to Bhattacharyya sphere."""
    return np.sqrt(np.clip(b, 0, None))


def sphere_to_portfolio(u):
    """Inverse: u ∈ S^{d-1}_+ → b = u² ∈ Δ_{d-1}."""
    return u ** 2


# ---------------------------------------------------------------------------
# 1. The positive octant of S² (the ambient space for d=3)
# ---------------------------------------------------------------------------

def positive_octant_sphere(n=60):
    """Generate the positive octant of S² as a mesh."""
    theta = np.linspace(0, np.pi / 2, n)
    phi = np.linspace(0, np.pi / 2, n)
    theta, phi = np.meshgrid(theta, phi)
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return x, y, z


# ---------------------------------------------------------------------------
# 2. CAPM great hemisphere S^1_+ (a great circle arc in S²_+)
# ---------------------------------------------------------------------------

def capm_great_circle(b_star=None, n=200):
    """
    A great circle through the positive octant of S².
    For d=3, r=1: this is a 1D curve (geodesic) on S²_+.
    We parameterise a great circle passing through b* = (1/3, 1/3, 1/3).
    """
    if b_star is None:
        b_star = np.array([1/3, 1/3, 1/3])

    u_star = bhattacharyya(b_star)
    u_star /= np.linalg.norm(u_star)

    # Pick a tangent direction in the positive octant
    v = np.array([1, -1, 0]) / np.sqrt(2)
    # Gram-Schmidt to make v orthogonal to u_star
    v = v - np.dot(v, u_star) * u_star
    v /= np.linalg.norm(v)

    # Great circle: u(t) = cos(t) u* + sin(t) v
    t = np.linspace(-0.8, 0.8, n)
    curve = np.outer(np.cos(t), u_star) + np.outer(np.sin(t), v)

    # Keep only points in positive octant
    mask = np.all(curve > 0, axis=1)
    return curve[mask]


# ---------------------------------------------------------------------------
# 3. Clifford torus T² in S³ projected to S²_+
# For d=4, the Clifford torus lives in S³. For visualisation with d=3,
# we show a "torus-like" surface on S²_+ via a product parameterisation.
# ---------------------------------------------------------------------------

def clifford_torus_on_sphere(n=80):
    """
    The Clifford torus in S³: (cos θ₁/√2, sin θ₁/√2, cos θ₂/√2, sin θ₂/√2).
    We project to 3D by stereographic projection from the 4th coordinate,
    keeping only points with all coordinates positive.
    """
    theta1 = np.linspace(0.05, np.pi / 2 - 0.05, n)
    theta2 = np.linspace(0.05, np.pi / 2 - 0.05, n)
    t1, t2 = np.meshgrid(theta1, theta2)

    # Clifford torus in S³
    w = np.cos(t1) / np.sqrt(2)
    x = np.sin(t1) / np.sqrt(2)
    y = np.cos(t2) / np.sqrt(2)
    z = np.sin(t2) / np.sqrt(2)

    # Stereographic projection from (0,0,0,-1) to R³
    denom = 1 + z
    X = w / denom
    Y = x / denom
    Z = y / denom

    # Normalise to unit sphere for display
    norm = np.sqrt(X**2 + Y**2 + Z**2)
    X, Y, Z = X / norm, Y / norm, Z / norm

    # Keep positive octant
    mask = (X > 0.01) & (Y > 0.01) & (Z > 0.01)
    X[~mask] = np.nan
    Y[~mask] = np.nan
    Z[~mask] = np.nan

    return X, Y, Z


# ---------------------------------------------------------------------------
# 4. Hyperbolic (pseudo-Anosov) patch on S²_+
# A negatively-curved region — we model this as a saddle-shaped
# perturbation of the sphere near a point.
# ---------------------------------------------------------------------------

def hyperbolic_patch(b_star=None, n=60, amplitude=0.15):
    """
    A saddle-shaped (negatively curved) patch on S²_+,
    representing the pseudo-Anosov market manifold.
    """
    if b_star is None:
        b_star = np.array([0.5, 0.3, 0.2])

    u_star = bhattacharyya(b_star)
    u_star /= np.linalg.norm(u_star)

    # Local coordinates on the tangent plane
    e1 = np.array([1, -1, 0]) / np.sqrt(2)
    e1 = e1 - np.dot(e1, u_star) * u_star
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(u_star, e1)
    e2 /= np.linalg.norm(e2)

    s = np.linspace(-0.5, 0.5, n)
    t = np.linspace(-0.5, 0.5, n)
    S, T = np.meshgrid(s, t)

    # Saddle perturbation: h(s,t) = amplitude * (s² - t²)
    H = amplitude * (S**2 - T**2)

    # Points on perturbed sphere
    pts = (np.outer(np.ones(n*n), u_star).reshape(n, n, 3)
           + S[:, :, None] * e1[None, None, :]
           + T[:, :, None] * e2[None, None, :]
           + H[:, :, None] * u_star[None, None, :])

    # Project back to sphere
    norms = np.linalg.norm(pts, axis=2, keepdims=True)
    pts = pts / norms

    X, Y, Z = pts[:, :, 0], pts[:, :, 1], pts[:, :, 2]

    # Keep positive octant
    mask = (X > 0.01) & (Y > 0.01) & (Z > 0.01)
    X[~mask] = np.nan
    Y[~mask] = np.nan
    Z[~mask] = np.nan

    return X, Y, Z


# ---------------------------------------------------------------------------
# 5. Brownian paths (diffusion sample paths on each manifold)
# ---------------------------------------------------------------------------

def brownian_on_sphere(start, n_steps=500, dt=0.001, seed=42):
    """Brownian motion on S²_+ with reflecting boundary."""
    rng = np.random.default_rng(seed)
    path = [start / np.linalg.norm(start)]
    for _ in range(n_steps):
        p = path[-1]
        # Tangent space noise
        noise = rng.normal(0, np.sqrt(dt), 3)
        noise -= np.dot(noise, p) * p  # Project to tangent plane
        p_new = p + noise
        p_new = np.abs(p_new)  # Reflect at boundary
        p_new /= np.linalg.norm(p_new)  # Project to sphere
        path.append(p_new)
    return np.array(path)


def jacobi_diffusion_path(b_star, kappa=2.0, n_steps=500, dt=0.002, seed=42):
    """
    Jacobi diffusion on the simplex (CAPM process).
    db_i = κ(b*_i - b_i)dt + √(b_i(δ_{ij} - b_j)/T) dW
    Mapped to S²_+ via Bhattacharyya.
    """
    rng = np.random.default_rng(seed)
    d = len(b_star)
    b = b_star.copy() + rng.normal(0, 0.05, d)
    b = np.abs(b)
    b /= b.sum()
    path = [bhattacharyya(b)]

    for _ in range(n_steps):
        drift = kappa * (b_star - b)
        # Simplified diffusion
        noise = rng.normal(0, np.sqrt(dt), d) * np.sqrt(b * (1 - b))
        b_new = b + drift * dt + noise * 0.3
        b_new = np.clip(b_new, 1e-6, None)
        b_new /= b_new.sum()
        b = b_new
        u = bhattacharyya(b)
        u /= np.linalg.norm(u)
        path.append(u)

    return np.array(path)


# ---------------------------------------------------------------------------
# Main figure: Four-panel visualisation
# ---------------------------------------------------------------------------

def plot_market_manifolds():
    fig = plt.figure(figsize=(20, 16))
    fig.suptitle(
        'The Geometry of Efficient Markets\n'
        r'Market manifold $M^r \subset S^{d-1}_+$ (Bhattacharyya sphere)',
        fontsize=16, fontweight='bold', y=0.98
    )

    # --- Panel 1: The ambient space S²_+ with simplex ---
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')
    X, Y, Z = positive_octant_sphere(50)
    ax1.plot_surface(X, Y, Z, alpha=0.08, color='lightblue', edgecolor='none')

    # Simplex edges on S²_+
    t = np.linspace(0, np.pi/2, 100)
    ax1.plot(np.cos(t), np.sin(t), np.zeros_like(t), 'k-', lw=1.5, alpha=0.5)
    ax1.plot(np.cos(t), np.zeros_like(t), np.sin(t), 'k-', lw=1.5, alpha=0.5)
    ax1.plot(np.zeros_like(t), np.cos(t), np.sin(t), 'k-', lw=1.5, alpha=0.5)

    # Equal-weight portfolio
    eq = bhattacharyya(np.array([1/3, 1/3, 1/3]))
    eq /= np.linalg.norm(eq)
    ax1.scatter(*eq, color='red', s=80, zorder=5)
    ax1.text(eq[0]+0.05, eq[1]+0.05, eq[2]+0.05, r'$b^* = \frac{1}{3}\mathbf{1}$',
             fontsize=10, color='red')

    ax1.set_title(r'Ambient space $S^2_+$ (Bhattacharyya sphere)', fontsize=12)
    ax1.set_xlabel(r'$\sqrt{b_1}$')
    ax1.set_ylabel(r'$\sqrt{b_2}$')
    ax1.set_zlabel(r'$\sqrt{b_3}$')
    ax1.view_init(25, 45)

    # --- Panel 2: CAPM great circle (β=1, GOE) ---
    ax2 = fig.add_subplot(2, 2, 2, projection='3d')
    X, Y, Z = positive_octant_sphere(40)
    ax2.plot_surface(X, Y, Z, alpha=0.06, color='lightblue', edgecolor='none')

    # Great circle
    gc = capm_great_circle(n=300)
    ax2.plot(gc[:, 0], gc[:, 1], gc[:, 2], 'b-', lw=3, label=r'$S^1_+$ (great circle)')

    # Jacobi diffusion path
    b_star = np.array([1/3, 1/3, 1/3])
    path = jacobi_diffusion_path(b_star, kappa=3.0, n_steps=800, dt=0.001, seed=42)
    ax2.plot(path[:, 0], path[:, 1], path[:, 2], 'r-', lw=0.5, alpha=0.6,
             label='Jacobi diffusion')
    ax2.scatter(*path[0], color='green', s=40, zorder=5)
    ax2.scatter(*path[-1], color='red', s=40, zorder=5)

    ax2.set_title(
        'Type I: CAPM Great Sphere\n'
        r'Jacobi diffusion · $\beta=1$ (GOE) · $K > 0$',
        fontsize=11
    )
    ax2.legend(fontsize=9, loc='upper left')
    ax2.view_init(25, 45)

    # --- Panel 3: Clifford torus (β=2, GUE) ---
    ax3 = fig.add_subplot(2, 2, 3, projection='3d')

    Xt, Yt, Zt = clifford_torus_on_sphere(n=80)
    ax3.plot_surface(Xt, Yt, Zt, alpha=0.5, cmap=cm.coolwarm, edgecolor='none',
                     antialiased=True)

    # Geodesic loops on the torus (the two generating circles)
    theta = np.linspace(0.1, np.pi/2 - 0.1, 200)
    # Circle 1: fix θ₂ = π/4
    t2_fixed = np.pi / 4
    w1 = np.cos(theta) / np.sqrt(2)
    x1 = np.sin(theta) / np.sqrt(2)
    y1 = np.cos(t2_fixed) / np.sqrt(2) * np.ones_like(theta)
    z1 = np.sin(t2_fixed) / np.sqrt(2) * np.ones_like(theta)
    denom1 = 1 + z1
    X1, Y1, Z1 = w1/denom1, x1/denom1, y1/denom1
    n1 = np.sqrt(X1**2 + Y1**2 + Z1**2)
    ax3.plot(X1/n1, Y1/n1, Z1/n1, 'k-', lw=2, label='Generating circles')

    # Circle 2: fix θ₁ = π/4
    t1_fixed = np.pi / 4
    w2 = np.cos(t1_fixed) / np.sqrt(2) * np.ones_like(theta)
    x2 = np.sin(t1_fixed) / np.sqrt(2) * np.ones_like(theta)
    y2 = np.cos(theta) / np.sqrt(2)
    z2 = np.sin(theta) / np.sqrt(2)
    denom2 = 1 + z2
    X2, Y2, Z2 = w2/denom2, x2/denom2, y2/denom2
    n2 = np.sqrt(X2**2 + Y2**2 + Z2**2)
    ax3.plot(X2/n2, Y2/n2, Z2/n2, 'k--', lw=2)

    ax3.set_title(
        'Type II: Clifford Torus\n'
        r'Flat torus BM · $\beta=2$ (GUE) · $K = 0$',
        fontsize=11
    )
    ax3.legend(fontsize=9, loc='upper left')
    ax3.view_init(30, 60)

    # --- Panel 4: Pseudo-Anosov / hyperbolic (β=4, GSE) ---
    ax4 = fig.add_subplot(2, 2, 4, projection='3d')

    Xh, Yh, Zh = hyperbolic_patch(amplitude=0.18, n=60)
    ax4.plot_surface(Xh, Yh, Zh, alpha=0.5, cmap=cm.RdYlGn_r, edgecolor='none',
                     antialiased=True)

    # Diverging geodesics (sensitive dependence)
    b0 = np.array([0.5, 0.3, 0.2])
    for seed in range(5):
        path = brownian_on_sphere(bhattacharyya(b0), n_steps=300, dt=0.0008,
                                  seed=seed+10)
        ax4.plot(path[:, 0], path[:, 1], path[:, 2], '-', lw=0.8, alpha=0.7)

    ax4.scatter(*bhattacharyya(b0)/np.linalg.norm(bhattacharyya(b0)),
                color='black', s=60, zorder=5)

    ax4.set_title(
        'Type III: Pseudo-Anosov (Hyperbolic)\n'
        r'McKean kernel · $\beta=4$ (GSE) · $K < 0$',
        fontsize=11
    )
    ax4.view_init(25, 35)

    # Common formatting
    for ax in [ax1, ax2, ax3, ax4]:
        ax.set_xlim(0, 1.05)
        ax.set_ylim(0, 1.05)
        ax.set_zlim(0, 1.05)
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.grid(True, alpha=0.3)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    return fig


# ---------------------------------------------------------------------------
# Curvature comparison figure
# ---------------------------------------------------------------------------

def plot_curvature_profiles():
    """
    Show how curvature varies across each manifold type,
    illustrating the Sharpe-curvature relationship.
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle(
        r'Mean curvature $|H|^2$ profiles — Sharpe$^* = \|H\|_{L^2}$',
        fontsize=14, fontweight='bold'
    )

    t = np.linspace(0, 1, 500)

    # CAPM: constant positive curvature on great sphere
    H_capm = np.ones_like(t) * 0.0  # Minimal → H=0 (efficient)
    H_capm_ineff = np.ones_like(t) * 0.3  # Inefficient: constant H
    axes[0].fill_between(t, 0, H_capm_ineff**2, alpha=0.3, color='blue',
                          label=r'Inefficient: $|H|^2 > 0$')
    axes[0].plot(t, H_capm, 'b-', lw=2, label=r'Efficient: $H = 0$')
    axes[0].set_title('CAPM (Great Sphere)\nConstant curvature', fontsize=11)
    axes[0].set_ylabel(r'$|H(b)|^2$')
    axes[0].set_xlabel('Position on manifold')
    axes[0].legend()
    axes[0].set_ylim(-0.02, 0.15)

    # Clifford torus: flat intrinsic curvature, can have extrinsic curvature
    H_cliff = 0.2 * np.sin(2 * np.pi * t) ** 2  # Periodic
    axes[1].fill_between(t, 0, H_cliff, alpha=0.3, color='red')
    axes[1].plot(t, H_cliff, 'r-', lw=2,
                 label=r'$|H|^2$ periodic (torus winding)')
    axes[1].axhline(y=0, color='gray', ls='--', alpha=0.5)
    axes[1].set_title('Clifford Torus\nFlat intrinsic, periodic extrinsic', fontsize=11)
    axes[1].set_xlabel('Position on manifold')
    axes[1].legend()
    axes[1].set_ylim(-0.02, 0.25)

    # Hyperbolic: curvature varies, can be large
    H_hyp = 0.1 * np.exp(2 * (t - 0.5)**2)  # Exponentially growing tails
    axes[2].fill_between(t, 0, H_hyp, alpha=0.3, color='green')
    axes[2].plot(t, H_hyp, 'g-', lw=2,
                 label=r'$|H|^2$ exponential (geodesic divergence)')
    axes[2].set_title('Pseudo-Anosov (Hyperbolic)\nExponentially varying', fontsize=11)
    axes[2].set_xlabel('Position on manifold')
    axes[2].legend()
    axes[2].set_ylim(-0.02, 0.15)

    for ax in axes:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    return fig


# ---------------------------------------------------------------------------
# Classification summary figure
# ---------------------------------------------------------------------------

def plot_classification_table():
    """Visual summary of the three market types."""
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.axis('off')

    headers = ['Property', 'Type I: CAPM', 'Type II: Clifford', 'Type III: Pseudo-Anosov']
    rows = [
        ['Manifold', r'$S^r_+$ (great sphere)', r'$T^2$ (Clifford torus)', r'$\mathbb{H}^2$ (hyperbolic)'],
        ['Curvature K', 'K > 0 (positive)', 'K = 0 (flat)', 'K < 0 (negative)'],
        ['Process', 'Jacobi diffusion', 'Flat torus BM', 'Hyperbolic BM'],
        ['Transition density', 'Jacobi polynomials', r'$\vartheta_3$ (theta fn)', 'McKean kernel'],
        ['Dyson class β', '1 (GOE)', '2 (GUE)', '4 (GSE)'],
        ['Tail behaviour', r'Power law $\alpha = r/2$', 'Exponential decay', 'Heavy power law'],
        ['Stability index', '0 (stable)', '5 (unstable)', '∞ (chaotic)'],
        ['Entropy', r'$h = \lambda_1$ (spectral gap)', r'$h = 0$ (flat)', r'$h = \log\lambda_{pA}$'],
        ['Example', 'S&P 500 / broad index', 'Balanced two-sector', 'Crisis / regime change'],
    ]

    colors = ['#e6f3ff', '#ffe6e6', '#e6ffe6']

    table = ax.table(
        cellText=rows, colLabels=headers,
        cellLoc='center', loc='center',
        colWidths=[0.18, 0.27, 0.27, 0.27]
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.8)

    # Style headers
    for j in range(4):
        table[0, j].set_facecolor('#2c3e50')
        table[0, j].set_text_props(color='white', fontweight='bold')

    # Style data cells
    for i in range(1, len(rows) + 1):
        table[i, 0].set_facecolor('#f5f5f5')
        table[i, 0].set_text_props(fontweight='bold')
        for j in range(1, 4):
            table[i, j].set_facecolor(colors[j-1])

    ax.set_title(
        'The Three Market Types — Classification Theorem\n'
        r'Only Type I (CAPM) is stably efficient ($H = 0$ with stability index 0)',
        fontsize=13, fontweight='bold', pad=20
    )

    plt.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    print("Generating market manifold visualisations...")

    fig1 = plot_market_manifolds()
    fig1.savefig('code/visualisation/market_manifolds.png', dpi=150, bbox_inches='tight')
    print("  → market_manifolds.png")

    fig2 = plot_curvature_profiles()
    fig2.savefig('code/visualisation/curvature_profiles.png', dpi=150, bbox_inches='tight')
    print("  → curvature_profiles.png")

    fig3 = plot_classification_table()
    fig3.savefig('code/visualisation/classification_table.png', dpi=150, bbox_inches='tight')
    print("  → classification_table.png")

    plt.show()
    print("Done.")
