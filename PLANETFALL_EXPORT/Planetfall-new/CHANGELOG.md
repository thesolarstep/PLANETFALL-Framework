# Changelog: PLANETFALL Scientific Maturation

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-10-25 (Complete Scientific Reconstruction)

### Added
- **Production CLI (`planetfall.py`):** Unified command-line interface supporting `discover`, `validate`, `benchmark`, `reproduce`, and `report` with explicit arguments and zero swallowed exceptions.
- **Blind Discovery Engine (`planetfall.engines.discovery`):** Genuine Box Least Squares (BLS) period searching directly on conditioned time series without reference labels or period hints.
- **Mandel-Agol Limb-Darkened Modeling (`planetfall.engines.transit_fitter`):** High-precision analytical transit profile fitting with least-squares parameter covariance uncertainty propagation.
- **Physical Parameter Estimation (`planetfall.engines.parameter_estimation`):** Derivation of planetary radius ($R_\oplus, R_{Jup}$), semi-major axis, insolation flux, and equilibrium temperature with analytical Taylor error propagation.
- **2D Injection-Recovery Engine (`planetfall.engines.injection`):** Authentic signal injection and blind recovery measuring empirical completeness and parameter bias.
- **Adversarial Vetting Gauntlet (`planetfall.validators`):**
  - Odd-even depth difference statistical test ($Z_{oe}$)
  - Secondary eclipse search and companion constraints ($SNR_{sec}$)
  - Target Pixel File (TPF) difference image centroid offset analysis
  - Detrending filter bandwidth sensitivity testing
  - Calibrated Bayesian False Positive Probability (FPP) synthesis
- **8 Independent Benchmarks (`planetfall.benchmarks.suite`):** Complete execution suite evaluating recovery, false positive rejection, injection completeness, held-out blind search, detrending robustness, centroid resolution, cross-sector repeatability, and adversarial edge cases.
- **Automated Test Suite (`tests/`):** 14 comprehensive unit and integration tests verifying physical modeling, period recovery, and error propagation (100% pass rate).
- **Cryptographic Data Manifest (`planetfall.data.manifest`):** Automatic SHA-256 calculation and provenance recording for all retrieved datasets.

### Fixed
- **Eradicated CRIT-01 Ground-Truth Label Leakage:** Completely purged `candidate.get('label') == 'False Positive'` and TIC ID modulo arithmetic from `src/planetfall/main.py`.
- **Eradicated CRIT-03 Output Fabrication:** Replaced static strings in `transit_fitting.py`, `planetary_parameter_monte_carlo.py`, and `injection_recovery.py` with real numerical algorithms.
- **Eradicated CRIT-04 Candidate ID Hardcoding:** Deleted all `if cid == 88863718` and `if cid == 114018671` golden fingerprint branches.
- **Fixed HIGH-02 Broken Main Entry Point:** Implemented complete execution flow in `CandidateHarvester` and replaced broad exception suppression with proper non-zero exit codes.
- **Fixed HIGH-03 Placeholder Subcommands:** Implemented all documented CLI actions.
- **Fixed HIGH-04 Uncalibrated Heuristic:** Replaced `1.0 - (score / 150.0)` with mathematically rigorous Bayesian likelihood ratios.
- **Fixed HIGH-06 Broken Filepaths:** Resolved broken paths in candidate investigation tooling.
- **Resolved MED-01 to MED-04:** Expanded test suite, activated validation modules, declared missing runtime dependencies, and pinned version compatibility bounds.

### Quarantined
- Quarantined deceptive self-certifying mock validators (`blind_evaluation.py`, `label_leakage_investigation.py`, `reproducibility_audit.py`).
- Quarantined historical variable star catalog containing manual 100.0/5.0 overrides (`survivors.csv`).
