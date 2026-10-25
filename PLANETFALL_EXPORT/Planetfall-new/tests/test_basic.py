import pytest
from planetfall import __version__
from planetfall.engines import BlindDiscoveryEngine, TransitModelFitter, ParameterEstimation
from planetfall.validators import OddEvenValidator, SecondaryEclipseValidator, FalsificationTribunal

def test_version():
    assert __version__ == "1.0.0"

def test_import_engines():
    assert BlindDiscoveryEngine is not None
    assert TransitModelFitter is not None
    assert ParameterEstimation is not None

def test_import_validators():
    assert OddEvenValidator is not None
    assert SecondaryEclipseValidator is not None
    assert FalsificationTribunal is not None
