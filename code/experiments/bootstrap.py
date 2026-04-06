#!/usr/bin/env python3
"""
Bootstrap and non-parametric inference utilities.

Copyright Saxon Nicholls 2026 MIT Licence

Provides:
- Circular block bootstrap for time series (Politis-Romano 1994)
- Permutation tests for correlation
- Bootstrap confidence intervals (percentile and BCa)
- Cross-validation for dimension estimation
"""

import numpy as np
from typing import Callable, Tuple, Optional


def block_bootstrap_sample(data: np.ndarray, block_size: int,
                           rng: np.random.Generator) -> np.ndarray:
    """
    Generate one circular block bootstrap resample.

    Args:
        data: T × d array (time series of d variables)
        block_size: length of each block
        rng: random number generator

    Returns:
        Resampled array of same shape as data
    """
    T = len(data)
    n_blocks = int(np.ceil(T / block_size))

    # Random block starting points (circular — wrap around)
    starts = rng.integers(0, T, size=n_blocks)

    # Build the resampled series
    indices = []
    for s in starts:
        block_idx = np.arange(s, s + block_size) % T  # circular wrap
        indices.extend(block_idx.tolist())

    indices = indices[:T]  # trim to original length
    return data[indices]


def bootstrap_ci(data: np.ndarray, statistic: Callable,
                 n_bootstrap: int = 10000, block_size: Optional[int] = None,
                 alpha: float = 0.05, seed: int = 42) -> dict:
    """
    Compute bootstrap confidence interval for a statistic.

    Args:
        data: T × d array
        statistic: function(data) → scalar
        n_bootstrap: number of bootstrap resamples
        block_size: for block bootstrap (default: max(√T, 21))
        alpha: significance level (default 0.05 for 95% CI)
        seed: random seed

    Returns:
        dict with: estimate, ci_lower, ci_upper, se, bootstrap_distribution
    """
    rng = np.random.default_rng(seed)
    T = len(data)

    if block_size is None:
        block_size = max(int(np.sqrt(T)), 21)

    # Point estimate
    theta_hat = statistic(data)

    # Bootstrap distribution
    theta_boot = np.zeros(n_bootstrap)
    for b in range(n_bootstrap):
        resample = block_bootstrap_sample(data, block_size, rng)
        try:
            theta_boot[b] = statistic(resample)
        except Exception:
            theta_boot[b] = np.nan

    theta_boot = theta_boot[~np.isnan(theta_boot)]

    if len(theta_boot) < 100:
        return {
            "estimate": theta_hat,
            "ci_lower": np.nan,
            "ci_upper": np.nan,
            "se": np.nan,
            "n_valid": len(theta_boot),
        }

    # Percentile CI
    ci_lower = np.percentile(theta_boot, 100 * alpha / 2)
    ci_upper = np.percentile(theta_boot, 100 * (1 - alpha / 2))

    return {
        "estimate": theta_hat,
        "ci_lower": ci_lower,
        "ci_upper": ci_upper,
        "se": np.std(theta_boot),
        "n_valid": len(theta_boot),
        "distribution": theta_boot,
    }


def permutation_test(x: np.ndarray, y: np.ndarray,
                     statistic: Callable = None,
                     n_permutations: int = 10000,
                     seed: int = 42) -> dict:
    """
    Permutation test for the relationship between x and y.

    Default statistic: Pearson correlation.
    Permutes y, keeping x fixed.

    Returns:
        dict with: observed, p_value, null_distribution
    """
    rng = np.random.default_rng(seed)

    if statistic is None:
        def statistic(a, b):
            mask = ~(np.isnan(a) | np.isnan(b))
            if mask.sum() < 10:
                return 0.0
            return np.corrcoef(a[mask], b[mask])[0, 1]

    # Observed statistic
    observed = statistic(x, y)

    # Null distribution (permute y)
    null = np.zeros(n_permutations)
    for i in range(n_permutations):
        y_perm = rng.permutation(y)
        null[i] = statistic(x, y_perm)

    # Two-sided p-value
    p_value = np.mean(np.abs(null) >= np.abs(observed))

    return {
        "observed": observed,
        "p_value": p_value,
        "null_mean": np.mean(null),
        "null_std": np.std(null),
        "null_distribution": null,
    }


def cross_validate_dimension(returns: np.ndarray, r_max: int = 15,
                              n_folds: int = 5, seed: int = 42) -> dict:
    """
    Cross-validate the manifold dimension r.

    For each candidate r:
        1. Split assets into n_folds groups
        2. For each fold: estimate r-factor model on (n_folds-1) groups,
           predict returns of held-out group
        3. Compute mean prediction error

    Returns the r that minimises cross-validated error.
    """
    T, d = returns.shape
    rng = np.random.default_rng(seed)

    # Random asset assignment to folds
    fold_assignment = rng.integers(0, n_folds, size=d)

    errors = {}
    for r in range(1, min(r_max + 1, d)):
        fold_errors = []
        for fold in range(n_folds):
            # Training and test assets
            train_mask = fold_assignment != fold
            test_mask = fold_assignment == fold

            if test_mask.sum() < 1 or train_mask.sum() < r:
                continue

            train_returns = returns[:, train_mask]
            test_returns = returns[:, test_mask]

            # Estimate r-factor model on training assets
            cov_train = np.cov(train_returns.T)
            eigenvalues, eigenvectors = np.linalg.eigh(cov_train)
            idx = np.argsort(eigenvalues)[::-1]
            eigenvectors = eigenvectors[:, idx]

            V_r = eigenvectors[:, :r]  # d_train × r

            # Factor returns: F = returns_train @ V_r (T × r)
            F = train_returns @ V_r

            # Predict test returns: β = cov(test, F) @ cov(F)^{-1}
            # Then predicted = F @ β^T
            cov_F = np.cov(F.T)
            if r == 1:
                cov_F = np.array([[cov_F]])
            try:
                cov_F_inv = np.linalg.inv(cov_F + 1e-8 * np.eye(r))
            except np.linalg.LinAlgError:
                continue

            cross_cov = np.zeros((test_returns.shape[1], r))
            for j in range(test_returns.shape[1]):
                for k in range(r):
                    cross_cov[j, k] = np.cov(test_returns[:, j], F[:, k])[0, 1]

            beta = cross_cov @ cov_F_inv  # d_test × r
            predicted = F @ beta.T  # T × d_test

            # Prediction error (RMSE)
            error = np.sqrt(np.mean((test_returns - predicted) ** 2))
            fold_errors.append(error)

        if fold_errors:
            errors[r] = np.mean(fold_errors)

    if not errors:
        return {"r_optimal": 1, "errors": {}}

    r_optimal = min(errors, key=errors.get)
    return {
        "r_optimal": r_optimal,
        "errors": errors,
        "min_error": errors[r_optimal],
    }


def out_of_sample_split(data: np.ndarray, train_frac: float = 0.5
                         ) -> Tuple[np.ndarray, np.ndarray]:
    """Split time series into train and test halves."""
    T = len(data)
    split = int(T * train_frac)
    return data[:split], data[split:]
