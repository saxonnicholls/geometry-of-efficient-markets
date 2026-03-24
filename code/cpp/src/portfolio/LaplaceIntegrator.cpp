// Copyright Saxon Nicholls 2026 MIT Licence
#include "portfolio/LaplaceIntegrator.hpp"
#include <chrono>
#include <stdexcept>

namespace up {

using namespace math;

SimplexIntegralResult LaplaceIntegrator::integrate(
    const Eigen::MatrixXd& X, const IntegrationConfig& cfg) const
{
    const auto t0 = std::chrono::high_resolution_clock::now();
    const int T = static_cast<int>(X.rows());
    const int d = static_cast<int>(X.cols());
    if (T == 0 || d == 0)
        throw std::invalid_argument("LaplaceIntegrator: empty history");

    // Step 1: b* = argmax L_T(b)
    const auto logOpt = solveLogOptimal(X, cfg.maxIterations, cfg.convergenceTol,
                                         cfg.initialStepSize, std::nullopt);

    // Step 2: Fisher information at b*
    const Eigen::MatrixXd F = fisherInformation(logOpt.bStar, X);

    // Step 3: Laplace approximation for posterior mean
    const auto laplace = computeLaplaceApproximation(
        logOpt, F, static_cast<std::size_t>(T), cfg.regularisation);

    const auto t1 = std::chrono::high_resolution_clock::now();
    return buildResult(logOpt, laplace, T, t1 - t0);
}

SimplexIntegralResult LaplaceIntegrator::incrementalUpdate(
    const SimplexIntegralResult& prev, const Eigen::VectorXd&,
    const Eigen::MatrixXd& X, const IntegrationConfig& cfg) const
{
    const auto t0 = std::chrono::high_resolution_clock::now();
    const int T = static_cast<int>(X.rows());

    // Warm-started solve (typically 2-5 iterations)
    const auto logOpt = solveLogOptimal(X, cfg.maxIterations, cfg.convergenceTol,
                                         cfg.initialStepSize, prev.posteriorMean);
    const Eigen::MatrixXd F = fisherInformation(logOpt.bStar, X);
    const auto laplace = computeLaplaceApproximation(logOpt, F, T, cfg.regularisation);

    const auto t1 = std::chrono::high_resolution_clock::now();
    return buildResult(logOpt, laplace, T, t1 - t0);
}

SimplexIntegralResult LaplaceIntegrator::buildResult(
    const math::LogOptimalResult& logOpt, const math::LaplaceApproximation& lap,
    std::size_t T, std::chrono::nanoseconds elapsed)
{
    SimplexIntegralResult r;
    r.posteriorMean         = lap.posteriorMean;
    r.posteriorVariance     = lap.posteriorStdDev.array().square().matrix();
    r.logNormalisationConst = lap.logMarginalLikelihood;
    r.effectiveRank         = lap.effectiveRank;
    r.estimatedError        = lap.errorBound;
    r.convergenceDiag       = logOpt.gradNorm;
    r.elapsed               = elapsed;
    r.method                = "Laplace";
    r.numEvaluations        = static_cast<std::size_t>(logOpt.iterations) * T;
    return r;
}

} // namespace up
