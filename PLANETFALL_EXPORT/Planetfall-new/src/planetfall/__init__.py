"""
PLANETFALL: Adversarial Exoplanet Discovery and Validation Framework.
"""

__version__ = "1.0.0"

from .cli import main
from .data.acquisition import DataAcquisition, get_lightcurve, get_targetpixelfile, DataUnavailableError
from .data.cleaner import LightCurveCleaner, clean_lightcurve
from .data.manifest import DatasetManifest
from .engines.detrending import biweight_detrend, median_detrend, spline_detrend
from .engines.discovery import BlindDiscoveryEngine, search_transits
from .engines.transit_fitter import TransitModelFitter, fit_transit
from .engines.parameter_estimation import ParameterEstimation, estimate_parameters
from .engines.injection import InjectionRecoveryEngine
from .validators.oddeven import OddEvenValidator, test_oddeven
from .validators.secondary_eclipse import SecondaryEclipseValidator, test_secondary_eclipse
from .validators.centroid import CentroidValidator, test_centroid
from .validators.detrending_sensitivity import DetrendingSensitivityValidator, test_detrending_sensitivity
from .validators.falsification_tribunal import FalsificationTribunal, evaluate_candidate
from .reporting.publication_plots import generate_diagnostic_plots
from .reporting.casefile import save_casefile

__all__ = [
    "__version__",
    "main",
    "DataAcquisition",
    "get_lightcurve",
    "get_targetpixelfile",
    "DataUnavailableError",
    "LightCurveCleaner",
    "clean_lightcurve",
    "DatasetManifest",
    "biweight_detrend",
    "median_detrend",
    "spline_detrend",
    "BlindDiscoveryEngine",
    "search_transits",
    "TransitModelFitter",
    "fit_transit",
    "ParameterEstimation",
    "estimate_parameters",
    "InjectionRecoveryEngine",
    "OddEvenValidator",
    "test_oddeven",
    "SecondaryEclipseValidator",
    "test_secondary_eclipse",
    "CentroidValidator",
    "test_centroid",
    "DetrendingSensitivityValidator",
    "test_detrending_sensitivity",
    "FalsificationTribunal",
    "evaluate_candidate",
    "generate_diagnostic_plots",
    "save_casefile",
]
