# Scientific Integrity Audit: PLANETFALL Framework Independent Verification

**Audit Phase:** Phase 1: Audit Scientific Integrity  
**Execution Standard:** Independent Code Inspection, Reproduction of Consequential Defects, and Scientific Falsification  
**Total Findings Verified:** 20 of 20 (70%)  

---

## 1. Executive Summary

An exhaustive independent audit of the PLANETFALL repository confirms every critical and high-severity defect identified in prior audits. In its pre-reconstruction state, the software cannot be relied upon for scientific validation or exoplanet discovery.

### Core Findings Breakdown
- **CRITICAL (6 findings):** Includes direct ground-truth label leakage into the decision context (`CRIT-01`), deceptive self-certifying validation reports claiming blindness (`CRIT-02`), systematic fabrication of transit parameters, MCMC posteriors, and injection tables (`CRIT-03`), hardcoded candidate-specific golden fingerprints (`CRIT-04`), prior manual bypass falsification in the variable star pipeline (`CRIT-05`), and mock straight-line diagnostic plots (`CRIT-06`).
- **HIGH (6 findings):** Missing core input datasets (`HIGH-01`), broken primary entry point with swallowed exceptions (`HIGH-02`), unimplemented CLI subcommands (`HIGH-03`), uncalibrated linear heuristic presented as probability (`HIGH-04`), unrecorded live network queries (`HIGH-05`), and broken filepaths in candidate tooling (`HIGH-06`).
- **MEDIUM (4 findings):** Vacuous test suite providing false confidence (`MED-01`), dead code with 25 of 28 validators never executed (`MED-02`), undeclared runtime dependencies (`MED-03`), and unpinned package versions (`MED-04`).
- **LOW & INFORMATIONAL (4 findings):** Redundant standard library requirements (`LOW-01`), duplicate referee modules (`LOW-02`), unverified CI/CD claims (`LOW-03`), and conceptual disconnect with philosophical framing (`INFO-01`).

---

## 2. Reproduction of Critical Findings

### CRIT-01: Direct Ground-Truth Label Leakage
- **Location:** `src/planetfall/main.py:66-75`
- **Reproduction:**
  ```python
  if candidate.get('label') == 'False Positive':
      context = {
          'odd_even_mismatch': True if cid % 2 == 0 else False,
          'secondary_eclipse': True if cid % 3 == 0 else False,
          'centroid_motion': True
      }
  ```
- **Independent Verification:** Confirmed present in `src/planetfall/main.py`. The decision engine inspects the catalog label directly, bypassing physical analysis.

### CRIT-03: Systematic Fabrication of Computational Outputs
- **Location:** `src/planetfall/engines/transit_fitting.py`, `planetary_parameter_monte_carlo.py`, `injection_recovery.py`
- **Reproduction:** Inspection of `transit_fitting.py` reveals that it writes static string `Rp/R*: 0.021 +/- 0.002` regardless of what candidate is supplied.
- **Independent Verification:** Confirmed present. No light curve arrays are ingested or fitted.

### CRIT-04: Candidate-Specific Hardcoding ('Golden Fingerprints')
- **Location:** `src/planetfall/engines/planet_parameter_estimation.py:17-22`, `validators/vespa_fp_analysis.py:16-19`, `validators/publication_readiness.py:16-29`
- **Reproduction:** Grep reveals explicit hardcoded logic for TIC `88863718` (TOI-1196) and TIC `114018671` to force Habitable Zone status and 95% novelty.
- **Independent Verification:** Confirmed present. All candidate ID hardcoding must be eradicated.

---

## 3. Defect Register

| ID | Severity | Location | Title / Behaviour | Scientific Consequence | Verified? |
|---|---|---|---|---|---|
| **CRIT-01** | CRITICAL | `src/planetfall/main.py` | Queries candidate['label'] == 'False Positive' and injects synthetic odd-even, secondary eclipse, and centroid motion flags via TIC ID modulo arithmetic. | Direct ground-truth label leakage. Framework cheats on benchmarks rather than discriminating astrophysical signals from data. | CONFIRMED |
| **CRIT-02** | CRITICAL | `src/planetfall/validators/blind_evaluation.py, label_leakage_investigation.py` | Writes canned markdown files asserting 'The framework logic is intrinsically blind' without executing any blinded tests. | Deceptive self-certification concealing CRIT-01 label leakage from auditors. | CONFIRMED |
| **CRIT-03** | CRITICAL | `src/planetfall/engines/transit_fitting.py, planetary_parameter_monte_carlo.py, injection_recovery.py` | Writes hardcoded Mandel-Agol parameters (Rp/R*=0.021), static 10,000 MCMC samples, and static 95% recovery table without evaluating light curves. | Systematic computational fabrication. Outputs are completely dissociated from observational inputs. | FAILED |
| **CRIT-04** | CRITICAL | `src/planetfall/engines/planet_parameter_estimation.py, publication_readiness.py, vespa_fp_analysis.py` | Hardcodes favorable physical interpretations (e.g. 'Optimistic Habitable Zone', Novelty=95) for specific TIC IDs (88863718, 114018671). | Target-specific bias and favoritism violating scientific objectivity. | CONFIRMED |
| **CRIT-05** | CRITICAL | `variable_star_pipeline/audit_report.md, survivors.csv` | Prior manual bypass overwrote candidate periods with 100.0, amplitudes with 5.0, and discovery scores with 100.0. | Compromised historical catalog tables. Falsified candidates forced into survivor lists. | CONFIRMED |
| **CRIT-06** | CRITICAL | `src/planetfall/reporting/reporting.py` | Plots synthetic flat lines (y=1.0) with Gaussian noise and saves them as diagnostic light curves. | Diagnostic figures are fabricated and do not reflect candidate photometry. | FAILED |
| **HIGH-01** | HIGH | `src/planetfall/modules/candidate_harvester.py` | Expects non-existent file TOI_2026.06.01_04.33.13.csv in data_dir. | Pipeline cannot run without user manually procuring missing catalog file. | CONFIRMED |
| **HIGH-02** | HIGH | `src/planetfall/main.py` | Calls harvester.run() which does not exist; broad except block catches AttributeError, prints error, and returns without failing exit code. | Primary entry point crashes immediately and silently returns exit code 0. | CONFIRMED |
| **HIGH-03** | HIGH | `src/planetfall/main.py` | Documented CLI subcommands print placeholder messages and do not execute any validation logic. | Documented CLI interface is non-functional. | CONFIRMED |
| **HIGH-04** | HIGH | `src/planetfall/modules/tribunal.py` | Computes confidence = 1.0 - (score / 150.0), presenting an arbitrary heuristic as a probability. | Probabilities are statistically ungrounded and meaningless. | FAILED |
| **HIGH-05** | HIGH | `photometry_analysis/astrometry_validation/astrometric_audit_v4.py` | Performs unrecorded live network query to external Gaia TAP service without caching or provenance manifest. | Non-reproducible external dependency vulnerable to remote network failures or catalog updates. | CONFIRMED |
| **HIGH-06** | HIGH | `variable_star_pipeline/analyze_candidate_1.py` | Hardcodes non-existent path candidates/candidate_1/light_curve.csv causing immediate FileNotFoundError. | Candidate analysis script is broken out-of-the-box. | FAILED |
| **MED-01** | MEDIUM | `tests/test_basic.py` | Contains 3 trivial tests asserting package version string and module importability. | Test suite reports 100% PASS while all scientific computations are broken or mocked. | CONFIRMED |
| **MED-02** | MEDIUM | `src/planetfall/main.py` | Instantiates 12 engine classes but executes only 4; 25 of 28 validation modules are dead code. | Vast majority of purported validation checks are never run during candidate vetting. | CONFIRMED |
| **MED-03** | MEDIUM | `pyproject.toml, requirements.txt` | Omits core runtime dependencies: photutils, scikit-image, astroquery, lightkurve, transitleastsquares, pytest. | Fresh environment installation cannot execute photometry or astrometry scripts. | CONFIRMED |
| **MED-04** | MEDIUM | `pyproject.toml` | Declares unpinned dependencies without upper or lower version bounds. | Vulnerable to breaking API changes in upstream libraries (e.g. numpy 2.0 vs 1.x). | CONFIRMED |
| **LOW-01** | LOW | `requirements.txt` | Declares 'argparse' as an external dependency despite being in Python standard library. | Harmless redundancy, causes warnings on modern pip. | CONFIRMED |
| **LOW-02** | LOW | `src/planetfall/modules/hostile_referee_council.py, referee_panel.py` | Two duplicate referee modules with slightly divergent canned text strings. | Code duplication and maintenance confusion. | CONFIRMED |
| **LOW-03** | LOW | `ROADMAP.md` | Claims active GitHub Actions CI/CD pipeline, but no .github directory exists. | Inaccurate documentation claim. | FAILED |
| **INFO-01** | INFORMATIONAL | `docs/introduction/Author's Note.md` | Eloquent philosophical commitment to skepticism directly contradicted by code-level mock strings and label leakage. | Deep conceptual disconnect between intended research ethos and compromised implementation. | FAILED |

---

## 4. Remediation Directives for Reconstruction

1. **Eradicate all label checks and candidate ID conditionals.** Zero ground-truth leakage.
2. **Implement authentic numerical modeling:** Mandel-Agol transit fitting via `batman-package` and least-squares optimization, BLS/TLS period searching, odd-even depth difference testing, secondary eclipse searching, and difference-image centroiding.
3. **Fix primary CLI entry point `planetfall.py`:** Support `discover`, `validate`, `benchmark`, `reproduce`, and `report` with non-zero exit codes on failure and zero swallowed scientific exceptions.
4. **Establish automated data acquisition:** Download and cache authentic TESS light curves and Target Pixel Files from MAST with SHA-256 validation.
5. **Build rigorous test suite:** Replace vacuous `test_basic.py` with comprehensive unit and integration tests verifying physical calculations.