# PLANETFALL Workflow

## 1. Input Preparation
Users provide candidate catalogs and associated light curve data. PLANETFALL expects standard formats like TIC (TESS Input Catalog) IDs.

## 2. The Gauntlet (Execution)
The `main.py` script orchestrates the flow:
- Ingesting candidates.
- Running parallel validation modules.
- Accumulating evidence of falsification.

## 3. The Verdict
The Tribunal evaluates the cumulative evidence. 
- If the **Suspicion Score** exceeds the threshold, the candidate is **EXECUTED**.
- If it survives, it is flagged for manual professional review.

## 4. Casefile Generation
For every run, PLANETFALL generates an `output/` directory containing:
- `master_catalog.csv`: Status of all candidates.
- `casefile_<ID>/`: A dedicated folder for each candidate with detailed reports and plots (visualizations of the prosecution).
