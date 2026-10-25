# Data Provenance and Catalog Registry

**Project:** OPERATION PLANETFALL  
**Audit Standard:** Complete Provenance, Cryptographic Hashing, and Open Access Compliance  

---

## 1. Primary Astronomical Archives

| Archive / Facility | Primary Products Ingested | Query Protocol | License / Access Terms |
|---|---|---|---|
| **NASA Mikulski Archive for Space Telescopes (MAST)** | TESS SPOC 2-Minute Cadence Light Curves & Target Pixel Files (TPF) | REST API / `lightkurve` / `astroquery.mast` | Public Domain / NASA Open Data Policy |
| **NASA Exoplanet Archive (NExScI / IPAC)** | Confirmed Planets, TOI Exoplanet Candidate Tables, Host Stellar Parameters | TAP API / HTTP GET | Public Domain / Caltech-IPAC |
| **European Space Agency Gaia DR3** | Astrometric Cross-Matches, Nearby Contaminant Photometry, Parallaxes | TAP API / CDS VizieR | ESA Gaia Open Access Policy |
| **ASAS-SN Sky Patrol** | Historical Ground-Based Time Series (Candidates #1 and #2) | Sky Patrol Public Photometry Interface | Academic Research / Attribution Required |

---

## 2. Cryptographic Checksums of Cached Datasets

All observational light curves and Target Pixel Files downloaded during execution are stored in `data/cache/` and registered with SHA-256 checksums in `data/dataset_manifest.json`:

- `WASP-18_LC_all.fits` (TESS SPOC Light Curve): Checked & Verified
- `WASP-18_TPF_sfirst.fits` (TESS Target Pixel File): Checked & Verified
- `WASP-126_LC_all.fits` (TESS SPOC Light Curve): Checked & Verified
- `TIC_88863718_LC_all.fits` (TOI-1196 TESS Light Curve): Checked & Verified

---

## 3. Separation of Observations and Transformed Products

- **Raw Observational Data:** Cached in `data/cache/*.fits` with original FITS headers preserved intact.
- **Cleaned & Detrended Time Series:** Intermediate normalized arrays with deterministic parameters.
- **Derived Candidate Casefiles:** Stored in `output/` with machine-readable JSON and Markdown reports.
