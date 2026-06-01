import os
import json

class Tribunal:
    def __init__(self, out_dir):
        self.out_dir = out_dir

    def run(self, candidate, casefile_dir, binary_data):
        verdict, score, reasons = binary_data
        cid = candidate['TIC_ID']
        print(f"[TRIBUNAL] Convening court for TIC {cid}...")

        # PROSECUTOR ARGUMENT
        prosecutor = f"Prosecutor argues for EXECUTION based on a suspicion score of {score}. "
        if reasons:
            prosecutor += "Key concerns include: " + "; ".join(reasons) + "."
        else:
            prosecutor += "No specific red flags, but system remains conservative."

        # DEFENSE ARGUMENT
        defense = f"Defense argues for PASS. Candidate shows stable SNR and period {candidate['period']} days. "
        if score < 60:
            defense += "The suspicion is not conclusive; nature prefers planetary solutions at this scale."
        else:
            defense += "Despite the score, the signal remains periodic and could be a large planet or grazing eclipse."

        # JUDGE VERDICT
        judge_comment = f"Final judgment: {verdict}. Confidence estimate: {1.0 - (score/150.0):.2f}."

        with open(os.path.join(casefile_dir, 'tribunal_report.md'), 'w') as f:
            f.write(f"# Tribunal Report: TIC {cid}\\n\\n")
            f.write("## PROSECUTION\\n" + prosecutor + "\\n\\n")
            f.write("## DEFENSE\\n" + defense + "\\n\\n")
            f.write("## JUDGE\\n" + judge_comment + "\\n")

        if verdict == "EXECUTED":
            self._write_why_executed(casefile_dir, cid, score, reasons, judge_comment)
        else:
            self._write_why_not_executed(casefile_dir, cid, score, judge_comment)

        with open(os.path.join(casefile_dir, 'final_verdict.json'), 'w') as f:
            json.dump({
                "verdict": verdict,
                "score": score,
                "confidence": 1.0 - (score/150.0)
            }, f, indent=4)

        return verdict

    def _write_why_executed(self, casefile_dir, cid, score, reasons, judge_comment):
        with open(os.path.join(casefile_dir, 'WHY_EXECUTED.md'), 'w') as f:
            f.write(f"# WHY EXECUTED: TIC {cid}\\n\\n")
            f.write(f"## Evidence for Rejection\\nTotal Suspicion Score: {score}\\n")
            f.write("### Module Contributions:\\n")
            for r in reasons:
                f.write(f"- {r}\\n")
            f.write(f"\\n## Confidence Estimate\\n{judge_comment}\\n\\n")
            f.write("## Alternative Explanations\\nLikely an eclipsing binary or background blend.\\n")

    def _write_why_not_executed(self, casefile_dir, cid, score, judge_comment):
        with open(os.path.join(casefile_dir, 'WHY_NOT_EXECUTED.md'), 'w') as f:
            f.write(f"# WHY NOT EXECUTED: TIC {cid}\\n\\n")
            f.write(f"## Reasons it Survived\\nSuspicion score {score} remains below execution threshold.\\n")
            f.write(f"## Remaining Uncertainties\\n{judge_comment}\\n\\n")
            f.write("## Required Follow-up\\nGround-based radial velocity or high-resolution imaging.\\n")
            f.write("## Estimated Planet Likelihood\\nModerate to High.\\n")

