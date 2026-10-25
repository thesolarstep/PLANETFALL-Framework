"""PLANETFALL Adversarial Validation Subpackage."""

from .oddeven import OddEvenValidator, test_oddeven
from .secondary_eclipse import SecondaryEclipseValidator, test_secondary_eclipse
from .centroid import CentroidValidator, test_centroid
from .detrending_sensitivity import DetrendingSensitivityValidator, test_detrending_sensitivity
from .falsification_tribunal import FalsificationTribunal, evaluate_candidate

__all__ = [
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
]
