"""
fisher_rao.py
-------------
Fisher-Rao geometry on the portfolio simplex.

The Fisher-Rao metric on Delta_{d-1}:
    g^FR_ij(b) = delta_ij / b_i

The Bhattacharyya isometry maps b -> sqrt(b) in S^{d-1}_+,
where the metric becomes the standard round metric with K = 1/4.

All distances, geodesics, and projections are exact.
"""

import numpy as np
from typing import Tuple, Optional


# ── Core metric and distance ──────────────────────────────────────────────────

def bhattacharyya_map(b: np.ndarray) -> np.ndarray:
    """
    The Bhattacharyya isometry: b -> sqrt(b) in S^{d-1}_+.
    Maps (Delta_{d-1}, g^FR) isometrically to (S^{d-1}_+, g_round).
    """
    return np.sqrt(np.maximum(b, 0.0))


def inverse_bhattacharyya(u: np.ndarray) -> np.ndarray:
    """
    Inverse Bhattacharyya map: u -> u^2 (component-wise).
    Maps S^{d-1}_+ back to Delta_{d-1}.
    """
    b = u ** 2
    return b / b.sum(axis=-1, keepdims=True)


def fisher_rao_distance(b1: np.ndarray, b2: np.ndarray) -> float:
    """
    Fisher-Rao geodesic distance between two portfolios.

    d_FR(b1, b2) = 2 * arccos(sum_i sqrt(b1_i * b2_i))
                 = 2 * arccos(Bhattacharyya coefficient)

    This is the geodesic distance on S^{d-1}_+ with curvature K=1/4,
    equivalently the arc length in the Bhattacharyya hemisphere.

    Range: [0, pi/2]. Zero iff b1 == b2.
    """
    b1 = np.maximum(b1, 1e-15)
    b2 = np.maximum(b2, 1e-15)
    bc = np.sum(np.sqrt(b1 * b2))           # Bhattacharyya coefficient
    bc = np.clip(bc, -1.0, 1.0)
    return 2.0 * np.arccos(bc)


def bhattacharyya_coefficient(b1: np.ndarray, b2: np.ndarray) -> float:
    """
    Bhattacharyya coefficient: BC(b1,b2) = sum_i sqrt(b1_i * b2_i).
    Equals cos(d_FR/2). Range: [0, 1].
    """
    return float(np.sum(np.sqrt(np.maximum(b1, 0) * np.maximum(b2, 0))))


def tracking_error(b: np.ndarray, b_star: np.ndarray) -> float:
    """
    Fisher-Rao tracking error: how far b is from the log-optimal portfolio.
    This is the correct risk metric in Fisher-Rao geometry — not variance.

    TE = d_FR(b, b*) = 2 * arccos(sum_i sqrt(b_i * b*_i))
    """
    return fisher_rao_distance(b, b_star)


# ── Geodesics ─────────────────────────────────────────────────────────────────

def geodesic(
    b0: np.ndarray,
    b1: np.ndarray,
    t: float,
) -> np.ndarray:
    """
    Geodesic interpolation between b0 and b1 at parameter t in [0, 1].

    The geodesic on (Delta_{d-1}, g^FR) is a great circle arc on S^{d-1}_+.
    In Bhattacharyya coordinates: spherical linear interpolation (slerp).

    Parameters
    ----------
    b0 : start portfolio (t=0)
    b1 : end portfolio (t=1)
    t  : interpolation parameter in [0, 1]

    Returns
    -------
    b_t : portfolio at parameter t along the geodesic
    """
    u0 = bhattacharyya_map(b0)
    u1 = bhattacharyya_map(b1)

    # Spherical linear interpolation (slerp)
    cos_angle = np.dot(u0, u1)
    cos_angle = np.clip(cos_angle, -1.0, 1.0)
    angle = np.arccos(cos_angle)

    if angle < 1e-10:
        # Portfolios are essentially identical
        return b0.copy()

    u_t = (np.sin((1 - t) * angle) * u0 + np.sin(t * angle) * u1) / np.sin(angle)
    return inverse_bhattacharyya(u_t)


def geodesic_path(
    b0: np.ndarray,
    b1: np.ndarray,
    n_steps: int = 100,
) -> np.ndarray:
    """
    Discretised geodesic from b0 to b1.

    Returns
    -------
    path : (n_steps, d) array of portfolios along the geodesic
    """
    ts = np.linspace(0, 1, n_steps)
    return np.array([geodesic(b0, b1, t) for t in ts])


def damped_geodesic(
    b0: np.ndarray,
    b_star: np.ndarray,
    t: float,
    kappa: float,
    T: float,
) -> np.ndarray:
    """
    Critically damped geodesic execution schedule (Theorem 3.1 of
    STOCHASTIC_CONTROL_KALMAN.md).

    Optimal execution path minimising tracking penalty + trading cost:
        b(t) = exp_{b*}(-exp(-kappa*t) * log_{b*}(b0))

    Parameters
    ----------
    b0    : initial portfolio
    b_star: target log-optimal portfolio
    t     : current time in [0, T]
    kappa : damping rate = sqrt(tracking_penalty / trading_cost)
    T     : total execution horizon

    Returns
    -------
    b_t : optimal portfolio at time t
    """
    decay = np.exp(-kappa * t)
    return geodesic(b_star, b0, decay)


# ── Tangent and normal bundle projections ─────────────────────────────────────

def project_onto_factor_subspace(
    v: np.ndarray,
    V_r: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Decompose vector v into tangential (factor) and normal (idiosyncratic) components.

    Parameters
    ----------
    v   : (d,) vector (e.g., a return or a portfolio deviation)
    V_r : (d, r) factor loading matrix from kelly.factor_subspace()

    Returns
    -------
    v_tangential : projection onto TM (factor component)
    v_normal     : projection onto NM (idiosyncratic component)
    """
    v_tangential = V_r @ (V_r.T @ v)
    v_normal = v - v_tangential
    return v_tangential, v_normal


def fisher_rao_inner_product(
    v1: np.ndarray,
    v2: np.ndarray,
    b: np.ndarray,
) -> float:
    """
    Inner product in the Fisher-Rao metric at portfolio b.
    <v1, v2>_{g^FR} = sum_i v1_i * v2_i / b_i
    """
    b = np.maximum(b, 1e-15)
    return float(np.sum(v1 * v2 / b))


def fisher_rao_norm(v: np.ndarray, b: np.ndarray) -> float:
    """
    Norm of vector v in the Fisher-Rao metric at b.
    ||v||_{g^FR} = sqrt(sum_i v_i^2 / b_i)
    """
    return np.sqrt(max(fisher_rao_inner_product(v, v, b), 0.0))


# ── Exponential and logarithm maps ────────────────────────────────────────────

def exp_map(b: np.ndarray, v: np.ndarray) -> np.ndarray:
    """
    Riemannian exponential map at b in direction v.
    Maps tangent vector v at b to a point on Delta_{d-1}.

    In Bhattacharyya coordinates: standard spherical exponential map.
    """
    u = bhattacharyya_map(b)
    # Convert v to Bhattacharyya tangent: du = v / (2*sqrt(b))
    du = v / (2.0 * np.maximum(u, 1e-15))
    du_norm = np.linalg.norm(du)

    if du_norm < 1e-12:
        return b.copy()

    u_new = np.cos(du_norm) * u + np.sin(du_norm) * (du / du_norm)
    u_new = np.maximum(u_new, 0.0)
    return inverse_bhattacharyya(u_new)


def log_map(b_base: np.ndarray, b_target: np.ndarray) -> np.ndarray:
    """
    Riemannian logarithm map: tangent vector at b_base pointing toward b_target.
    Inverse of exp_map: exp_{b_base}(log_{b_base}(b_target)) = b_target.

    The Fisher-Rao distance equals ||log_{b_base}(b_target)||_{g^FR}.
    """
    u0 = bhattacharyya_map(b_base)
    u1 = bhattacharyya_map(b_target)

    cos_angle = np.dot(u0, u1)
    cos_angle = np.clip(cos_angle, -1.0, 1.0)
    angle = np.arccos(cos_angle)

    if angle < 1e-10:
        return np.zeros_like(b_base)

    # Tangent vector in Bhattacharyya coordinates
    du = angle * (u1 - cos_angle * u0) / np.sin(angle)

    # Convert back to simplex tangent: v = 2*sqrt(b) * du
    v = 2.0 * u0 * du
    return v


# ── Mean curvature estimation ──────────────────────────────────────────────────
# (See curvature.py for full implementation)

def mean_curvature_proxy(
    b_star: np.ndarray,
    V_r: np.ndarray,
) -> float:
    """
    Fast proxy for the mean curvature ||H|| of the market manifold.

    H = Pi_{NM}(1/(2*sqrt(b*))) — projection of the half-inverse-sqrt
    vector onto the normal bundle.

    This proxy requires only b* and the factor loading matrix V_r.
    Full computation is in curvature.py.
    """
    d = len(b_star)
    half_inv_sqrt = 1.0 / (2.0 * np.sqrt(np.maximum(b_star, 1e-15)))

    # Normal bundle projection
    Pi_N = np.eye(d) - V_r @ V_r.T
    H_vec = Pi_N @ half_inv_sqrt
    return float(np.linalg.norm(H_vec))


# ── Pairwise distance matrix ───────────────────────────────────────────────────

def pairwise_fr_distances(portfolios: np.ndarray) -> np.ndarray:
    """
    Compute pairwise Fisher-Rao distances between N portfolios.

    Parameters
    ----------
    portfolios : (N, d) array of portfolio weights

    Returns
    -------
    D : (N, N) symmetric distance matrix
    """
    N = portfolios.shape[0]
    U = np.sqrt(np.maximum(portfolios, 0))   # Bhattacharyya coords
    # Dot products
    dots = U @ U.T
    dots = np.clip(dots, -1.0, 1.0)
    return 2.0 * np.arccos(dots)


if __name__ == "__main__":
    rng = np.random.default_rng(42)
    d = 5
    b1 = rng.dirichlet(np.ones(d))
    b2 = rng.dirichlet(np.ones(d))
    b_star = np.ones(d) / d   # equal weight as proxy for log-optimal

    dist = fisher_rao_distance(b1, b2)
    te   = tracking_error(b1, b_star)
    path = geodesic_path(b1, b2, n_steps=10)

    print(f"Fisher-Rao distance b1->b2:      {dist:.4f}")
    print(f"Tracking error b1 from b_star:   {te:.4f}")
    print(f"Geodesic path shape:             {path.shape}")
    print(f"Geodesic endpoint (should=b2):   {path[-1].round(4)}")
    print(f"All weights sum to 1:            {np.allclose(path.sum(1), 1.0)}")
