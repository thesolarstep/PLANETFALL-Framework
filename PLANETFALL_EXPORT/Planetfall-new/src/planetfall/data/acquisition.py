import os
import re
import numpy as np
import pandas as pd
from .manifest import DatasetManifest

class DataUnavailableError(Exception):
    """Raised when astronomical data products cannot be retrieved or found."""
    pass

class DataAcquisition:
    """Manages target resolution, data downloads from MAST, and cryptographic caching."""

    def __init__(self, cache_dir="data/cache", manifest_file="data/dataset_manifest.json"):
        self.cache_dir = cache_dir
        self.manifest = DatasetManifest(manifest_file)
        os.makedirs(self.cache_dir, exist_ok=True)

    def resolve_target(self, target_id):
        """Format target name into canonical TIC or star name."""
        target_str = str(target_id).strip()
        if target_str.isdigit():
            return f"TIC {target_str}"
        if target_str.upper().startswith("TIC"):
            num = re.sub(r"[^\d]", "", target_str)
            return f"TIC {num}" if num else target_str
        if target_str.upper().startswith("TOI"):
            return target_str.upper()
        return target_str

    def get_lightcurve(self, target, sector=None, author="SPOC"):
        """
        Retrieve TESS light curve, using local cache when valid or downloading from MAST.
        
        Returns:
        --------
        dict:
            time, flux, flux_err, quality, metadata
        """
        import lightkurve as lk

        canon_target = self.resolve_target(target)
        target_safe = re.sub(r"[^\w\-]", "_", canon_target)
        sector_str = f"_s{sector}" if sector is not None else "_all"
        cache_filename = f"{target_safe}{sector_str}_lc.fits"
        cache_path = os.path.join(self.cache_dir, cache_filename)

        # 1. Check local cache
        if os.path.exists(cache_path):
            is_valid, _ = self.manifest.verify(f"{canon_target}_LC{sector_str}")
            if is_valid or not self.manifest.get(f"{canon_target}_LC{sector_str}"):
                try:
                    lc = lk.read(cache_path)
                    return self._package_lightcurve(lc, canon_target, cache_path, from_cache=True)
                except Exception:
                    pass  # corrupted cache, re-download

        # 2. Query MAST
        try:
            search_args = {"target": canon_target, "mission": "TESS"}
            if sector is not None:
                search_args["sector"] = int(sector)
            if author:
                search_args["author"] = author

            search_result = lk.search_lightcurve(**search_args)
            if len(search_result) == 0:
                # Fallback without author restriction
                search_result = lk.search_lightcurve(canon_target, mission="TESS", sector=sector)
                if len(search_result) == 0:
                    raise DataUnavailableError(f"No TESS light curves found for {canon_target} (sector={sector})")

            # Download first available sector (or specific requested sector)
            if sector is not None:
                lc = search_result[0].download()
            else:
                # Prefer first available SPOC sector
                lc = search_result[0].download()

            if lc is None:
                raise DataUnavailableError(f"Download returned empty product for {canon_target}")

            # Save to cache
            lc.to_fits(cache_path, overwrite=True)
            self.manifest.register(
                identifier=f"{canon_target}_LC{sector_str}",
                filepath=cache_path,
                source="NASA MAST / TESS SPOC Pipeline",
                sector=str(sector) if sector else "stitched",
                cadence="2-min / SPOC",
                notes=f"Retrieved {len(lc.time)} epochs"
            )

            return self._package_lightcurve(lc, canon_target, cache_path, from_cache=False)

        except Exception as e:
            if isinstance(e, DataUnavailableError):
                raise
            raise DataUnavailableError(f"Failed to retrieve light curve for {canon_target}: {e}")

    def get_targetpixelfile(self, target, sector=None, author="SPOC"):
        """
        Retrieve TESS Target Pixel File (TPF) for centroid and pixel analysis.
        """
        import lightkurve as lk

        canon_target = self.resolve_target(target)
        target_safe = re.sub(r"[^\w\-]", "_", canon_target)
        sector_str = f"_s{sector}" if sector is not None else "_sfirst"
        cache_filename = f"{target_safe}{sector_str}_tpf.fits"
        cache_path = os.path.join(self.cache_dir, cache_filename)

        if os.path.exists(cache_path):
            try:
                tpf = lk.read(cache_path)
                return tpf, cache_path
            except Exception:
                pass

        try:
            search_args = {"target": canon_target, "mission": "TESS"}
            if sector is not None:
                search_args["sector"] = int(sector)
            if author:
                search_args["author"] = author

            search_result = lk.search_targetpixelfile(**search_args)
            if len(search_result) == 0:
                search_result = lk.search_targetpixelfile(canon_target, mission="TESS")
                if len(search_result) == 0:
                    return None, "TPF_NOT_FOUND"

            tpf = search_result[0].download()
            if tpf is None:
                return None, "TPF_DOWNLOAD_EMPTY"

            tpf.to_fits(cache_path, overwrite=True)
            self.manifest.register(
                identifier=f"{canon_target}_TPF{sector_str}",
                filepath=cache_path,
                source="NASA MAST / TESS SPOC TPF",
                sector=str(tpf.sector) if hasattr(tpf, "sector") else str(sector),
                cadence="2-min / SPOC TPF",
                notes="Target Pixel File for centroid analysis"
            )
            return tpf, cache_path
        except Exception:
            return None, "TPF_QUERY_FAILED"

    def get_stellar_parameters(self, target):
        """
        Query TIC catalog / NASA Exoplanet Archive for host star parameters.
        Returns Teff, Rstar, Mstar, logg, with uncertainties.
        """
        from astroquery.mast import Catalogs

        canon_target = self.resolve_target(target)
        tic_num = re.sub(r"[^\d]", "", canon_target)

        # Default solar-like parameters with conservative uncertainties if catalog lookup fails
        default_params = {
            "teff": 5777.0, "teff_err": 150.0,
            "radius": 1.0, "radius_err": 0.1,
            "mass": 1.0, "mass_err": 0.1,
            "logg": 4.43, "logg_err": 0.15,
            "ra": 0.0, "dec": 0.0,
            "provenance": "Fallback solar defaults"
        }

        if not tic_num:
            return default_params

        try:
            cat_data = Catalogs.query_criteria(catalog="Tic", ID=int(tic_num))
            if len(cat_data) > 0:
                row = cat_data[0]
                teff = float(row['Teff']) if np.isfinite(row['Teff']) else default_params['teff']
                teff_err = float(row['e_Teff']) if 'e_Teff' in row and np.isfinite(row['e_Teff']) else 100.0
                radius = float(row['rad']) if np.isfinite(row['rad']) else default_params['radius']
                radius_err = float(row['e_rad']) if 'e_rad' in row and np.isfinite(row['e_rad']) else radius * 0.05
                mass = float(row['mass']) if np.isfinite(row['mass']) else default_params['mass']
                mass_err = float(row['e_mass']) if 'e_mass' in row and np.isfinite(row['e_mass']) else mass * 0.08
                logg = float(row['logg']) if np.isfinite(row['logg']) else default_params['logg']
                
                return {
                    "teff": teff, "teff_err": teff_err,
                    "radius": radius, "radius_err": radius_err,
                    "mass": mass, "mass_err": mass_err,
                    "logg": logg, "logg_err": 0.1,
                    "ra": float(row['ra']) if np.isfinite(row['ra']) else 0.0,
                    "dec": float(row['dec']) if np.isfinite(row['dec']) else 0.0,
                    "provenance": f"NASA MAST TIC Catalog (ID {tic_num})"
                }
        except Exception:
            pass

        return default_params

    def _package_lightcurve(self, lc, target, cache_path, from_cache=False):
        # Extract time, pdcsap_flux if available, else sap_flux, else flux
        time = lc.time.value
        flux = lc.pdcsap_flux.value if hasattr(lc, "pdcsap_flux") and lc.pdcsap_flux is not None else lc.flux.value
        flux_err = lc.pdcsap_flux_err.value if hasattr(lc, "pdcsap_flux_err") and lc.pdcsap_flux_err is not None else (lc.flux_err.value if hasattr(lc, "flux_err") else None)
        quality = lc.quality.value if hasattr(lc, "quality") else None

        meta = {
            "target": target,
            "cache_path": cache_path,
            "from_cache": from_cache,
            "mission": getattr(lc, "mission", "TESS"),
            "sector": getattr(lc, "sector", None),
            "ra": getattr(lc, "ra", None),
            "dec": getattr(lc, "dec", None)
        }

        return {
            "time": time,
            "flux": flux,
            "flux_err": flux_err,
            "quality": quality,
            "metadata": meta
        }

_acq_instance = None

def get_lightcurve(target, sector=None, author="SPOC", cache_dir="data/cache"):
    global _acq_instance
    if _acq_instance is None or _acq_instance.cache_dir != cache_dir:
        _acq_instance = DataAcquisition(cache_dir=cache_dir)
    return _acq_instance.get_lightcurve(target, sector=sector, author=author)

def get_targetpixelfile(target, sector=None, author="SPOC", cache_dir="data/cache"):
    global _acq_instance
    if _acq_instance is None or _acq_instance.cache_dir != cache_dir:
        _acq_instance = DataAcquisition(cache_dir=cache_dir)
    return _acq_instance.get_targetpixelfile(target, sector=sector, author=author)
