# PLANETFALL

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Status: v1.0.0--release](https://img.shields.io/badge/Version-1.0.0--release-brightgreen.svg)](https://github.com/thesolarstep/planetfall-validation-framework)
[![Tests: 14 passed](https://img.shields.io/badge/Tests-14%20passed-brightgreen.svg)](tests/)

**An adversarial, falsification-driven scientific discovery and validation engine for exoplanetary transits and astronomical time series.**

---

## 🌌 Scientific Mission & Contract

PLANETFALL inverts conventional exoplanet vetting pipelines. Rather than attempting to maximize candidate detection volume, PLANETFALL enforces **calibrated skepticism**: assuming candidate signals are astrophysical false positives, stellar variability, or instrumental artifacts until proven otherwise.

The framework operates under three strictly partitioned modes:
1. **Mode A: Blind Discovery Engine:** Ingests raw time-series photometry and observational metadata without access to known periods, ephemerides, or catalog disposition labels. Detects transits using Box Least Squares (BLS), screens for aliases and harmonics, and extracts physical signal parameters.
2. **Mode B: Candidate Validation Gauntlet:** Prosecutes detected signals with an adversarial battery of tests:
   - Analytical Mandel-Agol limb-darkened transit profile fitting
   - Odd-even transit depth difference testing ($Z_{oe}$)
   - Secondary eclipse search and thermal constraint ($SNR_{sec}$)
   - Pixel-level Target Pixel File (TPF) difference image centroiding
   - Detrending filter bandwidth sensitivity testing
   - Synthetic injection-recovery completeness testing
   - Statistically calibrated Bayesian False Positive Probability (FPP)
3. **Mode C: Reproducible Research:** Complete cryptographic hashing (SHA-256), open-access provenance tracking, and deterministic casefile logging. Missing evidence is honestly reported as `NOT_TESTED` or `UNAVAILABLE`, never `PASS`.

---

## 🚀 Quickstart & Installation

```bash
# Clone the repository
git clone https://github.com/thesolarstep/planetfall-validation-framework.git
cd planetfall-validation-framework

# Create isolated environment
python3 -m venv .venv
source .venv/bin/activate

# Install in editable mode with development dependencies
pip install -e ".[dev]"
```

### Run Automated Unit & Scientific Validation Tests
```bash
pytest tests/
```

### Run the 8 Independent Benchmark Suites
```bash
python planetfall.py benchmark --suite all
```

### Run Blind Discovery on a TESS Target
```bash
python planetfall.py discover --target WASP-18
```

### Validate a Specific Candidate Ephemeris
```bash
python planetfall.py validate --target WASP-18 --period 0.941452 --t0 1354.46 --duration 0.09
```

### Reproduce Historical Case Studies
```bash
python planetfall.py reproduce --case toi-1196
python planetfall.py reproduce --case asassn-candidate-1
```

---

## 🏛 Package Architecture

```
planetfall-validation-framework/
├── planetfall.py                     # Primary executable entry point
├── src/planetfall/
│   ├── cli.py                        # Core CLI implementation
│   ├── data/
│   │   ├── acquisition.py            # MAST / TESS downloader with SHA-256 caching
│   │   ├── cleaner.py                # Quality bitmask, gap assessment, outlier rejection
│   │   └── manifest.py               # Cryptographic dataset provenance registry
│   ├── engines/
│   │   ├── detrending.py             # Windowed biweight, median, and spline detrending
│   │   ├── discovery.py              # Box Least Squares (BLS) blind transit search
│   │   ├── transit_fitter.py         # Mandel-Agol limb-darkened transit model fitting
│   │   ├── parameter_estimation.py   # Keplerian physics and error propagation
│   │   └── injection.py              # Authentic 2D injection-recovery grid
│   ├── validators/
│   │   ├── oddeven.py                # Odd-even depth difference statistical test
│   │   ├── secondary_eclipse.py      # Secondary eclipse search and companion constraints
│   │   ├── centroid.py               # TPF difference image centroid offset
│   │   ├── detrending_sensitivity.py # Preprocessing window sensitivity
│   │   └── falsification_tribunal.py # Calibrated Bayesian FPP & verdict synthesis
│   ├── reporting/
│   │   ├── publication_plots.py      # Publication-quality diagnostic figures
│   │   └── casefile.py               # Machine-readable JSON and Markdown casefiles
│   └── benchmarks/
│       └── suite.py                  # 8 independent benchmark execution harnesses
├── reports/                          # Audit records, benchmark results, and candidate lists
│   ├── BENCHMARK_PROTOCOL.md
│   ├── BENCHMARK_RESULTS.md
│   ├── SCIENTIFIC_LIMITATIONS.md
│   ├── DATA_PROVENANCE.md
│   ├── FINAL_ACCEPTANCE_MATRIX.csv
│   ├── KNOWN_CANDIDATES.csv
│   ├── UNRESOLVED_CANDIDATES.csv
│   └── NEW_CANDIDATE_SHORTLIST.csv
└── tests/                            # Comprehensive scientific test suite
```

---

## 📊 Benchmark Summary

| Benchmark | Focus | Metric | Result |
|---|---|---|---|
| **BM1: Confirmed Planet Recovery** | WASP-18, WASP-126, TOI-1196 | Period Error | **0.003% error (WASP-18, WASP-126)** |
| **BM2: False-Positive Rejection** | Simulated EBs & Companions | Specificity | **100% rejection of EBs (FPP = 0.9999)** |
| **BM3: Injection-Recovery** | 2D parameter grid | Empirical Completeness | Measured across period/depth grid |
| **BM4: Blind Search** | Held-out light curves | Candidate Yield | Blind detection without reference labels |
| **BM5: Detrending Robustness** | Biweight vs Median vs Spline | Continuum RMS | Biweight achieves 686 ppm out-of-transit |
| **BM6: Centroid Analysis** | Real TPF vs Missing TPF | Offset Accuracy | 0.43 pix on target; missing TPF marked `NOT_TESTED` |
| **BM7: Cross-Sector Repeatability** | Sectors 2 & 3 | Repeatability | Confirmed repeatable physical signals |
| **BM8: Adversarial Suite** | Aliases, NaNs, Edge Cases | Robustness | 4/4 edge cases passed safely |

---

## 📜 Scientific Citation & License

If you use PLANETFALL in academic research:
```bibtex
@software{planetfall2026,
  author = {Kadam, Aditya Anil and Antigravity Autonomous Scientific Team},
  title = {PLANETFALL: Adversarial Exoplanet Discovery and Validation Framework},
  year = {2026},
  version = {1.0.0},
  url = {https://github.com/thesolarstep/planetfall-validation-framework}
}
```

Licensed under the [MIT License](LICENSE).
