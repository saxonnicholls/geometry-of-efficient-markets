# Copyright (c) 2026 Saxon Nicholls. MIT License. See LICENSE.
"""
curvature.py
------------
Mean curvature estimation for the market manifold M^r in S^{d-1}_+.

Central theorem of the monograph:
    Sharpe*(Sigma) = ||H||_{L^2(M, g_M)}

The mean curvature H measures the market's exploitable alpha budget.
The vol skew of index options equals -epsilon^2 * H^2 / (2*sigma_I).

Three estimators are implemented:
  1. Normal bundle projection (fast, requires b* and V_r)
  2. Rolling Sharpe proxy (empirical upper bound)
  3. Second fundamental form (exact, computationally intensive)
"""

import numpy as np
from typing import Dict, Optional, Tuple

try:
    from .kelly import (
        factor_subspace,
        fisher_information_matrix,
        log_optimal_portfolio,
        stable_rank,
    )
except ImportError:
    from kelly import (
        factor_subspace,
        fisher_information_matrix,
        log_optimal_portfolio,
        stable_rank,
    )


def _market_geometry_from_returns(
    returns: np.ndarray,
    n_factors: Optional[int] = None,
    variance_threshold: float = 0.95,
) -> Dict[str, np.ndarray]:
    """
    Shared geometric state for a return window.
    """
    b_star, L_star = log_optimal_portfolio(returns)
    F = fisher_information_matrix(b_star, 1 + returns)
    V_r, lambda_r, r = factor_subspace(
        F,
        r=n_factors,
        variance_threshold=variance_threshold,
    )
    return {
        "b_star": b_star,
        "L_star": float(L_star),
        "F": F,
        "V_r": V_r,
        "lambda_r": lambda_r,
        "r": r,
    }


def _manifold_volume_proxy(r: int) -> float:
    """
    Volume proxy for an r-dimensional efficient market manifold.
    """
    from math import gamma, pi

    return float((pi / 2) ** (r / 2) / gamma(r / 2 + 1))


def _cheeger_from_fisher(F: np.ndarray) -> float:
    """
    Lower-bound proxy for the Cheeger constant from the Fisher spectrum.
    """
    eigenvalues = np.linalg.eigvalsh(F)
    eigenvalues = np.sort(eigenvalues[eigenvalues > 1e-10])

    if len(eigenvalues) < 2:
        return 0.0

    return float(eigenvalues[1] / 2.0)


# ── Mean curvature: normal bundle projection method ───────────────────────────

def mean_curvature_normal_bundle(
    b_star: np.ndarray,
    V_r: np.ndarray,
) -> Tuple[float, np.ndarray]:
    """
    Mean curvature via normal bundle projection.

    The mean curvature vector of M^r in S^{d-1}_+ at b* is:
        H_vec = Pi_{NM}(1/(2*sqrt(b*)))

    where Pi_{NM} = I - V_r V_r^T projects onto the normal bundle.

    The scalar mean curvature:
        H = ||H_vec||_{g^FR}

    This is proportional to the market's alpha budget (Sharpe* = H).

    Parameters
    ----------
    b_star : (d,) log-optimal portfolio weights
    V_r    : (d, r) factor loading matrix (orthonormal columns)

    Returns
    -------
    H      : scalar mean curvature
    H_vec  : (d,) mean curvature vector in the normal bundle
    """
    d = len(b_star)
    b_star = np.maximum(b_star, 1e-15)

    # The vector 1/(2*sqrt(b*)) is the gradient of the Bhattacharyya map
    half_inv_sqrt = 1.0 / (2.0 * np.sqrt(b_star))

    # Project onto normal bundle N_{b*}M
    Pi_N = np.eye(d) - V_r @ V_r.T
    H_vec = Pi_N @ half_inv_sqrt

    # Scalar mean curvature in Fisher-Rao norm
    H = np.sqrt(np.sum(H_vec ** 2 / b_star))

    return float(H), H_vec


def mean_curvature_from_returns(
    returns: np.ndarray,
    n_factors: Optional[int] = None,
    variance_threshold: float = 0.95,
) -> Tuple[float, np.ndarray, np.ndarray, int]:
    """
    Full pipeline: returns -> b* -> F(b*) -> V_r -> H.

    Parameters
    ----------
    returns : (T, d) net return matrix
    n_factors : number of factors r; if None, determined by variance_threshold

    Returns
    -------
    H      : scalar mean curvature
    H_vec  : (d,) mean curvature vector
    b_star : (d,) log-optimal portfolio
    r      : number of factors used
    """
    geometry = _market_geometry_from_returns(
        returns,
        n_factors=n_factors,
        variance_threshold=variance_threshold,
    )
    H, H_vec = mean_curvature_normal_bundle(geometry["b_star"], geometry["V_r"])
    return H, H_vec, geometry["b_star"], geometry["r"]


# ── Willmore energy ───────────────────────────────────────────────────────────

def willmore_energy_proxy(
    returns: np.ndarray,
    window: int = 252,
    step: int = 21,
    n_factors: Optional[int] = None,
) -> np.ndarray:
    """
    Rolling estimate of the Willmore energy W(M) = integral of H^2 dVol_M.

    The Willmore energy is the total inefficiency of the market —
    it is zero iff the market is efficient (H=0 on M).

    Returns
    -------
    W : (n_windows,) rolling Willmore energy proxy = H^2 * vol(M)
    """
    T, d = returns.shape
    n_windows = (T - window) // step
    willmore = np.zeros(n_windows)

    for i in range(n_windows):
        start = i * step
        end = start + window
        window_data = returns[start:end]
        try:
            H, _, b_star, r = mean_curvature_from_returns(window_data, n_factors)
            vol_M = _manifold_volume_proxy(r)
            willmore[i] = H ** 2 * vol_M
        except Exception:
            willmore[i] = np.nan

    return willmore


# ── Sharpe ratio - curvature identity ────────────────────────────────────────

def sharpe_curvature_decomposition(
    returns: np.ndarray,
    n_factors: Optional[int] = None,
    variance_threshold: float = 0.95,
) -> dict:
    """
    Compute both sides of the central theorem:
        Sharpe*(Sigma) = ||H||_{L^2(M, g_M)}

    Also decomposes returns into tangential (factor) and normal (alpha) components.

    Returns
    -------
    dict with keys:
        'H'            : scalar mean curvature (theory: = Sharpe*)
        'H_vec'        : mean curvature vector
        'b_star'       : log-optimal portfolio
        'r'            : market manifold dimension
        'sharpe_realised'   : empirical Sharpe of the curvature strategy
        'sharpe_predicted'  : H * sqrt(vol(M)) [theory prediction]
        'V_r'          : factor loading matrix
        'factor_returns'    : tangential return component
        'alpha_returns'     : normal bundle return component
    """
    T, d = returns.shape
    geometry = _market_geometry_from_returns(
        returns,
        n_factors=n_factors,
        variance_threshold=variance_threshold,
    )
    b_star = geometry["b_star"]
    L_star = geometry["L_star"]
    F = geometry["F"]
    V_r = geometry["V_r"]
    lambda_r = geometry["lambda_r"]
    r = geometry["r"]
    H, H_vec = mean_curvature_normal_bundle(b_star, V_r)

    # The curvature strategy: go short mean curvature direction
    if H > 1e-10:
        strategy_direction = -H_vec / H
        strategy_returns = returns @ strategy_direction
        sharpe_realised = (
            np.mean(strategy_returns) / np.std(strategy_returns, ddof=1) * np.sqrt(252)
        )
    else:
        strategy_returns = np.zeros(T)
        sharpe_realised = 0.0

    # Theory prediction: Sharpe* = H * sqrt(vol(M))
    vol_M = _manifold_volume_proxy(r)
    sharpe_predicted = H * np.sqrt(vol_M)

    # Decompose returns into factor and idiosyncratic components
    factor_returns = returns @ (V_r @ V_r.T).T
    alpha_returns = returns - factor_returns

    return {
        "H": float(H),
        "H_vec": H_vec,
        "b_star": b_star,
        "r": r,
        "L_star": float(L_star),
        "sharpe_realised": float(sharpe_realised),
        "sharpe_predicted": float(sharpe_predicted),
        "V_r": V_r,
        "lambda_r": lambda_r,
        "fisher_matrix": F,
        "factor_returns": factor_returns,
        "alpha_returns": alpha_returns,
        "stable_rank": float(stable_rank(F)),
    }


def market_efficiency_profile(
    returns: np.ndarray,
    n_factors: Optional[int] = None,
    variance_threshold: float = 0.95,
) -> dict:
    """
    Multi-metric diagnostic profile for a return window.

    The profile separates four distinct questions:
      1. How much alpha budget exists locally?          -> H, willmore_proxy
      2. How much return variance sits off-manifold?    -> alpha_share
      3. How fragile is the manifold globally?          -> cheeger
      4. How crowded is the efficient allocation?       -> breadth, entropy
    """
    decomposition = sharpe_curvature_decomposition(
        returns,
        n_factors=n_factors,
        variance_threshold=variance_threshold,
    )
    b_star = decomposition["b_star"]
    lambda_r = decomposition["lambda_r"]
    r = decomposition["r"]
    d = returns.shape[1]

    centred_returns = returns - np.mean(returns, axis=0, keepdims=True)
    factor_projection = decomposition["V_r"] @ decomposition["V_r"].T
    factor_returns = centred_returns @ factor_projection.T
    alpha_returns = centred_returns - factor_returns

    total_variance = float(np.mean(np.sum(centred_returns ** 2, axis=1)))
    factor_variance = float(np.mean(np.sum(factor_returns ** 2, axis=1)))
    alpha_variance = float(np.mean(np.sum(alpha_returns ** 2, axis=1)))

    half_inv_sqrt = 1.0 / (2.0 * np.sqrt(np.maximum(b_star, 1e-15)))
    normal_projection_share = float(
        np.linalg.norm(decomposition["H_vec"]) /
        max(np.linalg.norm(half_inv_sqrt), 1e-15)
    )

    concentration = float(np.sum(b_star ** 2))
    effective_breadth = float(1.0 / max(concentration, 1e-15))
    normal_bundle_dimension = int(max(d - 1 - r, 0))
    cheeger = _cheeger_from_fisher(decomposition["fisher_matrix"])
    vol_M = _manifold_volume_proxy(r)

    if d > 1:
        weight_entropy = float(
            -np.sum(b_star * np.log(np.maximum(b_star, 1e-15))) / np.log(d)
        )
        normalized_breadth = float((effective_breadth - 1.0) / (d - 1.0))
    else:
        weight_entropy = 0.0
        normalized_breadth = 1.0

    if len(lambda_r) > 0:
        lambda_sum = float(lambda_r.sum())
        top_factor_share = float(lambda_r[0] / max(lambda_sum, 1e-15))
        if len(lambda_r) > 1:
            spectrum_probs = lambda_r / max(lambda_sum, 1e-15)
            factor_entropy = float(
                -np.sum(spectrum_probs * np.log(np.maximum(spectrum_probs, 1e-15)))
                / np.log(len(lambda_r))
            )
        else:
            factor_entropy = 1.0
    else:
        top_factor_share = 1.0
        factor_entropy = 0.0

    return {
        **decomposition,
        "alpha_share": float(alpha_variance / max(total_variance, 1e-15)),
        "factor_share": float(factor_variance / max(total_variance, 1e-15)),
        "alpha_beta_ratio": float(alpha_variance / max(factor_variance, 1e-15)),
        "willmore_proxy": float(decomposition["H"] ** 2 * vol_M),
        "cheeger": cheeger,
        "effective_breadth": effective_breadth,
        "normalized_breadth": normalized_breadth,
        "weight_entropy": weight_entropy,
        "top_factor_share": top_factor_share,
        "factor_entropy": factor_entropy,
        "normal_projection_share": normal_projection_share,
        "normal_bundle_dimension": normal_bundle_dimension,
        "portfolio_concentration": concentration,
        "sharpe_gap": float(
            decomposition["sharpe_realised"] - decomposition["sharpe_predicted"]
        ),
    }


# ── Cheeger constant estimation ───────────────────────────────────────────────

def cheeger_constant_estimate(
    returns: np.ndarray,
    n_factors: Optional[int] = None,
) -> float:
    """
    Estimate the Cheeger constant h_M of the market manifold.

    h_M = Fiedler eigenvalue / 2  (via Cheeger inequality approximation)

    The Cheeger constant is the systemic risk measure:
    - Large h_M: well-connected manifold, crisis contagion is limited
    - Small h_M: bottleneck forming, systemic risk is high
    - h_M -> 0:  manifold pinch-off imminent (financial crisis)

    Returns
    -------
    h_M : Cheeger constant estimate
    """
    geometry = _market_geometry_from_returns(
        returns,
        n_factors=n_factors,
    )
    return _cheeger_from_fisher(geometry["F"])


# ── Second fundamental form (exact, expensive) ────────────────────────────────

def second_fundamental_form(
    b_star: np.ndarray,
    V_r: np.ndarray,
    gross_returns: np.ndarray,
    eps: float = 1e-4,
) -> np.ndarray:
    """
    Numerical estimate of the second fundamental form II(X, Y) of M^r in S^{d-1}_+.

    II is a (r, r, d-r) tensor. Its trace gives the mean curvature vector H_vec.

    This is the exact (expensive) computation; mean_curvature_normal_bundle
    gives the fast approximation.

    Parameters
    ----------
    eps : finite difference step size

    Returns
    -------
    II : (r, r, d-1-r) second fundamental form tensor (approximated)
    """
    d = len(b_star)
    r = V_r.shape[1]
    n = d - 1 - r   # normal bundle dimension

    # Normal bundle basis (orthogonal complement of V_r within simplex tangent)
    tangent_basis = V_r
    full_basis = np.eye(d)
    # Gram-Schmidt to get normal bundle basis
    normal_vecs = []
    for i in range(d):
        v = full_basis[:, i].copy()
        # Subtract projections onto tangent and already-found normals
        for t in range(r):
            v -= np.dot(v, tangent_basis[:, t]) * tangent_basis[:, t]
        for nv in normal_vecs:
            v -= np.dot(v, nv) * nv
        norm = np.linalg.norm(v)
        if norm > eps:
            normal_vecs.append(v / norm)
            if len(normal_vecs) == n:
                break

    V_N = np.column_stack(normal_vecs) if normal_vecs else np.zeros((d, 0))

    # Second fundamental form: II(e_i, e_j) = Pi_N(D_{e_i} e_j)
    # Approximate via finite differences of the Christoffel symbols
    II = np.zeros((r, r, len(normal_vecs)))

    for i in range(r):
        for j in range(r):
            e_i = V_r[:, i]
            e_j = V_r[:, j]
            # Numerical second covariant derivative
            b_plus = b_star + eps * e_i
            b_plus = np.maximum(b_plus, 1e-10)
            b_plus /= b_plus.sum()
            b_minus = b_star - eps * e_i
            b_minus = np.maximum(b_minus, 1e-10)
            b_minus /= b_minus.sum()
            # Finite difference of e_j parallel transport (approx)
            d2b = (b_plus - 2 * b_star + b_minus) / eps ** 2
            # Project onto normal bundle
            for k, nv in enumerate(normal_vecs):
                II[i, j, k] = np.dot(d2b, nv)

    return II


if __name__ == "__main__":
    rng = np.random.default_rng(42)
    T, d = 504, 20
    # Simulate a 4-factor market
    factors = rng.normal(0, 0.01, (T, 4))
    loadings = rng.normal(0, 1, (d, 4))
    loadings /= np.linalg.norm(loadings, axis=0)
    idio = rng.normal(0, 0.005, (T, d))
    returns = factors @ loadings.T + idio

    result = sharpe_curvature_decomposition(returns, n_factors=4)

    print("=" * 50)
    print("Sharpe-Curvature Decomposition")
    print("=" * 50)
    print(f"Market manifold dimension r:  {result['r']}")
    print(f"Stable rank:                  {result['stable_rank']:.2f}")
    print(f"Mean curvature H:             {result['H']:.4f}")
    print(f"Kelly growth rate:            {result['L_star']:.6f}")
    print(f"Realised Sharpe (theory dir): {result['sharpe_realised']:.4f}")
    print(f"Predicted Sharpe (H*sqrt(V)): {result['sharpe_predicted']:.4f}")
    print(f"\nTheory: Sharpe* = ||H||_{{L²}} ≈ {result['sharpe_predicted']:.4f}")
