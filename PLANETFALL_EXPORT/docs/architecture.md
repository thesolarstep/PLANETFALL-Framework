# PLANETFALL Architecture

The framework is structured as a modular "Prosecution Engine."

## Core Components

### 1. Candidate Harvester
Responsible for ingesting candidate data from various sources (TESS, Kepler, etc.) and preparing them for the validation gauntlet.

### 2. Validation Modules
A suite of independent engines that analyze different aspects of the signal:
- **Signal Integrity**: Checks for SNR, period stability, and transit shape.
- **Binary Tribunal**: Investigates eclipsing binary (EB) characteristics (odd-even mismatches, secondary eclipses).
- **Stellar Background**: Analyzes the neighborhood of the target star for potential contamination.
- **Detrending Torture**: Subjecting the signal to multiple detrending algorithms to see if it survives.

### 3. The Tribunal
The central decision logic. It collects "Suspicion Scores" from all validation modules and convenes a symbolic court:
- **Prosecutor**: Argues for execution based on suspicion scores.
- **Defense**: Argues for survival based on signal robustness.
- **Judge**: Issues the final verdict (EXECUTED or PASSED) and a confidence score.

### 4. Reporting Engine
Generates detailed "Casefiles" for every candidate, documenting why it was rejected or allowed to pass.
