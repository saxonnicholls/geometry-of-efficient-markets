// Copyright Saxon Nicholls 2026 MIT Licence
#include "math/SimplexMath.hpp"
#include <Eigen/SVD>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <numeric>
#include <stdexcept>

namespace up::math {

// ───────────────────────────────────────────────────────────
// Simplex projection (Duchi et al. 2008, O(d log d))
// ───────────────────────────────────────────────────────────

Eigen::VectorXd projectOntoSimplex(const Eigen::VectorXd& v) {
    const int n = static_cast<int>(v.size());
    assert(n > 0);
    Eigen::VectorXd u = v;
    std::sort(u.data(), u.data() + n, std::greater<double>());
    double cumSum = 0.0;
    int    rho    = 0;
    for (int i = 0; i < n; ++i) {
        cumSum += u[i];
        if (u[i] - (cumSum - 1.0) / (i + 1) > 0.0) rho = i;
    }
    const double theta = (u.head(rho + 1).sum() - 1.0) / (rho + 1);
    return (v.array() - theta).max(0.0).matrix();
}

Eigen::VectorXd projectOntoSimplexBounded(
    const Eigen::VectorXd& v, double lo, double hi)
{
    Eigen::VectorXd shifted = (v.array() - lo).matrix();
    const double scale = hi - lo;
    Eigen::VectorXd proj = projectOntoSimplex(shifted / scale);
    return (proj * scale).array() + lo;
}

// ───────────────────────────────────────────────────────────
// Wealth
// ───────────────────────────────────────────────────────────

double wealth(const Eigen::VectorXd& b, const Eigen::MatrixXd& X) {
    const int T = static_cast<int>(X.rows());
    double w = 1.0;
    for (int t = 0; t < T; ++t) w *= b.dot(X.row(t));
    return w;
}

double logWealth(const Eigen::VectorXd& b, const Eigen::MatrixXd& X) {
    const int T = static_cast<int>(X.rows());
    double lw = 0.0;
    for (int t = 0; t < T; ++t) {
        const double bx = b.dot(X.row(t));
        if (bx <= 0.0) return -std::numeric_limits<double>::infinity();
        lw += std::log(bx);
    }
    return lw;
}

double logGrowthRate(const Eigen::VectorXd& b, const Eigen::MatrixXd& X) {
    return logWealth(b, X) / static_cast<double>(X.rows());
}

Eigen::VectorXd gradLogGrowth(const Eigen::VectorXd& b, const Eigen::MatrixXd& X) {
    const int T = static_cast<int>(X.rows());
    const int d = static_cast<int>(X.cols());
    Eigen::VectorXd g = Eigen::VectorXd::Zero(d);
    for (int t = 0; t < T; ++t) {
        const double bx = b.dot(X.row(t));
        g += X.row(t).transpose() / bx;
    }
    return g / static_cast<double>(T);
}

Eigen::MatrixXd hessianLogGrowth(const Eigen::VectorXd& b, const Eigen::MatrixXd& X) {
    const int T = static_cast<int>(X.rows());
    const int d = static_cast<int>(X.cols());
    Eigen::MatrixXd H = Eigen::MatrixXd::Zero(d, d);
    for (int t = 0; t < T; ++t) {
        const double bx = b.dot(X.row(t));
        const Eigen::VectorXd xt = X.row(t).transpose();
        H -= xt * xt.transpose() / (bx * bx);
    }
    return H / static_cast<double>(T);
}

// ───────────────────────────────────────────────────────────
// Log-optimal solver (projected gradient ascent + Armijo)
// ───────────────────────────────────────────────────────────

LogOptimalResult solveLogOptimal(
    const Eigen::MatrixXd& X, int maxIter, double tol,
    double initStep, std::optional<Eigen::VectorXd> warmStart)
{
    const int d = static_cast<int>(X.cols());
    const int T = static_cast<int>(X.rows());
    if (T == 0 || d == 0)
        throw std::invalid_argument("solveLogOptimal: empty price relative matrix");

    Eigen::VectorXd b = warmStart.has_value()
        ? *warmStart : Eigen::VectorXd::Ones(d) / d;
    b = projectOntoSimplex(b);

    double lr  = initStep;
    double lgr = logGrowthRate(b, X);

    LogOptimalResult res;
    res.converged  = false;
    res.iterations = 0;

    const double alpha = 0.01, beta = 0.6, lrMax = 10.0;

    for (int it = 0; it < maxIter; ++it) {
        const Eigen::VectorXd g = gradLogGrowth(b, X);
        res.gradNorm = g.norm();
        if (res.gradNorm < tol) { res.converged = true; res.iterations = it; break; }

        int lineIter = 0;
        while (lineIter < 50) {
            const Eigen::VectorXd bNew = projectOntoSimplex(b + lr * g);
            const double lgrNew = logGrowthRate(bNew, X);
            const double expected = lgr + alpha * (bNew - b).dot(g) / lr;
            if (lgrNew >= expected) { b = bNew; lgr = lgrNew; lr = std::min(lr * 1.2, lrMax); break; }
            lr *= beta;
            ++lineIter;
        }
        res.iterations = it + 1;
        if (lr < 1e-15) { res.converged = true; break; }
    }

    res.bStar = b;
    res.logGrowth = lgr;
    return res;
}

// ───────────────────────────────────────────────────────────
// Fisher information: F(b) = (1/T) Σ_t x_t x_t^T / (b·x_t)²
// ───────────────────────────────────────────────────────────

Eigen::MatrixXd fisherInformation(
    const Eigen::VectorXd& b, const Eigen::MatrixXd& X)
{
    const int T = static_cast<int>(X.rows());
    const int d = static_cast<int>(X.cols());
    Eigen::MatrixXd F = Eigen::MatrixXd::Zero(d, d);
    for (int t = 0; t < T; ++t) {
        const double bx = b.dot(X.row(t));
        const Eigen::VectorXd xt = X.row(t).transpose();
        F += xt * xt.transpose() / (bx * bx);
    }
    return F / static_cast<double>(T);
}

double stableRank(const Eigen::MatrixXd& F) {
    const double frobSq = F.squaredNorm();
    const double specSq = F.operatorNorm() * F.operatorNorm();
    if (specSq < 1e-15) return 0.0;
    return frobSq / specSq;
}

double effectiveRankEntropy(const Eigen::MatrixXd& F) {
    Eigen::SelfAdjointEigenSolver<Eigen::MatrixXd> es(F);
    Eigen::VectorXd ev = es.eigenvalues().cwiseMax(0.0);
    const double total = ev.sum();
    if (total < 1e-15) return 0.0;
    const Eigen::VectorXd p = ev / total;
    double entropy = 0.0;
    for (int i = 0; i < p.size(); ++i)
        if (p[i] > 1e-15) entropy -= p[i] * std::log(p[i]);
    return std::exp(entropy);
}

double conditionNumber(const Eigen::MatrixXd& F) {
    Eigen::SelfAdjointEigenSolver<Eigen::MatrixXd> es(F);
    const Eigen::VectorXd ev = es.eigenvalues();
    const double lMin = ev.minCoeff(), lMax = ev.maxCoeff();
    if (std::abs(lMin) < 1e-15) return std::numeric_limits<double>::infinity();
    return lMax / lMin;
}

Eigen::MatrixXd regularisedFisherInverse(const Eigen::MatrixXd& F, double lambda) {
    const int d = static_cast<int>(F.rows());
    Eigen::MatrixXd Freg = F + lambda * Eigen::MatrixXd::Identity(d, d);
    return Freg.selfadjointView<Eigen::Upper>().llt().solve(Eigen::MatrixXd::Identity(d, d));
}

// ───────────────────────────────────────────────────────────
// Laplace approximation on the simplex
// ───────────────────────────────────────────────────────────

LaplaceApproximation computeLaplaceApproximation(
    const LogOptimalResult& logOpt, const Eigen::MatrixXd& F,
    std::size_t T, double regularisation)
{
    const int d = static_cast<int>(logOpt.bStar.size());
    const double Td = static_cast<double>(T);

    const Eigen::MatrixXd Finv = regularisedFisherInverse(F, regularisation);
    const Eigen::MatrixXd Sigma = Finv / Td;

    // For uniform prior, posterior mean = b* + O(1/T²)
    Eigen::VectorXd posteriorMean = projectOntoSimplex(logOpt.bStar);

    const double errorBound = Sigma.diagonal().sum() / Td;

    const Eigen::SelfAdjointEigenSolver<Eigen::MatrixXd> es(F);
    const Eigen::VectorXd ev = es.eigenvalues().cwiseMax(1e-15);
    const double logDetF = ev.array().log().sum();
    const double logMarginal = logOpt.logGrowth * Td
        + 0.5 * (d - 1) * std::log(2.0 * M_PI / Td) - 0.5 * logDetF;

    return LaplaceApproximation{
        .posteriorMean         = posteriorMean,
        .posteriorStdDev       = Sigma.diagonal().cwiseSqrt(),
        .posteriorCovariance   = Sigma,
        .logMarginalLikelihood = logMarginal,
        .effectiveRank         = stableRank(F),
        .errorBound            = errorBound
    };
}

// ───────────────────────────────────────────────────────────
// Exponentiated Gradient (Cover 1991)
// ───────────────────────────────────────────────────────────

Eigen::VectorXd egUpdate(const Eigen::VectorXd& b, const Eigen::VectorXd& x, double eta) {
    const double bx = b.dot(x);
    if (bx <= 0.0) return b;
    const Eigen::VectorXd bnew = b.array() * (eta * x.array() / bx).exp();
    const double s = bnew.sum();
    if (s <= 0.0) return b;
    return bnew / s;
}

Eigen::VectorXd egOnline(const Eigen::MatrixXd& X, double eta) {
    const int T = static_cast<int>(X.rows());
    const int d = static_cast<int>(X.cols());
    Eigen::VectorXd b = Eigen::VectorXd::Ones(d) / d;
    for (int t = 0; t < T; ++t) b = egUpdate(b, X.row(t).transpose(), eta);
    return b;
}

// ───────────────────────────────────────────────────────────
// Factor model (PCA on log-return covariance)
// ───────────────────────────────────────────────────────────

FactorModel fitFactorModel(
    const Eigen::MatrixXd& X, int numFactors, double varianceThreshold)
{
    const int T = static_cast<int>(X.rows());
    Eigen::MatrixXd logR(T, X.cols());
    for (int t = 0; t < T; ++t)
        logR.row(t) = X.row(t).array().max(1e-10).log().matrix();

    Eigen::VectorXd mu = logR.colwise().mean();
    Eigen::MatrixXd centred = logR.rowwise() - mu.transpose();

    Eigen::JacobiSVD<Eigen::MatrixXd> svd(
        centred / std::sqrt(static_cast<double>(T - 1)),
        Eigen::ComputeThinU | Eigen::ComputeThinV);

    const Eigen::VectorXd singVals = svd.singularValues();
    const Eigen::VectorXd eigVals  = singVals.array().square();
    const double totalVar = eigVals.sum();

    int r = numFactors;
    if (varianceThreshold > 0.0 && totalVar > 0.0) {
        r = 0;
        double cumVar = 0.0;
        for (int i = 0; i < singVals.size(); ++i) {
            cumVar += eigVals[i]; ++r;
            if (cumVar / totalVar >= varianceThreshold) break;
        }
    }
    r = std::min(r, static_cast<int>(singVals.size()));

    return FactorModel{
        .loadings       = svd.matrixV().leftCols(r),
        .explainedVar   = eigVals.head(r) / totalVar,
        .numFactors     = r,
        .totalExplained = eigVals.head(r).sum() / totalVar
    };
}

// ───────────────────────────────────────────────────────────
// Simplex sampling
// ───────────────────────────────────────────────────────────

Eigen::VectorXd sampleSimplex(int d, std::mt19937_64& rng) {
    std::exponential_distribution<double> expDist(1.0);
    Eigen::VectorXd z(d);
    for (int i = 0; i < d; ++i) z[i] = expDist(rng);
    return z / z.sum();
}

double halton(std::size_t index, int base) {
    double result = 0.0, f = 1.0;
    std::size_t i = index + 1;
    while (i > 0) { f /= base; result += f * static_cast<double>(i % base); i /= base; }
    return result;
}

Eigen::VectorXd haltonSimplex(int d, std::size_t idx) {
    static const int primes[] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71};
    Eigen::VectorXd u(d);
    for (int i = 0; i < d; ++i) u[i] = halton(idx, primes[i % 20]);
    Eigen::VectorXd z = -u.array().max(1e-15).log().matrix();
    return z / z.sum();
}

Eigen::MatrixXd sampleSimplexBatch(int d, int N, std::mt19937_64& rng) {
    Eigen::MatrixXd S(N, d);
    for (int i = 0; i < N; ++i) S.row(i) = sampleSimplex(d, rng).transpose();
    return S;
}

Eigen::MatrixXd haltonSimplexBatch(int d, int N) {
    Eigen::MatrixXd S(N, d);
    for (int i = 0; i < N; ++i) S.row(i) = haltonSimplex(d, i).transpose();
    return S;
}

// ───────────────────────────────────────────────────────────
// Portfolio metrics
// ───────────────────────────────────────────────────────────

double sharpeRatio(const std::vector<double>& logRets, double rfRate, double barsPerYear) {
    if (logRets.empty()) return 0.0;
    const int N = static_cast<int>(logRets.size());
    const double mean = std::accumulate(logRets.begin(), logRets.end(), 0.0) / N;
    double var = 0.0;
    for (double r : logRets) var += (r - mean) * (r - mean);
    var /= (N > 1 ? N - 1 : 1);
    const double vol = std::sqrt(var * barsPerYear);
    if (vol < 1e-12) return 0.0;
    return (mean * barsPerYear - rfRate) / vol;
}

double maxDrawdown(const std::vector<double>& cumWealth) {
    double peak = -std::numeric_limits<double>::infinity(), mdd = 0.0;
    for (double w : cumWealth) { peak = std::max(peak, w); mdd = std::max(mdd, peak - w); }
    return mdd;
}

double calmarRatio(const std::vector<double>& logRets, double barsPerYear) {
    if (logRets.empty()) return 0.0;
    const double mean = std::accumulate(logRets.begin(), logRets.end(), 0.0)
                        / logRets.size() * barsPerYear;
    std::vector<double> cumW; cumW.reserve(logRets.size());
    double cumSum = 0.0;
    for (double r : logRets) { cumSum += r; cumW.push_back(cumSum); }
    const double mdd = maxDrawdown(cumW);
    if (mdd < 1e-12) return 0.0;
    return mean / mdd;
}

double turnover(const Eigen::VectorXd& bNew, const Eigen::VectorXd& bOld) {
    return (bNew - bOld).cwiseAbs().sum();
}

double logSumExp(const Eigen::VectorXd& v) {
    const double maxV = v.maxCoeff();
    return maxV + std::log((v.array() - maxV).exp().sum());
}

bool isInSimplex(const Eigen::VectorXd& v, double tol) {
    if ((v.array() < -tol).any()) return false;
    if (std::abs(v.sum() - 1.0) > tol) return false;
    return true;
}

double l1Distance(const Eigen::VectorXd& a, const Eigen::VectorXd& b) { return (a - b).cwiseAbs().sum(); }
double lInfDistance(const Eigen::VectorXd& a, const Eigen::VectorXd& b) { return (a - b).cwiseAbs().maxCoeff(); }

} // namespace up::math
