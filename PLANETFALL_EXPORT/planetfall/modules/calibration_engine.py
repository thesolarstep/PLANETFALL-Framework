import pandas as pd
import os

class CalibrationEngine:
    def __init__(self, out_dir):
        self.out_dir = out_dir

    def run(self, results_df):
        print("[CALIBRATION] Computing performance metrics...")
        
        # results_df should have 'verdict' and 'label' (Confirmed, False Positive)
        # Mapping verdict to binary discovery
        results_df['discovered'] = results_df['verdict'].apply(lambda x: 1 if x != 'EXECUTED' else 0)
        results_df['is_planet'] = results_df['label'].apply(lambda x: 1 if x == 'Confirmed' else 0)
        
        tp = len(results_df[(results_df['discovered'] == 1) & (results_df['is_planet'] == 1)])
        fp = len(results_df[(results_df['discovered'] == 1) & (results_df['is_planet'] == 0)])
        tn = len(results_df[(results_df['discovered'] == 0) & (results_df['is_planet'] == 0)])
        fn = len(results_df[(results_df['discovered'] == 0) & (results_df['is_planet'] == 1)])
        
        tpr = tp / (tp + fn) if (tp + fn) > 0 else 0
        fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tpr
        
        with open(os.path.join(self.out_dir, 'calibration_report.md'), 'w') as f:
            f.write("# Calibration Report\\n\\n")
            f.write(f"- True Positive Rate: {tpr:.2f}\\n")
            f.write(f"- False Positive Rate: {fpr:.2f}\\n")
            f.write(f"- Precision: {precision:.2f}\\n")
            f.write(f"- Recall: {recall:.2f}\\n\\n")
            f.write("## Confusion Matrix\\n")
            f.write(f"| | Predicted Planet | Predicted False Positive |\\n")
            f.write(f"|---|---|---|\\n")
            f.write(f"| Actual Planet | {tp} (TP) | {fn} (FN) |\\n")
            f.write(f"| Actual False Positive | {fp} (FP) | {tn} (TN) |\\n")
            
        print(f"[CALIBRATION] Report generated: {os.path.join(self.out_dir, 'calibration_report.md')}")
        return {
            "TPR": tpr,
            "FPR": fpr,
            "Precision": precision,
            "Recall": recall
        }
