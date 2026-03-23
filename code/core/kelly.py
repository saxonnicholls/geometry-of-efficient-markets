"""
kelly.py
--------
Log-optimal (Kelly) portfolio solver on the market manifold.

The log-optimal portfolio b* maximises the expected log-growth rate:
    L_T(b) = (1/T) sum_t log(<b, x_t>)

where x_t are gross returns (1 + r_t).

Core of "The Geometry of Efficient Markets" —
every other quantity in the monograph is derived from b*.
"""

import numpy as np
from scipy.optimize import minimize
from scipy.linalg import eigh
from typing import Optional, Tuple
import warnings


# ── Kelly growth rate ────────────────────────────────────────────────────────

def kelly_growth_rate(b: np.ndarray, gross_returns: np.ndarray) -> float:
    """
    L_T(b) = (1/T) sum_t log(<b, x_t>)

    Parameters
    ----------
    b : (d,) portfolio weights, must sum to 1, non-negative
    gross_returns : (T, d) gross return matrix (1 + r_t)

    Returns
    -------
    float : average log-growth rate
    """
    b = np.maximum(b, 1e-12)
    portfolio_returns = gross_returns @ b
    portfolio_returns = np.maximum(portfolio_returns, 1e-12)
    return np.mean(np.log(portfolio_returns))


def kelly_gradient(b: np.ndarray, gross_returns: np.ndarray) -> np.ndarray:
    """
    Gradient of L_T(b) with respect to b.
    grad_i L_T = (1/T) sum_t x_{t,i} / <b, x_t>
    """
    b = np.maximum(b, 1e-12)
    portfolio_returns = np.maximum(gross_returns @ b, 1e-12)
    return np.mean(gross_returns / portfolio_returns[:, None], axis=0)


def kelly_hessian(b: np.ndarray, gross_returns: np.ndarray) -> np.ndarray:
    """
    Hessian of L_T(b). This is the negative Fisher information matrix F(b*).
    H_ij = -(1/T) sum_t x_{t,i} x_{t,j} / <b, x_t>^2
    """
    b = np.maximum(b, 1e-12)
    portfolio_returns = np.maximum(gross_returns @ b, 1e-12)
    weighted = gross_returns / portfolio_returns[:, None]          # (T, d)
    return -np.mean(weighted[:, :, None] * weighted[:, None, :], axis=0)


# ── Log-optimal portfolio solver ─────────────────────────────────────────────

def log_optimal_portfolio(
    returns: np.ndarray,
    method: str = "slsqp",
    initial_weights: Optional[np.ndarray] = None,
    tol: float = 1e-10,
    max_iter: int = 500,
    min_weight: float = 1e-6,
) -> Tuple[np.ndarray, float]:
    """
    Compute the log-optimal (Kelly) portfolio.

    Parameters
    ----------
    returns : (T, d) net returns matrix (r_t, not 1+r_t)
    method  : optimisation method — 'slsqp' (default), 'natural_gradient'
    initial_weights : (d,) starting point; defaults to equal weight
    tol     : convergence tolerance
    max_iter: maximum iterations
    min_weight : floor on portfolio weights (Feller boundary protection)

    Returns
    -------
    b_star : (d,) log-optimal portfolio weights
    L_star : float, log-growth rate at b_star
    """
    T, d = returns.shape
    gross = 1.0 + returns

    if initial_weights is None:
        b0 = np.ones(d) / d
    else:
        b0 = np.array(initial_weights, dtype=float)
        b0 = np.maximum(b0, min_weight)
        b0 /= b0.sum()

    if method == "slsqp":
        def neg_kelly(b):
            return -kelly_growth_rate(b, gross)

        def neg_kelly_grad(b):
            return -kelly_gradient(b, gross)

        constraints = [{"type": "eq", "fun": lambda b: b.sum() - 1.0}]
        bounds = [(min_weight, 1.0)] * d

        result = minimize(
            neg_kelly,
            b0,
            jac=neg_kelly_grad,
            method="SLSQP",
            bounds=bounds,
            constraints=constraints,
            options={"ftol": tol, "maxiter": max_iter},
        )

        if not result.success:
            warnings.warn(f"Kelly optimisation: {result.message}")

        b_star = np.maximum(result.x, min_weight)
        b_star /= b_star.sum()

    elif method == "natural_gradient":
        b_star = _natural_gradient_kelly(gross, b0, tol, max_iter, min_weight)

    else:
        raise ValueError(f"Unknown method: {method}. Use 'slsqp' or 'natural_gradient'.")

    L_star = kelly_growth_rate(b_star, gross)
    return b_star, L_star


def _natural_gradient_kelly(
    gross: np.ndarray,
    b0: np.ndarray,
    tol: float,
    max_iter: int,
    min_weight: float,
) -> np.ndarray:
    """
    Natural gradient ascent on the simplex.
    The natural gradient uses the Fisher-Rao metric as the preconditioner:
        b_{t+1} = b_t + eta * F(b_t)^{-1} * grad L_T(b_t)
    This converges much faster than Euclidean gradient near b*.
    """
    b = b0.copy()
    d = len(b)

    for _ in range(max_iter):
        grad = kelly_gradient(b, gross)

        # Fisher-Rao metric at b: F_ii = 1/b_i (diagonal)
        # Natural gradient = F^{-1} grad = b * grad (component-wise)
        nat_grad = b * grad
        nat_grad -= nat_grad.mean()    # project onto simplex tangent

        # Line search
        eta = 0.1
        for _ in range(20):
            b_new = b + eta * nat_grad
            b_new = np.maximum(b_new, min_weight)
            b_new /= b_new.sum()
            if kelly_growth_rate(b_new, gross) > kelly_growth_rate(b, gross):
                break
            eta *= 0.5

        b = b_new
        if np.max(np.abs(nat_grad)) < tol:
            break

    return b


# ── Fisher information matrix ────────────────────────────────────────────────

def fisher_information_matrix(b_star: np.ndarray, gross_returns: np.ndarray) -> np.ndarray:
    """
    F(b*) = -Hessian of L_T at b*.
    This is the Fisher information matrix of the log-optimal portfolio.

    In the Fisher-Rao geometry: F is the metric tensor at b*.
    The Van Vleck-Morette determinant = det(F(b*)).
    The Kalman steady-state covariance = F(b*)^{-1}.
    """
    return -kelly_hessian(b_star, gross_returns)


def stable_rank(cov_or_fisher: np.ndarray) -> float:
    """
    Stable rank = tr(F)^2 / tr(F^2) = effective manifold dimension r.

    This is the key estimator of the market manifold dimension r.
    Range: [1, d]. Equals d for isotropic, 1 for rank-1.
    """
    eigenvalues = np.linalg.eigvalsh(cov_or_fisher)
    eigenvalues = eigenvalues[eigenvalues > 0]
    if len(eigenvalues) == 0:
        return 1.0
    return (eigenvalues.sum() ** 2) / (eigenvalues ** 2).sum()


def factor_subspace(
    cov_or_fisher: np.ndarray,
    r: Optional[int] = None,
    variance_threshold: float = 0.95,
) -> Tuple[np.ndarray, np.ndarray, int]:
    """
    Extract the r-dimensional factor subspace from the Fisher/covariance matrix.

    Parameters
    ----------
    r : number of factors; if None, determined by variance_threshold
    variance_threshold : fraction of variance to retain if r is None

    Returns
    -------
    V_r      : (d, r) factor loading matrix (columns = factor directions)
    lambda_r : (r,) factor eigenvalues
    r        : effective number of factors
    """
    eigenvalues, eigenvectors = eigh(cov_or_fisher)
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    eigenvalues = np.maximum(eigenvalues, 0)

    if r is None:
        cumvar = np.cumsum(eigenvalues) / eigenvalues.sum()
        r = int(np.searchsorted(cumvar, variance_threshold)) + 1

    return eigenvectors[:, :r], eigenvalues[:r], r


# ── Convenience wrappers ─────────────────────────────────────────────────────

def rolling_kelly(
    returns: np.ndarray,
    window: int = 252,
    step: int = 1,
    **kwargs,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Rolling log-optimal portfolio estimation.

    Returns
    -------
    b_stars : (n_windows, d) rolling log-optimal weights
    L_stars : (n_windows,) rolling Kelly growth rates
    """
    T, d = returns.shape
    n_windows = (T - window) // step + 1

    b_stars = np.zeros((n_windows, d))
    L_stars = np.zeros(n_windows)

    for i in range(n_windows):
        start = i * step
        end = start + window
        window_returns = returns[start:end]
        b_stars[i], L_stars[i] = log_optimal_portfolio(window_returns, **kwargs)

    return b_stars, L_stars


if __name__ == "__main__":
    # Quick smoke test
    rng = np.random.default_rng(42)
    T, d = 504, 10
    returns = rng.normal(0.0005, 0.02, (T, d))

    b_star, L_star = log_optimal_portfolio(returns)
    F = fisher_information_matrix(b_star, 1 + returns)
    r = stable_rank(F)

    print(f"Log-optimal portfolio: {b_star.round(4)}")
    print(f"Kelly growth rate:     {L_star:.6f}")
    print(f"Stable rank (r̂):      {r:.2f}")
    print(f"Sum of weights:        {b_star.sum():.6f}")
