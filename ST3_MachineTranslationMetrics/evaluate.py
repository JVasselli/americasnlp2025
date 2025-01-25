from scipy.stats import spearmanr
import argparse


def calculate_score_report(sys, ref):
    correlation, p_value = spearmanr(ref, sys)
    print(f"Spearman Correlation: {correlation:}")

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--metric_output', '--sys', type=str, help='File with each line-by-line metric score')
    parser.add_argument('--gold_reference', '--ref', type=str, help='File with corresponding line-by-line annotated scores')
    args = parser.parse_args()

    gold_lines = []
    with open(args.gold_reference, 'r') as f:
        for i, line in enumerate(f):
            gold_lines.append(float(line.strip()))

    metric_lines = []
    with open(args.metric_output, 'r') as f:
        for i,line in enumerate(f):
            metric_lines.append(float(line.strip()))

    assert len(metric_lines) == len(gold_lines)
    calculate_score_report(metric_lines, gold_lines)