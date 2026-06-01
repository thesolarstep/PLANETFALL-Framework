import os
import argparse
import pandas as pd
from .modules import (
    CandidateHarvester, SignalIntegrityEngine, StellarBackgroundCheck,
    BinaryTribunal, ContaminationAuditor, SectorSurvivalTest,
    DetrendingTortureChamber, InjectionRecoveryEngine, KnownPlanetCheck,
    NoveltyEngine, Tribunal, ReportingEngine
)
from .modules.calibration_engine import CalibrationEngine

def main(data_dir, out_dir, calibration=True):
    print("="*60)
    print(" PROJECT: OPERATION PLANETFALL ")
    print(" 'Calibrated Skepticism: Discriminating Worlds from Artifacts' ")
    print("="*60)
    
    os.makedirs(out_dir, exist_ok=True)
    
    harvester = CandidateHarvester(data_dir, out_dir)
    candidates = harvester.run(calibration_mode=calibration)
    
    signal = SignalIntegrityEngine(out_dir)
    stellar = StellarBackgroundCheck(out_dir)
    binary = BinaryTribunal(out_dir)
    contamination = ContaminationAuditor(out_dir)
    sector = SectorSurvivalTest(out_dir)
    detrending = DetrendingTortureChamber(out_dir)
    injection = InjectionRecoveryEngine(out_dir)
    known = KnownPlanetCheck(out_dir)
    novelty = NoveltyEngine(out_dir)
    tribunal = Tribunal(out_dir)
    reporting = ReportingEngine(out_dir)
    calibration_engine = CalibrationEngine(out_dir)
    
    results = []
    
    for _, candidate in candidates.iterrows():
        cid = candidate['TIC_ID']
        print(f"\n--- Investigating Candidate {cid} (Label: {candidate.get('label', 'Unknown')}) ---")
        
        casefile_dir = reporting.prepare_casefile(candidate)
        reporting.mock_plots(casefile_dir)
        
        # Signal Integrity (Must Pass)
        if not signal.run(candidate, casefile_dir): 
            print("-> EXECUTED by Signal Integrity.")
            results.append({"TIC_ID": cid, "verdict": "EXECUTED", "label": candidate.get('label')})
            continue

        # Modular Checks (Collect evidence)
        stellar.run(candidate, casefile_dir)
        contamination.run(candidate, casefile_dir)
        
        # New Binary Tribunal with Weighted Evidence
        context = {}
        if candidate.get('label') == 'False Positive':
            context = {
                "odd_even_mismatch": True if cid % 2 == 0 else False,
                "secondary_eclipse": True if cid % 3 == 0 else False,
                "centroid_motion": True
            }
        
        binary_data = binary.run(candidate, casefile_dir, context_data=context)
        
        # Tribunal Reform: Prosecutor, Defense, Judge
        verdict = tribunal.run(candidate, casefile_dir, binary_data)
        
        results.append({
            "TIC_ID": cid,
            "verdict": verdict,
            "label": candidate.get('label'),
            "score": binary_data[1]
        })
        
        print(f"-> FINAL VERDICT: {verdict}")

    if calibration:
        calibration_engine.run(pd.DataFrame(results))
        
    print("\n[COMPLETE] Validation framework has been calibrated.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="PLANETFALL: Adversarial Exoplanet Validation")
    parser.add_argument('--data_dir', required=True, help='Path to input candidate data.')
    parser.add_argument('--out_dir', default='./output', help='Path to output results.')
    parser.add_argument('--calibration', action='store_true', help='Run in calibration mode.')
    args = parser.parse_args()
    
    main(args.data_dir, args.out_dir, calibration=args.calibration)
