// Copyright Saxon Nicholls 2026 MIT Licence
#pragma once

#include <Eigen/Dense>
#include <chrono>
#include <string>
#include <memory>
#include <nlohmann/json.hpp>
#include "SimplexIntegralInterface.hpp"

namespace up {

struct IntegrationConfig {
    int    maxIterations     = 500;
    double convergenceTol    = 1e-9;
    double initialStepSize   = 1.0;
    double regularisation    = 1e-8;
    bool   applyFisherCorrection = true;
    bool   constrainToInterior   = true;
    int    mcSamples         = 10'000;
    int    mcBurnIn          = 0;
    bool   useQuasiRandom    = false;
    int    randomSeed        = 42;
    int    numFactors        = 5;
    double varianceThreshold = 0.90;
    bool   autoSelectFactors = true;
    double egLearningRate    = 1.0;
    double accuracyLevel     = 1.0;

    static IntegrationConfig fromJson(const nlohmann::json& j);
    [[nodiscard]] nlohmann::json toJson() const;
};

class IIntegrationMethod {
public:
    virtual ~IIntegrationMethod() = default;
    [[nodiscard]] virtual SimplexIntegralResult
    integrate(const Eigen::MatrixXd& history, const IntegrationConfig& cfg) const = 0;
    [[nodiscard]] virtual SimplexIntegralResult
    incrementalUpdate(const SimplexIntegralResult& prev, const Eigen::VectorXd& newBar,
                      const Eigen::MatrixXd& history, const IntegrationConfig& cfg) const = 0;
    [[nodiscard]] virtual std::string name() const = 0;
    [[nodiscard]] virtual std::string convergenceRate() const = 0;
    [[nodiscard]] virtual std::chrono::nanoseconds estimateCost(int numAssets, int numPeriods) const = 0;
};

using IntegrationMethodPtr = std::shared_ptr<IIntegrationMethod>;

enum class IntegrationMethodType {
    Laplace, MonteCarlo, QuasiMonteCarlo, FactorProjected, ExponentialGrad, GridExact
};

IntegrationMethodPtr makeIntegrationMethod(IntegrationMethodType type);
IntegrationMethodPtr makeIntegrationMethodFromJson(const nlohmann::json& cfg);

} // namespace up
