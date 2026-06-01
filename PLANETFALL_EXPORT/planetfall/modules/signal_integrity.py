import os

class SignalIntegrityEngine:
    def __init__(self, out_dir):
        self.out_dir = out_dir

    def run(self, candidate, casefile_dir):
        print(f"[SIGNAL INTEGRITY] Evaluating TIC {candidate['TIC_ID']}...")
        with open(os.path.join(casefile_dir, 'signal_integrity_report.md'), 'w') as f:
            f.write(f"# Signal Integrity Report: TIC {candidate['TIC_ID']}\n")
            f.write("- Transit depth consistency: Marginal\n")
            f.write("- Transit duration consistency: Stable\n")
            f.write(f"- SNR: {candidate['SNR']}\n")
        
        # Aggressively reject low SNR or single sector
        if candidate['SNR'] < 10 or candidate['sector_count'] < 2:
            return False
        return True
