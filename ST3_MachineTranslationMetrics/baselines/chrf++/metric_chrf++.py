import argparse
import sacrebleu
import pandas as pd



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str, help="CSV file containing the columns 'Reference Translation' and 'Candidate Translation'")
    parser.add_argument('--output', type=str, help="path of the output file", default="chrf++-scores.txt")
    args = parser.parse_args()

    df = pd.read_csv(args.file_path) 
    
    
    refs = df['Reference Translation']
    hyps = df['Candidate Translation']

    scores = []

    chrf_metric = sacrebleu.metrics.CHRF(word_order=2) ## ChrF++

    for ref, hyp in zip(refs, hyps):
        scores.append(chrf_metric.sentence_score(hyp, [ref]).score)

    with open(args.output, "w") as file:
        file.write("\n".join([str(x) for x in scores]))


