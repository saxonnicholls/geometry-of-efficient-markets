cmake_minimum_required(VERSION 3.20)
project(UniversalPortfolio VERSION 0.1.0 LANGUAGES CXX)

# Copyright Saxon Nicholls 2026 MIT Licence
# Universal Portfolio — Simplex Integration Engine
# Implements Papers I.1–I.5 of "The Geometry of Efficient Markets"

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# ── Build options ──────────────────────────────────────────
option(UP_ENABLE_FIX      "Build with QuickFIX support (step 4)"   OFF)
option(UP_ENABLE_TESTS    "Build unit tests"                        ON)
option(UP_ENABLE_ASAN     "Enable address sanitiser (debug)"        OFF)
option(UP_NATIVE_MARCH    "Compile with -march=native (AVX/AVX2)"   ON)

# ── Compiler flags ─────────────────────────────────────────
add_compile_options(-Wall -Wextra -Wpedantic)
if(UP_NATIVE_MARCH)
    add_compile_options(-march=native -O3 -ffast-math)
endif()
if(UP_ENABLE_ASAN)
    add_compile_options(-fsanitize=address,undefined)
    add_link_options(-fsanitize=address,undefined)
endif()

# ── Dependencies ───────────────────────────────────────────
include(FetchContent)
set(FETCHCONTENT_QUIET OFF)

# Eigen3
find_package(Eigen3 3.4 QUIET)
if(NOT Eigen3_FOUND)
    FetchContent_Declare(Eigen3
        GIT_REPOSITORY https://gitlab.com/libeigen/eigen.git
        GIT_TAG        3.4.0
        GIT_SHALLOW    TRUE)
    FetchContent_MakeAvailable(Eigen3)
endif()

# nlohmann::json
FetchContent_Declare(json
    GIT_REPOSITORY https://github.com/nlohmann/json.git
    GIT_TAG        v3.11.3
    GIT_SHALLOW    TRUE)
FetchContent_MakeAvailable(json)

# Dear ImGui
FetchContent_Declare(imgui
    GIT_REPOSITORY https://github.com/ocornut/imgui.git
    GIT_TAG        v1.90.4
    GIT_SHALLOW    TRUE)
FetchContent_MakeAvailable(imgui)

# ImPlot
FetchContent_Declare(implot
    GIT_REPOSITORY https://github.com/epezent/implot.git
    GIT_TAG        v0.17
    GIT_SHALLOW    TRUE)
FetchContent_MakeAvailable(implot)

# GLFW (for ImGui backend)
find_package(glfw3 3.3 QUIET)
if(NOT glfw3_FOUND)
    FetchContent_Declare(glfw3
        GIT_REPOSITORY https://github.com/glfw/glfw.git
        GIT_TAG        3.4
        GIT_SHALLOW    TRUE)
    FetchContent_MakeAvailable(glfw3)
endif()

find_package(OpenGL REQUIRED)

# ── ImGui static library ───────────────────────────────────
set(IMGUI_DIR ${imgui_SOURCE_DIR})
set(IMPLOT_DIR ${implot_SOURCE_DIR})

add_library(imgui_lib STATIC
    ${IMGUI_DIR}/imgui.cpp
    ${IMGUI_DIR}/imgui_draw.cpp
    ${IMGUI_DIR}/imgui_tables.cpp
    ${IMGUI_DIR}/imgui_widgets.cpp
    ${IMGUI_DIR}/backends/imgui_impl_glfw.cpp
    ${IMGUI_DIR}/backends/imgui_impl_opengl3.cpp
    ${IMPLOT_DIR}/implot.cpp
    ${IMPLOT_DIR}/implot_items.cpp)

target_include_directories(imgui_lib PUBLIC
    ${IMGUI_DIR}
    ${IMGUI_DIR}/backends
    ${IMPLOT_DIR})
target_link_libraries(imgui_lib PUBLIC glfw OpenGL::GL)

# ── QuickFIX (optional) ────────────────────────────────────
if(UP_ENABLE_FIX)
    find_package(QuickFIX REQUIRED)
    add_compile_definitions(UP_HAS_FIX)
endif()

# ── Core library ───────────────────────────────────────────
file(GLOB_RECURSE UP_SOURCES CONFIGURE_DEPENDS
    "src/math/*.cpp"
    "src/portfolio/*.cpp"
    "src/data/*.cpp"
    "src/execution/*.cpp"
    "src/benchmark/*.cpp")

# Exclude FIX source unless enabled
if(NOT UP_ENABLE_FIX)
    list(FILTER UP_SOURCES EXCLUDE REGEX ".*FIX.*\\.cpp")
endif()

add_library(up_core STATIC ${UP_SOURCES})

target_include_directories(up_core PUBLIC
    ${CMAKE_SOURCE_DIR}/include)

target_link_libraries(up_core PUBLIC
    Eigen3::Eigen
    nlohmann_json::nlohmann_json)

if(UP_ENABLE_FIX)
    target_link_libraries(up_core PUBLIC QuickFIX::quickfix)
endif()

# ── Main executable ────────────────────────────────────────
add_executable(universal_portfolio
    src/ui/Dashboard.cpp
    src/main.cpp)

target_link_libraries(universal_portfolio PRIVATE
    up_core
    imgui_lib)

# ── Tests ──────────────────────────────────────────────────
if(UP_ENABLE_TESTS)
    enable_testing()
    FetchContent_Declare(Catch2
        GIT_REPOSITORY https://github.com/catchorg/Catch2.git
        GIT_TAG        v3.5.2
        GIT_SHALLOW    TRUE)
    FetchContent_MakeAvailable(Catch2)

    file(GLOB_RECURSE TEST_SOURCES CONFIGURE_DEPENDS "tests/*.cpp")
    add_executable(up_tests ${TEST_SOURCES})
    target_link_libraries(up_tests PRIVATE up_core Catch2::Catch2WithMain)
    include(Catch)
    catch_discover_tests(up_tests)
endif()
