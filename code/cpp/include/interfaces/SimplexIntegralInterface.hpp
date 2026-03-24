// Copyright Saxon Nicholls 2026 MIT Licence
#pragma once

#include <Eigen/Dense>
#include <chrono>
#include <functional>
#include <string>
#include <vector>
#include <nlohmann/json.hpp>

namespace up {

struct SimplexIntegralResult {
    Eigen::VectorXd posteriorMean;
    Eigen::VectorXd posteriorVariance;
    double          logNormalisationConst;
    double          effectiveRank;
    double          estimatedError;
    double          convergenceDiag;
    std::chrono::nanoseconds elapsed;
    std::string     method;
    std::size_t     numEvaluations;
};

class ISimplexIntegral {
public:
    virtual ~ISimplexIntegral() = default;
    [[nodiscard]] virtual SimplexIntegralResult
    computeWeights(const Eigen::MatrixXd& priceRelatives) = 0;
    [[nodiscard]] virtual double
    computeExpectation(const Eigen::MatrixXd& priceRelatives,
                       std::function<double(const Eigen::VectorXd& b)> g) = 0;
    [[nodiscard]] virtual double
    computeLogWealth(const Eigen::MatrixXd& priceRelatives) = 0;
    virtual void update(const Eigen::VectorXd& priceRelative) = 0;
    [[nodiscard]] virtual SimplexIntegralResult getLastResult() const = 0;
    virtual void reset() = 0;
    virtual void configure(const nlohmann::json& cfg) = 0;
    [[nodiscard]] virtual std::string methodName() const = 0;
    [[nodiscard]] virtual nlohmann::json serialiseConfig() const = 0;
    virtual void setAccuracyLevel(double level) = 0;
    [[nodiscard]] virtual int estimateEffectiveDimension() const = 0;
};

using SimplexIntegralPtr = std::shared_ptr<ISimplexIntegral>;

} // namespace up
