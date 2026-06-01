import os

class ExoFOPInvestigation:
    def __init__(self, out_dir):
        self.out_dir = out_dir

    def run(self, candidate, casefile_dir):
        cid = candidate['TIC_ID']
        print(f"[EXOFOP] Investigating community notes for TIC {cid}...")
        
        # Mock logic
        flags = "None"
        rv_status = "Not Started"
        
        if cid == 107782586:
            rv_status = "In Progress (HARPS)"
        elif cid == 114018671:
            flags = "Warning: Faint nearby companion spotted in adaptive optics."

        with open(os.path.join(casefile_dir, 'exofop_investigation.md'), 'w') as f:
            f.write(f"# ExoFOP Investigation: TIC {cid}\\n")
            f.write(f"- TOI Status: Active PC\\n")
            f.write(f"- Community Flags: {flags}\\n")
            f.write(f"- RV Follow-up: {rv_status}\\n")
            f.write("- Proposed Disposition: None yet.\\n")
        return True
