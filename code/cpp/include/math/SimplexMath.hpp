// Copyright Saxon Nicholls 2026 MIT Licence
#pragma once

#include <Eigen/Dense>
#include <Eigen/Eigenvalues>
#include <random>
#include <vector>
#include <functional>
#include <optional>
#include <stdexcept>
#include <cmath>

namespace up::math {

// Simplex projection (Duchi et al. 2008, O(d log d))
[[nodiscard]] Eigen::VectorXd projectOntoSimplex(const Eigen::VectorXd& v);
[[nodiscard]] Eigen::VectorXd projectOntoSimplexBounded(
    const Eigen::VectorXd& v, double lo = 0.0, double hi = 1.0);

// Wealth: S_T(b) = Π_t b·x_t
[[nodiscard]] double wealth(const Eigen::VectorXd& b, const Eigen::MatrixXd& priceRelatives);
[[nodiscard]] double logWealth(const Eigen::VectorXd& b, const Eigen::MatrixXd& priceRelatives);
[[nodiscard]] double logGrowthRate(const Eigen::VectorXd& b, const Eigen::MatrixXd& priceRelatives);
[[nodiscard]] Eigen::VectorXd gradLogGrowth(const Eigen::VectorXd& b, const Eigen::MatrixXd& priceRelatives);
[[nodiscard]] Eigen::MatrixXd hessianLogGrowth(const Eigen::VectorXd& b, const Eigen::MatrixXd& priceRelatives);

// Log-optimal: b* = argmax_{b∈Δ} L_T(b)
struct LogOptimalResult {
    Eigen::VectorXd bStar;
    double          logGrowth;
    double          gradNorm;
    int             iterations;
    bool            converged;
};

LogOptimalResult solveLogOptimal(
    const Eigen::MatrixXd& priceRelatives,
    int maxIter = 1000, double tol = 1e-10, double initStep = 1.0,
    std::optional<Eigen::VectorXd> warmStart = std::nullopt);

// Fisher information: F(b) = (1/T) Σ_t x_t x_t^T / (b·x_t)²
[[nodiscard]] Eigen::MatrixXd fisherInformation(const Eigen::VectorXd& b, const Eigen::MatrixXd& priceRelatives);
[[nodiscard]] double stableRank(const Eigen::MatrixXd& F);
[[nodiscard]] double effectiveRankEntropy(const Eigen::MatrixXd& F);
[[nodiscard]] double conditionNumber(const Eigen::MatrixXd& F);
[[nodiscard]] Eigen::MatrixXd regularisedFisherInverse(const Eigen::MatrixXd& F, double lambda = 1e-8);

// Laplace approximation
struct LaplaceApproximation {
    Eigen::VectorXd posteriorMean;
    Eigen::VectorXd posteriorStdDev;
    Eigen::MatrixXd posteriorCovariance;
    double          logMarginalLikelihood;
    double          effectiveRank;
    double          errorBound;
};

LaplaceApproximation computeLaplaceApproximation(
    const LogOptimalResult& logOpt, const Eigen::MatrixXd& F,
    std::size_t T, double regularisation = 1e-8);

// Exponentiated Gradient (Cover 1991)
[[nodiscard]] Eigen::VectorXd egUpdate(const Eigen::VectorXd& b, const Eigen::VectorXd& x, double eta);
[[nodiscard]] Eigen::VectorXd egOnline(const Eigen::MatrixXd& priceRelatives, double eta = 1.0);

// Factor model (PCA)
struct FactorModel {
    Eigen::MatrixXd loadings;
    Eigen::VectorXd explainedVar;
    int             numFactors;
    double          totalExplained;
};

FactorModel fitFactorModel(const Eigen::MatrixXd& priceRelatives, int numFactors, double varianceThreshold = 0.0);

// Simplex sampling
[[nodiscard]] Eigen::VectorXd sampleSimplex(int d, std::mt19937_64& rng);
[[nodiscard]] Eigen::VectorXd haltonSimplex(int d, std::size_t idx);
[[nodiscard]] Eigen::MatrixXd sampleSimplexBatch(int d, int N, std::mt19937_64& rng);
[[nodiscard]] Eigen::MatrixXd haltonSimplexBatch(int d, int N);
[[nodiscard]] double halton(std::size_t index, int base);

// Portfolio metrics
[[nodiscard]] double sharpeRatio(const std::vector<double>& logReturns, double riskFreeRate = 0.0, double barsPerYear = 252.0);
[[nodiscard]] double maxDrawdown(const std::vector<double>& cumulativeWealth);
[[nodiscard]] double calmarRatio(const std::vector<double>& logReturns, double barsPerYear = 252.0);
[[nodiscard]] double turnover(const Eigen::VectorXd& bNew, const Eigen::VectorXd& bOld);

// Utility
[[nodiscard]] double logSumExp(const Eigen::VectorXd& v);
[[nodiscard]] bool isInSimplex(const Eigen::VectorXd& v, double tol = 1e-8);
[[nodiscard]] double l1Distance(const Eigen::VectorXd& a, const Eigen::VectorXd& b);
[[nodiscard]] double lInfDistance(const Eigen::VectorXd& a, const Eigen::VectorXd& b);

} // namespace up::math
