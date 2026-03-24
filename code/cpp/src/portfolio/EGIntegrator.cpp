// Copyright Saxon Nicholls 2026 MIT Licence
#include "portfolio/EGIntegrator.hpp"
#include "interfaces/IntegrationMethodInterface.hpp"
#include "portfolio/LaplaceIntegrator.hpp"
#include "portfolio/MonteCarloIntegrator.hpp"
#include "portfolio/FactorProjectedIntegrator.hpp"
#include <chrono>
#include <cmath>
#include <stdexcept>

namespace up {

using namespace math;

SimplexIntegralResult EGIntegrator::integrate(
    const Eigen::MatrixXd& X, const IntegrationConfig& cfg) const
{
    const auto t0 = std::chrono::high_resolution_clock::now();
    const int T = static_cast<int>(X.rows());
    const int d = static_cast<int>(X.cols());
    const double eta = cfg.egLearningRate > 0.0 ? cfg.egLearningRate : eta_;

    Eigen::VectorXd b = Eigen::VectorXd::Ones(d) / d;
    for (int t = 0; t < T; ++t)
        b = egUpdate(b, X.row(t).transpose(), eta);

    const auto t1 = std::chrono::high_resolution_clock::now();
    SimplexIntegralResult r;
    r.posteriorMean         = b;
    r.posteriorVariance     = Eigen::VectorXd::Zero(d);
    r.logNormalisationConst = logWealth(b, X);
    r.effectiveRank         = static_cast<double>(d);
    r.estimatedError        = std::sqrt(std::log(static_cast<double>(d)) / static_cast<double>(T));
    r.convergenceDiag       = 0.0;
    r.elapsed               = t1 - t0;
    r.method                = name();
    r.numEvaluations        = static_cast<std::size_t>(T);
    return r;
}

SimplexIntegralResult EGIntegrator::incrementalUpdate(
    const SimplexIntegralResult& prev, const Eigen::VectorXd& newBar,
    const Eigen::MatrixXd&, const IntegrationConfig& cfg) const
{
    const auto t0 = std::chrono::high_resolution_clock::now();
    const double eta = cfg.egLearningRate > 0.0 ? cfg.egLearningRate : eta_;
    const Eigen::VectorXd bNew = egUpdate(prev.posteriorMean, newBar, eta);
    const auto t1 = std::chrono::high_resolution_clock::now();

    SimplexIntegralResult r = prev;
    r.posteriorMean = bNew;
    r.elapsed       = t1 - t0;
    r.numEvaluations = 1;
    return r;
}

// Factory implementations
IntegrationConfig IntegrationConfig::fromJson(const nlohmann::json& j) {
    IntegrationConfig cfg;
    if (j.contains("maxIterations"))      cfg.maxIterations      = j["maxIterations"];
    if (j.contains("convergenceTol"))     cfg.convergenceTol     = j["convergenceTol"];
    if (j.contains("initialStepSize"))    cfg.initialStepSize    = j["initialStepSize"];
    if (j.contains("regularisation"))     cfg.regularisation     = j["regularisation"];
    if (j.contains("applyFisherCorrection")) cfg.applyFisherCorrection = j["applyFisherCorrection"];
    if (j.contains("mcSamples"))          cfg.mcSamples          = j["mcSamples"];
    if (j.contains("useQuasiRandom"))     cfg.useQuasiRandom     = j["useQuasiRandom"];
    if (j.contains("randomSeed"))         cfg.randomSeed         = j["randomSeed"];
    if (j.contains("numFactors"))         cfg.numFactors         = j["numFactors"];
    if (j.contains("varianceThreshold"))  cfg.varianceThreshold  = j["varianceThreshold"];
    if (j.contains("autoSelectFactors"))  cfg.autoSelectFactors  = j["autoSelectFactors"];
    if (j.contains("egLearningRate"))     cfg.egLearningRate     = j["egLearningRate"];
    if (j.contains("accuracyLevel"))      cfg.accuracyLevel      = j["accuracyLevel"];
    return cfg;
}

nlohmann::json IntegrationConfig::toJson() const {
    return {
        {"maxIterations", maxIterations}, {"convergenceTol", convergenceTol},
        {"initialStepSize", initialStepSize}, {"regularisation", regularisation},
        {"applyFisherCorrection", applyFisherCorrection},
        {"mcSamples", mcSamples}, {"useQuasiRandom", useQuasiRandom},
        {"randomSeed", randomSeed}, {"numFactors", numFactors},
        {"varianceThreshold", varianceThreshold}, {"autoSelectFactors", autoSelectFactors},
        {"egLearningRate", egLearningRate}, {"accuracyLevel", accuracyLevel}
    };
}

IntegrationMethodPtr makeIntegrationMethod(IntegrationMethodType type) {
    switch (type) {
        case IntegrationMethodType::Laplace:         return std::make_shared<LaplaceIntegrator>();
        case IntegrationMethodType::MonteCarlo:      return std::make_shared<MonteCarloIntegrator>(false);
        case IntegrationMethodType::QuasiMonteCarlo: return std::make_shared<MonteCarloIntegrator>(true);
        case IntegrationMethodType::FactorProjected: return std::make_shared<FactorProjectedIntegrator>();
        case IntegrationMethodType::ExponentialGrad: return std::make_shared<EGIntegrator>();
        case IntegrationMethodType::GridExact:
            throw std::runtime_error("GridExact only available for d <= 5");
        default: throw std::invalid_argument("Unknown integration method type");
    }
}

IntegrationMethodPtr makeIntegrationMethodFromJson(const nlohmann::json& cfg) {
    const std::string method = cfg.value("method", "laplace");
    if (method == "laplace")    return makeIntegrationMethod(IntegrationMethodType::Laplace);
    if (method == "montecarlo") return makeIntegrationMethod(IntegrationMethodType::MonteCarlo);
    if (method == "qmc")        return makeIntegrationMethod(IntegrationMethodType::QuasiMonteCarlo);
    if (method == "factor")     return makeIntegrationMethod(IntegrationMethodType::FactorProjected);
    if (method == "eg")         return makeIntegrationMethod(IntegrationMethodType::ExponentialGrad);
    throw std::invalid_argument("Unknown method: " + method);
}

} // namespace up
