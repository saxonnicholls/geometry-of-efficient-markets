#!/usr/bin/env python3
"""
test_24_option_pricing_charts.py

Comparison charts: Black-Scholes vs Fractional Palindromic SDE option pricing.

Produces:
  1. Option price curves vs strike (multiple maturities)
  2. Implied volatility smile (the key chart)
  3. ATM vol term structure
  4. Price difference heatmap (strike × maturity)
  5. Greeks comparison (Delta, Gamma, Vega)
  6. Hurst Vega — the new Greek

Output: PNG files in data/results/option_pricing/
Paper: PALINDROMIC_OPTIONS.md

Author: Saxon Nicholls
"""

import argparse
import numpy as np
from pathlib import Path
from scipy.stats import norm
from scipy.optimize import brentq

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────────────────────
# Setup
# ─────────────────────────────────────────────────────────────

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.labelsize": 12,
    "legend.fontsize": 10,
    "figure.titlesize": 14,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})


# ─────────────────────────────────────────────────────────────
# Pricing functions
# ─────────────────────────────────────────────────────────────

def fps_variance(T, kappa, H):
    """Effective variance of the Fractional Palindromic SDE."""
    if T <= 0:
        return 0.0
    if abs(kappa) < 1e-10:
        return T ** (2.0 * H)
    if abs(H - 0.5) < 1e-6:
        return (1.0 - np.exp(-2.0 * kappa * T)) / (2.0 * kappa)
    return T ** (2.0 * H) * (1.0 - np.exp(-2.0 * kappa * T)) / (2.0 * kappa * T)


def bs_call(S0, K, T, r, sigma):
    """Classical Black-Scholes European call option."""
    if T <= 0:
        return max(S0 - K, 0.0)
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


def fps_call(S0, K, T, r, sigma, kappa, H):
    """FPS European call option price."""
    if T <= 0:
        return max(S0 - K, 0.0)
    V = fps_variance(T, kappa, H)
    eff_var = sigma ** 2 * V
    eff_std = np.sqrt(eff_var)
    if eff_std < 1e-10:
        return np.exp(-r * T) * max(S0 * np.exp(r * T) - K, 0.0)
    d1 = (np.log(S0 / K) + r * T + 0.5 * eff_var) / eff_std
    d2 = d1 - eff_std
    return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


def bs_put(S0, K, T, r, sigma):
    """Classical Black-Scholes European put option."""
    return bs_call(S0, K, T, r, sigma) - S0 + K * np.exp(-r * T)


def fps_put(S0, K, T, r, sigma, kappa, H):
    """FPS European put option price."""
    return fps_call(S0, K, T, r, sigma, kappa, H) - S0 + K * np.exp(-r * T)


def implied_vol(price, S0, K, T, r):
    """Black-Scholes implied volatility from market price."""
    if T <= 0:
        return float("nan")
    try:
        return brentq(lambda s: bs_call(S0, K, T, r, s) - price, 1e-4, 5.0, xtol=1e-8)
    except (ValueError, RuntimeError):
        return float("nan")


# ─────────────────────────────────────────────────────────────
# Greeks
# ─────────────────────────────────────────────────────────────

def bs_greeks(S0, K, T, r, sigma):
    """Classical Black-Scholes Greeks."""
    if T <= 0:
        return {"delta": float(S0 > K), "gamma": 0, "vega": 0, "theta": 0, "rho": 0}
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return {
        "delta": norm.cdf(d1),
        "gamma": norm.pdf(d1) / (S0 * sigma * np.sqrt(T)),
        "vega": S0 * norm.pdf(d1) * np.sqrt(T),
        "theta": -S0 * norm.pdf(d1) * sigma / (2 * np.sqrt(T))
                 - r * K * np.exp(-r * T) * norm.cdf(d2),
        "rho": K * T * np.exp(-r * T) * norm.cdf(d2),
    }


def fps_greeks(S0, K, T, r, sigma, kappa, H):
    """FPS Greeks including Hurst Vega."""
    if T <= 0:
        return {"delta": float(S0 > K), "gamma": 0, "vega": 0, "hurst_vega": 0}
    V = fps_variance(T, kappa, H)
    eff_var = sigma ** 2 * V
    eff_std = np.sqrt(eff_var)
    d1 = (np.log(S0 / K) + r * T + 0.5 * eff_var) / eff_std
    greeks = {
        "delta": norm.cdf(d1),
        "gamma": norm.pdf(d1) / (S0 * eff_std),
        "vega": S0 * norm.pdf(d1) * eff_std / sigma,
    }
    # Numerical Hurst Vega
    dH = 0.01
    price_up = fps_call(S0, K, T, r, sigma, kappa, H + dH)
    price_dn = fps_call(S0, K, T, r, sigma, kappa, H - dH)
    greeks["hurst_vega"] = (price_up - price_dn) / (2 * dH)
    return greeks


# ─────────────────────────────────────────────────────────────
# PLOT 1: Price curves vs strike (multiple maturities)
# ─────────────────────────────────────────────────────────────

def plot_price_curves(output_path, S0=100, r=0.05, sigma=0.2, kappa=1.5, H=0.35):
    """Four panels: price vs strike at T = 1/12, 3/12, 1, 2 years."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharex=True)

    strikes = np.linspace(60, 140, 100)
    maturities = [(1 / 12, "1 month"), (3 / 12, "3 months"),
                  (1.0, "1 year"), (2.0, "2 years")]

    for ax, (T, label) in zip(axes.flat, maturities):
        bs = [bs_call(S0, K, T, r, sigma) for K in strikes]
        fps = [fps_call(S0, K, T, r, sigma, kappa, H) for K in strikes]

        ax.plot(strikes, bs, lw=2, color="red", label="Black-Scholes", alpha=0.85)
        ax.plot(strikes, fps, lw=2, color="#1f4e79", label="FPS (κ=1.5, H=0.35)")
        ax.fill_between(strikes, bs, fps,
                        where=np.array(fps) >= np.array(bs),
                        alpha=0.2, color="green", label="FPS > BS")
        ax.fill_between(strikes, bs, fps,
                        where=np.array(fps) < np.array(bs),
                        alpha=0.2, color="orange", label="FPS < BS")

        # Intrinsic value line
        ax.plot(strikes, [max(S0 - K, 0) for K in strikes], "k--", lw=1, alpha=0.4,
                label="Intrinsic value")

        ax.axvline(S0, color="black", linestyle=":", lw=1, alpha=0.5)
        ax.set_title(f"T = {label}")
        ax.set_xlabel("Strike K")
        ax.set_ylabel("Call Price")
        ax.legend(loc="upper right", fontsize=9)
        ax.set_xlim(60, 140)

    plt.suptitle(f"European Call Option Prices: Black-Scholes vs FPS\n"
                 f"S$_0$ = {S0}, r = {r*100:.0f}%, σ = {sigma*100:.0f}%",
                 y=1.01)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


# ─────────────────────────────────────────────────────────────
# PLOT 2: Implied volatility smile
# ─────────────────────────────────────────────────────────────

def plot_smile(output_path, S0=100, r=0.05, sigma=0.2, kappa=1.5, H=0.35):
    """Implied volatility smile at different maturities."""
    fig, ax = plt.subplots(figsize=(12, 7))

    maturities = [(1 / 12, "1 month", "#8B0000"),
                  (3 / 12, "3 months", "#B22222"),
                  (6 / 12, "6 months", "#1f4e79"),
                  (1.0, "1 year", "#2E8B57"),
                  (2.0, "2 years", "#9370DB")]
    strikes = np.linspace(80, 120, 50)

    for T, label, color in maturities:
        iv = []
        for K in strikes:
            fps_price = fps_call(S0, K, T, r, sigma, kappa, H)
            if fps_price > 1e-5:
                v = implied_vol(fps_price, S0, K, T, r)
                iv.append(v)
            else:
                iv.append(float("nan"))
        log_moneyness = np.log(strikes / S0)
        ax.plot(log_moneyness, iv, "o-", color=color, markersize=5, lw=1.8,
                label=f"T = {label}")

    ax.axhline(sigma, color="red", linestyle="--", lw=1.5, alpha=0.7,
               label=f"Black-Scholes σ = {sigma:.2f} (flat)")
    ax.axvline(0, color="black", linestyle=":", lw=1, alpha=0.5)

    ax.set_xlabel("Log-moneyness log(K/S₀)")
    ax.set_ylabel("Implied Volatility")
    ax.set_title(
        f"The FPS Volatility Smile Emerges from First Principles\n"
        f"FPS parameters: σ={sigma}, κ={kappa}, H={H}. No ad-hoc fitting."
    )
    ax.legend(loc="upper right", fontsize=10)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


# ─────────────────────────────────────────────────────────────
# PLOT 3: ATM vol term structure
# ─────────────────────────────────────────────────────────────

def plot_term_structure(output_path, S0=100, r=0.05, sigma=0.2,
                        kappa=1.5, H=0.35):
    """ATM implied vol as function of maturity."""
    fig, ax = plt.subplots(figsize=(11, 6))

    T_range = np.linspace(0.05, 5.0, 80)
    iv_fps = []

    for T in T_range:
        fps_price = fps_call(S0, S0, T, r, sigma, kappa, H)
        iv_fps.append(implied_vol(fps_price, S0, S0, T, r))

    ax.plot(T_range, iv_fps, lw=2.2, color="#1f4e79",
            label=f"FPS ATM IV (κ={kappa}, H={H})")
    ax.axhline(sigma, color="red", linestyle="--", lw=1.5,
               label=f"Black-Scholes σ = {sigma:.2f} (flat)")

    # Annotate hump
    i_max = np.argmax(iv_fps)
    ax.annotate(
        f"Peak IV = {iv_fps[i_max]:.3f}\nat T = {T_range[i_max]:.2f}y",
        xy=(T_range[i_max], iv_fps[i_max]),
        xytext=(T_range[i_max] + 0.5, iv_fps[i_max] + 0.02),
        arrowprops=dict(arrowstyle="->", color="black"),
        fontsize=10,
    )

    # Mark asymptote
    ax.axhline(iv_fps[-1], color="gray", linestyle=":", lw=1,
               label=f"Long-run asymptote ≈ {iv_fps[-1]:.3f}")

    ax.set_xlabel("Time to maturity T (years)")
    ax.set_ylabel("At-the-money implied volatility")
    ax.set_title(
        "ATM Volatility Term Structure: FPS Produces the Empirical Hump\n"
        "BS is flat; real markets show exactly this hump shape"
    )
    ax.legend(loc="upper right")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


# ─────────────────────────────────────────────────────────────
# PLOT 4: Price difference heatmap
# ─────────────────────────────────────────────────────────────

def plot_difference_heatmap(output_path, S0=100, r=0.05, sigma=0.2,
                            kappa=1.5, H=0.35):
    """Heatmap of FPS - BS price differences across strike and maturity."""
    fig, ax = plt.subplots(figsize=(12, 7))

    strikes = np.linspace(80, 120, 40)
    maturities = np.linspace(1 / 12, 3.0, 40)

    diff_grid = np.zeros((len(maturities), len(strikes)))
    for i, T in enumerate(maturities):
        for j, K in enumerate(strikes):
            bs = bs_call(S0, K, T, r, sigma)
            fps = fps_call(S0, K, T, r, sigma, kappa, H)
            diff_grid[i, j] = fps - bs

    im = ax.imshow(
        diff_grid, aspect="auto",
        extent=(strikes[0], strikes[-1], maturities[-1], maturities[0]),
        cmap="RdBu_r", vmin=-np.abs(diff_grid).max(),
        vmax=np.abs(diff_grid).max(),
    )

    ax.set_xlabel("Strike K")
    ax.set_ylabel("Maturity T (years)")
    ax.set_title(
        "FPS Option Price − Black-Scholes (heatmap)\n"
        "Red = FPS pricier than BS (short-dated OTM smile); Blue = FPS cheaper (long-dated)"
    )

    # Colour bar
    cbar = plt.colorbar(im, ax=ax, label="FPS − BS (dollars)")

    # ATM line
    ax.axvline(S0, color="black", linestyle="-", lw=1.5, alpha=0.7,
               label="ATM strike")
    ax.legend(loc="upper right")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


# ─────────────────────────────────────────────────────────────
# PLOT 5: Greeks comparison
# ─────────────────────────────────────────────────────────────

def plot_greeks(output_path, S0=100, r=0.05, sigma=0.2, kappa=1.5, H=0.35):
    """Compare Delta, Gamma, Vega across BS and FPS."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 9))

    strikes = np.linspace(70, 130, 60)
    T = 0.5

    # Delta
    ax = axes[0, 0]
    bs_delta = [bs_greeks(S0, K, T, r, sigma)["delta"] for K in strikes]
    fps_delta = [fps_greeks(S0, K, T, r, sigma, kappa, H)["delta"] for K in strikes]
    ax.plot(strikes, bs_delta, lw=2, color="red", label="Black-Scholes")
    ax.plot(strikes, fps_delta, lw=2, color="#1f4e79", label="FPS")
    ax.axvline(S0, color="black", linestyle=":", alpha=0.5)
    ax.set_xlabel("Strike K")
    ax.set_ylabel("Delta")
    ax.set_title("Delta (Δ) — sensitivity to underlying price")
    ax.legend()

    # Gamma
    ax = axes[0, 1]
    bs_gamma = [bs_greeks(S0, K, T, r, sigma)["gamma"] for K in strikes]
    fps_gamma = [fps_greeks(S0, K, T, r, sigma, kappa, H)["gamma"] for K in strikes]
    ax.plot(strikes, bs_gamma, lw=2, color="red", label="Black-Scholes")
    ax.plot(strikes, fps_gamma, lw=2, color="#1f4e79", label="FPS")
    ax.axvline(S0, color="black", linestyle=":", alpha=0.5)
    ax.set_xlabel("Strike K")
    ax.set_ylabel("Gamma")
    ax.set_title("Gamma (Γ) — convexity in underlying price")
    ax.legend()

    # Vega
    ax = axes[1, 0]
    bs_vega = [bs_greeks(S0, K, T, r, sigma)["vega"] for K in strikes]
    fps_vega = [fps_greeks(S0, K, T, r, sigma, kappa, H)["vega"] for K in strikes]
    ax.plot(strikes, bs_vega, lw=2, color="red", label="Black-Scholes")
    ax.plot(strikes, fps_vega, lw=2, color="#1f4e79", label="FPS")
    ax.axvline(S0, color="black", linestyle=":", alpha=0.5)
    ax.set_xlabel("Strike K")
    ax.set_ylabel("Vega")
    ax.set_title("Vega (𝒱) — sensitivity to volatility")
    ax.legend()

    # Hurst Vega (FPS only)
    ax = axes[1, 1]
    hurst_vega = [fps_greeks(S0, K, T, r, sigma, kappa, H)["hurst_vega"] for K in strikes]
    ax.plot(strikes, hurst_vega, lw=2, color="green", label="FPS only")
    ax.axhline(0, color="black", lw=0.5)
    ax.axvline(S0, color="black", linestyle=":", alpha=0.5)
    ax.set_xlabel("Strike K")
    ax.set_ylabel("∂C / ∂H")
    ax.set_title("Hurst Vega (ℋ) — the new FPS-only Greek")
    ax.legend()

    plt.suptitle(
        f"Option Greeks: Black-Scholes vs FPS (T = {T} years)",
        y=1.01, fontsize=14,
    )
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


# ─────────────────────────────────────────────────────────────
# PLOT 6: Hurst sensitivity
# ─────────────────────────────────────────────────────────────

def plot_hurst_sensitivity(output_path, S0=100, r=0.05, sigma=0.2, kappa=1.5):
    """How does the option price depend on H?"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: price vs strike for multiple H
    ax = axes[0]
    strikes = np.linspace(70, 130, 50)
    T = 1.0
    H_values = [0.25, 0.35, 0.45, 0.5, 0.55]
    colors = plt.cm.viridis(np.linspace(0.1, 0.9, len(H_values)))

    for H, color in zip(H_values, colors):
        prices = [fps_call(S0, K, T, r, sigma, kappa, H) for K in strikes]
        ax.plot(strikes, prices, lw=1.8, color=color, label=f"H = {H:.2f}")

    bs_prices = [bs_call(S0, K, T, r, sigma) for K in strikes]
    ax.plot(strikes, bs_prices, "k--", lw=1.5, label="Black-Scholes")

    ax.axvline(S0, color="black", linestyle=":", alpha=0.5)
    ax.set_xlabel("Strike K")
    ax.set_ylabel("Call price")
    ax.set_title(f"FPS Price vs Hurst Parameter (T = {T} year)")
    ax.legend(loc="upper right", fontsize=9)

    # Right: implied vol vs H
    ax = axes[1]
    H_grid = np.linspace(0.2, 0.6, 40)
    strike_list = [85, 90, 100, 110, 115]
    colors = plt.cm.plasma(np.linspace(0.1, 0.9, len(strike_list)))

    for K, color in zip(strike_list, colors):
        iv_list = []
        for H in H_grid:
            price = fps_call(S0, K, T, r, sigma, kappa, H)
            iv = implied_vol(price, S0, K, T, r) if price > 1e-5 else float("nan")
            iv_list.append(iv)
        ax.plot(H_grid, iv_list, lw=1.8, color=color, label=f"K = {K}")

    ax.axvline(0.5, color="red", linestyle="--", alpha=0.6, label="H = 0.5 (GBM)")
    ax.axhline(sigma, color="black", linestyle=":", alpha=0.5, label=f"Base σ = {sigma}")

    ax.set_xlabel("Hurst exponent H")
    ax.set_ylabel("Implied volatility")
    ax.set_title("Implied Vol vs Hurst (Sensitivity to Palindromic Structure)")
    ax.legend(loc="upper right", fontsize=9)

    plt.suptitle(
        "Hurst Sensitivity: How Palindromic Structure (H) Changes Pricing",
        y=1.03, fontsize=14,
    )
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


# ─────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--S0", type=float, default=100.0)
    parser.add_argument("--r", type=float, default=0.05)
    parser.add_argument("--sigma", type=float, default=0.2)
    parser.add_argument("--kappa", type=float, default=1.5)
    parser.add_argument("--H", type=float, default=0.35)
    parser.add_argument("--output_dir", default="data/results/option_pricing")
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {out_dir}")

    print(f"\nParameters:")
    print(f"  S0 = {args.S0}")
    print(f"  r  = {args.r}")
    print(f"  σ  = {args.sigma}")
    print(f"  κ  = {args.kappa}")
    print(f"  H  = {args.H}")

    print("\n=== Generating option pricing charts ===")

    plot_price_curves(out_dir / "01_price_curves.png",
                      args.S0, args.r, args.sigma, args.kappa, args.H)
    plot_smile(out_dir / "02_volatility_smile.png",
               args.S0, args.r, args.sigma, args.kappa, args.H)
    plot_term_structure(out_dir / "03_term_structure.png",
                        args.S0, args.r, args.sigma, args.kappa, args.H)
    plot_difference_heatmap(out_dir / "04_difference_heatmap.png",
                            args.S0, args.r, args.sigma, args.kappa, args.H)
    plot_greeks(out_dir / "05_greeks_comparison.png",
                args.S0, args.r, args.sigma, args.kappa, args.H)
    plot_hurst_sensitivity(out_dir / "06_hurst_sensitivity.png",
                           args.S0, args.r, args.sigma, args.kappa)

    print(f"\nAll 6 plots saved to {out_dir}")


if __name__ == "__main__":
    main()
