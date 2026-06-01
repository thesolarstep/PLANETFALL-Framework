import os

class BinaryTribunal:
    def __init__(self, out_dir):
        self.out_dir = out_dir

    def run(self, candidate, casefile_dir, context_data=None):
        print(f"[BINARY TRIBUNAL] Analyzing evidence for TIC {candidate['TIC_ID']}...")

        suspicion_score = 0
        reasons = []

        # 1. Transit Depth Scoring (Revised)
        depth = candidate['depth']
        if depth > 0.10:
            suspicion_score += 20
            reasons.append(f"Excessive transit depth ({depth*100:.1f}%): +20 points")
        elif depth > 0.03:
            suspicion_score += 10
            reasons.append(f"Significant transit depth ({depth*100:.1f}%): +10 points")

        # 2. Mocking other evidence tests for calibration (derived from context if available)
        # In a full integration, these would come from signal_integrity or contamination modules
        if context_data:
            if context_data.get('odd_even_mismatch'):
                suspicion_score += 40
                reasons.append("Odd-even depth mismatch detected: +40 points")
            if context_data.get('secondary_eclipse'):
                suspicion_score += 50
                reasons.append("Secondary eclipse signature found: +50 points")
            if context_data.get('centroid_motion'):
                suspicion_score += 35
                reasons.append("Significant centroid motion: +35 points")

        # Verdict logic
        if suspicion_score < 30:
            verdict = "PASS"
        elif suspicion_score <= 60:
            verdict = "SUSPICIOUS"
        else:
            verdict = "EXECUTED"

        with open(os.path.join(casefile_dir, 'binary_tribunal.md'), 'w') as f:
            f.write(f"# Binary Tribunal: TIC {candidate['TIC_ID']}\\n")
            f.write(f"**Suspicion Score: {suspicion_score}**\\n")
            f.write(f"**Final Verdict: {verdict}**\\n\\n")
            f.write("## Evidence Log:\\n")
            for reason in reasons:
                f.write(f"- {reason}\\n")
            if not reasons:
                f.write("- No significant suspicion indicators detected.\\n")

        return verdict, suspicion_score, reasons

