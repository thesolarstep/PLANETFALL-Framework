import pytest
import numpy as np
from planetfall.engines.discovery import BlindDiscoveryEngine

def test_blind_transit_discovery():
    """Verify BLS engine recovers known period without prior assistance."""
    time = np.linspace(0, 15, 3000)
    true_period = 3.25
    true_t0 = 0.8
    true_depth = 0.008
    true_dur = 0.12

    flux = np.ones_like(time)
    phase = ((time - true_t0 + 0.5 * true_period) % true_period) - 0.5 * true_period
    in_tr = np.abs(phase) < (0.5 * true_dur)
    flux[in_tr] -= true_depth
    flux += np.random.normal(0, 0.0004, len(time))

    searcher = BlindDiscoveryEngine(period_min=1.0, period_max=8.0, min_snr=5.0)
    res = searcher.search(time, flux)

    assert res["status"] == "DETECTED"
    assert abs(res["period"] - true_period) / true_period < 0.01, f"Period recovery error: {res['period']}"
    assert res["snr"] > 10.0
    assert res["sde"] > 5.0
    assert not res["is_diurnal_alias"]

def test_diurnal_alias_detection():
    """Verify engine correctly flags 1.0-day diurnal alias."""
    time = np.linspace(0, 10, 2000)
    # 1.001-day period
    phase = ((time + 0.5) % 1.001) - 0.5
    flux = 1.0 - 0.01 * (np.abs(phase) < 0.03)

    searcher = BlindDiscoveryEngine(period_min=0.5, period_max=5.0)
    res = searcher.search(time, flux)

    assert res["is_diurnal_alias"]
    assert "1.0-day terrestrial" in res["alias_reason"]
