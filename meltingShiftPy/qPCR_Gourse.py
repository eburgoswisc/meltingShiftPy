import argparse, os
import pandas as pd


def parse():
    parser = argparse.ArgumentParser(
        description="Take averages of replicates in data table and make scatter plots"
    )
    parser.add_argument("-i", "--input", help="Input file with data.")

    parser.add_argument("-o", "--output", help="Output file for writing results.")

    parser.add_argument("--control", help="Control column of experiment")

    parser.add_argument("-r", "--replicates", help="Number of replicate in table.")

    parser.add_argument("--blank", help="Blank column in table")

    return parser.parse_args()


def calculate(df):
    return pd.Series(df.mean(axis=1), name=df.columns[0])


def get_averages(df, control):

    results_df = pd.DataFrame()

    # Find control columns and take average
    control_rep = []
    for col in df:

        if col.split(".")[0] == str(control):
            control_rep.append(col)

    control_avg = calculate(df[control_rep])

    df = df.drop(labels=control_rep, axis=1)

    rep = []
    for col in df:
        rep.append(col)
        if (len(rep) != 1) and (rep[-1].split(".")[0] != rep[-2]):
            results_df[rep[0]] = calculate(df[rep])
            rep = []
    # Take the difference with control from each sample
    results_df = results_df - results_df.iloc[:, control]

    return results_df


def main():
    args = parse()
    get_averages(args)
    return


if __name__ == "__main__":
    main()
