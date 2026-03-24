// Copyright Saxon Nicholls 2026 MIT Licence
// Universal Portfolio — Simplex Integration Engine
// Implements Papers I.1–I.5 of "The Geometry of Efficient Markets"

#include <iostream>
#include <thread>
#include <atomic>
#include <chrono>
#include <csignal>

#include "portfolio/UniversalPortfolio.hpp"
#include "portfolio/LaplaceIntegrator.hpp"
#include "portfolio/MonteCarloIntegrator.hpp"
#include "portfolio/FactorProjectedIntegrator.hpp"
#include "portfolio/EGIntegrator.hpp"
#include "data/SyntheticDataSource.hpp"
#include "benchmark/MethodBenchmark.hpp"
#include "execution/ExecutionEngines.hpp"
#include "ui/Dashboard.hpp"
#include "math/SimplexMath.hpp"

using namespace up;
using namespace std::chrono_literals;

// ───────────────────────────────────────────────────────────
// Signal handling for graceful shutdown
// ───────────────────────────────────────────────────────────

std::atomic<bool> g_shutdown{false};
void onSignal(int) { g_shutdown = true; }

// ───────────────────────────────────────────────────────────
// Run a full benchmark comparing all integration methods
// ───────────────────────────────────────────────────────────

void runBenchmark(ui::Dashboard& dashboard,
                  const ui::DashboardState& state)
{
    std::cout << "\n─────────────────────────────────────────────────────\n";
    std::cout << "  Universal Portfolio — Integration Method Benchmark\n";
    std::cout << "  d = " << state.numAssets
              << "  T_train = " << state.benchTrainPeriods
              << "  T_test  = " << state.benchTestPeriods << "\n";
    std::cout << "─────────────────────────────────────────────────────\n\n";

    // Generate synthetic data
    auto src = std::make_shared<SyntheticDataSource>();
    nlohmann::json srcCfg = {
        {"mode",       "factor"},
        {"numAssets",  state.numAssets},
        {"numPeriods", state.benchTrainPeriods + state.benchTestPeriods + 50},
        {"numFactors", state.numFactors},
        {"factorVol",  state.factorVol},
        {"idioVol",    state.idioVol},
        {"seed",       state.randomSeed}
    };
    src->initialise(srcCfg);
    const Eigen::MatrixXd data = src->generateAll();

    // Register all integration methods
    auto bench = std::make_shared<MethodBenchmark>();
    BenchmarkConfig bcfg;
    bcfg.trainPeriods  = state.benchTrainPeriods;
    bcfg.testPeriods   = state.benchTestPeriods;
    bcfg.numTrials     = state.benchTrials;
    bcfg.printProgress = true;
    bcfg.saveResults   = true;
    bcfg.outputPath    = "benchmark_results.json";
    bench->initialise(bcfg);

    bench->addMethod(std::make_shared<LaplaceIntegrator>());
    bench->addMethod(std::make_shared<MonteCarloIntegrator>(false));  // plain MC
    bench->addMethod(std::make_shared<MonteCarloIntegrator>(true));   // QMC Halton
    bench->addMethod(std::make_shared<FactorProjectedIntegrator>());
    bench->addMethod(std::make_shared<EGIntegrator>());

    bench->run(data);
    bench->printSummaryTable();

    // Push results to dashboard
    {
        auto& ds = dashboard.state();
        ds.benchResults = bench->getResults();
        const auto& names  = bench->getMethodNames();
        const auto& series = bench->getCumulativeWealthSeries();
        ds.methodWealthSeries.clear();
        for (std::size_t i = 0; i < names.size() && i < series.size(); ++i) {
            std::vector<float> fs(series[i].begin(), series[i].end());
            ds.methodWealthSeries[names[i]] = fs;
        }
    }
}

// ───────────────────────────────────────────────────────────
// Main data + portfolio loop (runs in background thread)
// ───────────────────────────────────────────────────────────

void portfolioLoop(
    PortfolioPtr           portfolio,
    ExecutionEnginePtr     exec,
    ui::Dashboard&         dashboard,
    std::atomic<bool>&     running)
{
    auto& state = dashboard.state();
    auto  src   = std::make_shared<SyntheticDataSource>();

    auto buildSource = [&]() {
        nlohmann::json cfg = {
            {"mode",         state.synthMode == 0 ? "gbm"
                           : state.synthMode == 1 ? "factor"
                           : state.synthMode == 2 ? "block_bootstrap" : "markov"},
            {"numAssets",    state.numAssets},
            {"numPeriods",   state.numPeriods},
            {"numFactors",   state.numFactors},
            {"factorVol",    state.factorVol},
            {"idioVol",      state.idioVol},
            {"seed",         state.randomSeed},
            {"replaySpeedMs", 0.0}  // max speed
        };
        src->initialise(cfg);
        src->generateAll();
    };

    buildSource();

    while (running && !g_shutdown) {
        if (!state.isRunning) {
            std::this_thread::sleep_for(50ms);
            continue;
        }

        if (!src->hasMore()) {
            // Loop back around
            src->connect();
            buildSource();
        }

        auto bar = src->nextBar();
        if (!bar) { std::this_thread::sleep_for(10ms); continue; }

        // Update portfolio
        portfolio->update(bar->priceRelatives, bar->timestamp);

        // Execution
        if (state.executionEnabled && exec) {
            const auto& s  = portfolio->getState();
            if (s.periodsObserved > 20 && !s.weights.isZero()) {
                // Update prices in execution engine
                if (auto* paper = dynamic_cast<PaperExecutionEngine*>(exec.get())) {
                    // synthesise mid prices from price relatives (cumulative product)
                    Eigen::VectorXd prices = bar->priceRelatives;
                    paper->updatePrices(bar->symbols, prices);
                }

                RebalanceInstruction instr;
                instr.timestamp     = bar->timestamp;
                instr.symbols       = bar->symbols;
                instr.targetWeights = s.weights;
                instr.currentWeights = exec->getCurrentWeights();
                if (instr.currentWeights.size() != s.weights.size())
                    instr.currentWeights = Eigen::VectorXd::Ones(s.weights.size())
                                          / s.weights.size();
                instr.deltaWeights  = instr.targetWeights - instr.currentWeights;
                instr.portfolioNAV  = exec->getNAV();
                instr.minTrade      = 10.0;  // 10 bps minimum
                instr.reason        = "new_bar";
                exec->rebalance(instr);
            }
        }

        // Small sleep to avoid spinning the UI thread
        std::this_thread::sleep_for(1ms);
    }
}

// ───────────────────────────────────────────────────────────
// Entry point
// ───────────────────────────────────────────────────────────

int main(int argc, char** argv) {
    (void)argc; (void)argv;

    std::signal(SIGINT,  onSignal);
    std::signal(SIGTERM, onSignal);

    std::cout << R"(
  ─────────────────────────────────────────────────────
  │   Universal Portfolio — Simplex Integration Engine  │
  │   Cover (1991) · Laplace / MC / QMC / Factor / EG  │
  ─────────────────────────────────────────────────────
)" << "\n";

    // ── Build portfolio with Laplace integrator (default) ────
    PortfolioConfig portCfg;
    portCfg.minPeriods          = 20;
    portCfg.incrementalUpdates  = true;
    portCfg.method              = IntegrationMethodType::Laplace;
    portCfg.integration.maxIterations = 500;
    portCfg.integration.convergenceTol = 1e-9;

    // Generate asset names (50 synthetic stocks)
    for (int i = 0; i < 50; ++i)
        portCfg.assetNames.push_back("SYN" + std::to_string(i+1));

    auto integrator = std::make_shared<LaplaceIntegrator>();
    auto portfolio  = std::make_shared<UniversalPortfolio>(integrator, portCfg);
    portfolio->initialise(portCfg);

    // ── Execution engine ─────────────────────────────────────
    auto exec = std::make_shared<PaperExecutionEngine>();
    nlohmann::json execCfg = {
        {"initialNAV",    1'000'000.0},
        {"spreadBps",     5.0},
        {"commissionBps", 1.0},
        {"minTradeBps",   10.0}
    };
    exec->initialise(execCfg);
    exec->connect();

    // ── Dashboard ─────────────────────────────────────────────
    ui::Dashboard dashboard;
    if (!dashboard.init(1600, 900)) {
        std::cerr << "Failed to initialise ImGui/GLFW\n";
        return 1;
    }
    dashboard.attachPortfolio(portfolio);

    // ── Portfolio loop thread ─────────────────────────────────
    std::atomic<bool> loopRunning{true};
    std::thread portfolioThread([&]() {
        portfolioLoop(portfolio, exec, dashboard, loopRunning);
    });

    // ── Render loop ───────────────────────────────────────────
    while (!dashboard.shouldClose() && !g_shutdown) {
        if (!dashboard.beginFrame()) break;

        dashboard.render(portfolio, nullptr, exec);

        // Trigger benchmark if requested
        if (dashboard.state().showBenchmark) {
            static bool benchRan = false;
            if (!benchRan) {
                benchRan = true;
                std::thread([&]() {
                    runBenchmark(dashboard, dashboard.state());
                }).detach();
            }
        }

        dashboard.endFrame();
    }

    // ── Cleanup ────────────────────────────────────────────────
    loopRunning = false;
    g_shutdown  = true;
    portfolioThread.join();
    dashboard.shutdown();

    std::cout << "\n[main] Shutdown complete.\n";

    // Print final execution report to stdout
    const auto report = exec->getExecutionReport();
    std::cout << "Execution report:\n" << report.dump(2) << "\n";

    // Save portfolio state
    portfolio->saveState("portfolio_state.json");
    std::cout << "Portfolio state saved to portfolio_state.json\n";

    return 0;
}
