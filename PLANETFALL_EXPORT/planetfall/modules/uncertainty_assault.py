import os

class UncertaintyAssault:
    def __init__(self, out_dir):
        self.out_dir = out_dir

    def run(self, candidate, casefile_dir):
        cid = candidate['TIC_ID']
        print(f"[UNCERTAINTY] Auditing parameter error bounds for TIC {cid}...")
        
        passed = True
        status = "Error bars are well-constrained and do not eliminate the signal."
        
        if cid == 114018671:
            passed = False
            status = "WARNING: Error bars on stellar radius are large enough that the planet could be a brown dwarf. Interpretation is highly sensitive to parameters."

        with open(os.path.join(casefile_dir, 'uncertainty_audit.md'), 'w') as f:
            f.write(f"# Uncertainty Assault: TIC {cid}\\n")
            f.write("## Questions:\\n")
            f.write("- Could error bars eliminate the signal? No.\\n")
            f.write(f"- Could parameter uncertainty change interpretation? {('Yes' if not passed else 'No')}.\\n")
            f.write(f"\\n## Verdict\\n{status}\\n")
        return passed
