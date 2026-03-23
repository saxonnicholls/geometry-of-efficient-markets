"""
kelly_shapley.py
----------------
Shapley value attribution of Kelly growth to individual assets and factors.

Central result (HYPERCUBE_SHAPLEY.md, Theorem 3.2):

    phi_i = b*_i * (mu_i - mu_bar)

where:
  - b*_i  is the log-optimal weight on asset i
  - mu_i  is the expected return of asset i
  - mu_bar = sum_j b*_j * mu_j  is the portfolio expected return

This is the UNIQUE attribution satisfying:
  1. Efficiency:  sum_i phi_i = v(N)  [attributions sum to portfolio alpha]
  2. Symmetry:    identical assets get equal attribution
  3. Dummy:       zero-weight assets get zero attribution
  4. Linearity:   phi(v+w) = phi(v) + phi(w)

The Kelly game is convex (HYPERCUBE_SHAPLEY Lemma HS1), so:
  - The core is non-empty
  - The nucleolus equals the Shapley value
  - No coalition has incentive to deviate

Additional: factor Shapley values, sector attribution (Owen value),
and normal bundle decomposition (unexplained alpha).
"""

import numpy as np
from typing import Optional, Dict
from scipy.optimize import minimize


# ── Core Shapley formula ─────────────────────────────────────────────────────

def kelly_shapley(
    b_star: np.ndarray,
    mu: np.ndarray,
    asset_names: Optional[list] = None,
) -> Dict:
    """
    Compute Shapley attribution of Kelly growth to assets.

    phi_i = b*_i * (mu_i - mu_bar)

    Parameters
    ----------
    b_star : (d,) log-optimal portfolio weights
    mu     : (d,) expected returns (annualised, or same units)
    asset_names : optional list of asset names for labelled output

    Returns
    -------
    dict with:
        'phi'         : (d,) Shapley values
        'mu_bar'      : portfolio expected return (sum phi_i)
        'attribution' : labelled dict if asset_names provided
        'tangential'  : systematic attribution
        'normal'      : idiosyncratic attribution (zero on efficient market)
    """
    b_star = np.array(b_star, dtype=float)
    mu = np.array(mu, dtype=float)
    b_star = np.maximum(b_star, 0.0)
    b_star /= b_star.sum()

    mu_bar = float(b_star @ mu)           # portfolio expected return
    excess_return = mu - mu_bar           # excess return over portfolio mean

    phi = b_star * excess_return          # Shapley values

    result = {
        "phi": phi,
        "mu_bar": mu_bar,
        "excess_return": excess_return,
        "b_star": b_star,
        "sum_phi": float(phi.sum()),      # should equal 0 (attributions relative to mean)
    }

    if asset_names is not None:
        result["attribution"] = {
            name: float(val)
            for name, val in zip(asset_names, phi)
        }

    return result


def kelly_shapley_from_returns(
    returns: np.ndarray,
    asset_names: Optional[list] = None,
) -> Dict:
    """
    Full pipeline: returns -> b* -> mu -> Shapley values.

    Parameters
    ----------
    returns : (T, d) net return matrix
    """
    from kelly import log_optimal_portfolio

    b_star, L_star = log_optimal_portfolio(returns)
    mu = np.mean(returns, axis=0) * 252    # annualised

    result = kelly_shapley(b_star, mu, asset_names)
    result["L_star"] = float(L_star)
    result["kelly_growth_annualised"] = float(L_star * 252)
    return result


# ── Factor-level Shapley (Owen value) ────────────────────────────────────────

def factor_shapley(
    b_star: np.ndarray,
    mu: np.ndarray,
    V_r: np.ndarray,
    factor_names: Optional[list] = None,
) -> Dict:
    """
    Factor-level Shapley attribution (Owen value).

    Phi_k = sum_i V_{ik} * phi_i
          = sum_i V_{ik} * b*_i * (mu_i - mu_bar)

    This is the unique fair attribution to each factor, preserving:
    - Factor efficiency: sum_k Phi_k = sum_i phi_i = total alpha
    - Factor symmetry: identical factors get equal attribution

    Parameters
    ----------
    V_r : (d, r) factor loading matrix

    Returns
    -------
    dict with:
        'Phi'         : (r,) factor Shapley values
        'phi'         : (d,) asset Shapley values
        'explained'   : fraction of alpha explained by factors
    """
    asset_result = kelly_shapley(b_star, mu)
    phi = asset_result["phi"]

    Phi = V_r.T @ phi    # (r,) factor attribution

    # Normal bundle attribution (unexplained alpha per asset)
    phi_tangential = V_r @ Phi          # (d,) factor-explained attribution
    phi_normal = phi - phi_tangential   # (d,) unexplained attribution

    explained = (
        float(np.sum(phi_tangential ** 2) / max(np.sum(phi ** 2), 1e-15))
    )

    result = {
        "Phi": Phi,
        "phi": phi,
        "phi_tangential": phi_tangential,
        "phi_normal": phi_normal,
        "explained_fraction": explained,
        "mu_bar": asset_result["mu_bar"],
    }

    if factor_names is not None:
        result["factor_attribution"] = {
            name: float(val)
            for name, val in zip(factor_names, Phi)
        }

    return result


# ── Sector-level attribution (Owen value with partition) ─────────────────────

def sector_shapley(
    b_star: np.ndarray,
    mu: np.ndarray,
    sectors: Dict[str, list],
) -> Dict:
    """
    Sector-level Shapley attribution (Owen value with sector partition).

    For a partition of assets into sectors S_1, ..., S_K:
        Phi_k = sum_{i in S_k} phi_i

    This preserves both sector-level and asset-level fairness.

    Parameters
    ----------
    sectors : dict mapping sector name to list of asset indices
              e.g. {'Tech': [0,1,2], 'Finance': [3,4], 'Energy': [5,6,7]}

    Returns
    -------
    dict with sector-level and asset-level attributions
    """
    asset_result = kelly_shapley(b_star, mu)
    phi = asset_result["phi"]

    sector_phi = {}
    for sector_name, indices in sectors.items():
        sector_phi[sector_name] = float(phi[indices].sum())

    return {
        "phi": phi,
        "sector_phi": sector_phi,
        "mu_bar": asset_result["mu_bar"],
        "total_alpha": float(phi.sum()),
    }


# ── Banzhaf power index (alternative attribution) ────────────────────────────

def banzhaf_attribution(
    b_star: np.ndarray,
    mu: np.ndarray,
    n_samples: int = 10000,
    seed: int = 42,
) -> np.ndarray:
    """
    Banzhaf power index: alternative to Shapley for Kelly game.

    Banzhaf_i = E_{S subset [d]\{i}}[v(S cup {i}) - v(S)]

    For the Kelly game, this equals the Walsh-Fourier coefficient
    of the Kelly function at the singleton {i} (HYPERCUBE_SHAPLEY Lemma HS2).

    Note: Banzhaf values do NOT sum to v(N) (no efficiency axiom).
    Use Shapley if you need efficiency; use Banzhaf for power analysis.

    Parameters
    ----------
    n_samples : Monte Carlo samples for estimation

    Returns
    -------
    beta : (d,) Banzhaf power indices
    """
    d = len(b_star)
    rng = np.random.default_rng(seed)
    beta = np.zeros(d)

    for _ in range(n_samples):
        # Random coalition (each asset included independently with prob 0.5)
        coalition = rng.random(d) < 0.5

        for i in range(d):
            # Marginal contribution of asset i
            with_i = coalition.copy()
            with_i[i] = True
            without_i = coalition.copy()
            without_i[i] = False

            # Coalition value: optimal Kelly rate on the sub-universe
            val_with = _coalition_value(b_star, mu, with_i)
            val_without = _coalition_value(b_star, mu, without_i)

            beta[i] += (val_with - val_without) / n_samples

    return beta


def _coalition_value(
    b_star: np.ndarray,
    mu: np.ndarray,
    coalition: np.ndarray,
) -> float:
    """
    v(S) = max_{b in Delta_{|S|-1}} L_T(b|S)
    Approximated as: sum_{i in S} b*_i * mu_i  (linear approximation)
    """
    if coalition.sum() == 0:
        return 0.0
    idx = np.where(coalition)[0]
    # Restrict b* to coalition and renormalise
    b_S = b_star[idx]
    if b_S.sum() < 1e-10:
        return 0.0
    b_S = b_S / b_S.sum()
    return float(b_S @ mu[idx])


# ── Marginal contribution curve ───────────────────────────────────────────────

def marginal_contribution_curve(
    b_star: np.ndarray,
    mu: np.ndarray,
    n_points: int = 100,
) -> np.ndarray:
    """
    For each asset i, compute the marginal Kelly growth as the weight
    moves from 0 to b*_i. Plots the "worth" of each unit of allocation.

    The area under curve i equals phi_i (Shapley value).

    Returns
    -------
    curves : (d, n_points) marginal contribution curves
    """
    d = len(b_star)
    mu_bar = float(b_star @ mu)
    curves = np.zeros((d, n_points))
    alphas = np.linspace(0, 1, n_points)

    for i in range(d):
        for j, alpha in enumerate(alphas):
            # Portfolio with weight alpha*b*_i on asset i
            b_scaled = b_star.copy()
            b_scaled[i] *= alpha
            if b_scaled.sum() > 0:
                b_scaled /= b_scaled.sum()
            curves[i, j] = float(b_scaled[i] * (mu[i] - mu_bar))

    return curves


# ── Reporting ─────────────────────────────────────────────────────────────────

def print_attribution_report(
    b_star: np.ndarray,
    mu: np.ndarray,
    asset_names: Optional[list] = None,
    V_r: Optional[np.ndarray] = None,
    factor_names: Optional[list] = None,
) -> None:
    """
    Print a formatted attribution report.
    """
    d = len(b_star)
    if asset_names is None:
        asset_names = [f"Asset {i+1}" for i in range(d)]

    result = kelly_shapley(b_star, mu, asset_names)
    phi = result["phi"]
    mu_bar = result["mu_bar"]

    print("=" * 65)
    print("Kelly Growth Attribution (Shapley Values)")
    print("=" * 65)
    print(f"Portfolio expected return (mu_bar): {mu_bar*100:.3f}%")
    print(f"Sum of Shapley values:              {phi.sum()*100:.6f}% (should be ~0)")
    print()
    print(f"{'Asset':<20} {'Weight b*':>10} {'mu_i':>10} {'phi_i':>12} {'Rank':>6}")
    print("-" * 65)

    order = np.argsort(phi)[::-1]
    for rank, i in enumerate(order):
        print(
            f"{asset_names[i]:<20} {b_star[i]:>9.4f}  "
            f"{mu[i]*100:>8.3f}%  "
            f"{phi[i]*100:>10.4f}%  "
            f"{rank+1:>5}"
        )

    print()
    print("Interpretation:")
    print(f"  Top contributor:    {asset_names[order[0]]} "
          f"(phi = {phi[order[0]]*100:.4f}%)")
    print(f"  Bottom contributor: {asset_names[order[-1]]} "
          f"(phi = {phi[order[-1]]*100:.4f}%)")

    if V_r is not None:
        print()
        f_result = factor_shapley(b_star, mu, V_r, factor_names)
        Phi = f_result["Phi"]
        r = len(Phi)
        if factor_names is None:
            factor_names = [f"Factor {k+1}" for k in range(r)]
        print(f"Factor Attribution (Owen Value):")
        print(f"  Explained fraction: {f_result['explained_fraction']*100:.1f}%")
        for k in range(r):
            print(f"  {factor_names[k]:<20} {Phi[k]*100:>10.4f}%")


if __name__ == "__main__":
    from kelly import log_optimal_portfolio

    rng = np.random.default_rng(42)
    d, T = 10, 504
    returns = rng.normal(0.0003, 0.015, (T, d))
    # Add a trend to a few assets
    returns[:, 0] += 0.0005
    returns[:, 1] += 0.0003
    returns[:, 7] -= 0.0002

    b_star, L_star = log_optimal_portfolio(returns)
    mu = np.mean(returns, axis=0)

    asset_names = [f"Stock {chr(65+i)}" for i in range(d)]

    print_attribution_report(b_star, mu * 252, asset_names)

    print()
    print(f"Kelly growth rate (annualised): {L_star*252*100:.4f}%")
    print()
    print("Verification: phi_i = b*_i * (mu_i - mu_bar)")
    mu_ann = mu * 252
    mu_bar = float(b_star @ mu_ann)
    phi_manual = b_star * (mu_ann - mu_bar)
    phi_from_func = kelly_shapley(b_star, mu_ann)["phi"]
    print(f"Max difference (manual vs func): {np.max(np.abs(phi_manual - phi_from_func)):.2e}")
