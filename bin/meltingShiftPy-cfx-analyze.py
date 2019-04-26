#!/usr/bin/env python3

import argparse
import pandas as pd
import os
import sys

from meltingShiftPy.qPCR_Gourse import single_cfx_averages, mult_cfx_averages
from meltingShiftPy.utils import write_output

""" Script use to analyze data from cfx qPCR machine in the Gourse Lab"""
def main(args):
    df = pd.DataFrame()
    # To store dataframes
    list_df = list()
    try:
        # Check if directory was given
        if os.path.isdir(args.input):
            for f in os.listdir(args.input):
                if f.endswith(".csv"):
                    list_df.append(pd.read_csv(str(args.input + f), index_col=[0]))

        # If a csv
        else:
            df = pd.read_csv(args.input)
    except ValueError as e:
        print(f"Exception thrown: {str(e)}")

    # Calculate Averages
    if list_df:
        df = mult_cfx_averages(list_df)
        write_output(df, args.output)
    else:
        df = single_cfx_averages(df)
        write_output(df, args.output)

    print(f"Job is done")


if __name__ == "__main__":

    """ Parse command line arguments """
    parser = argparse.ArgumentParser(description="Python script for parsing and analyzing data from CFX qPCR machine.")

    parser.add_argument(
        "-i", "--input", help="input csv file or directory with raw data", required=True
    )
    parser.add_argument(
        "-o", "--output", help="name for file output", required=True
    )
    parser.add_argument(
        "--index_control", help="index for control column", required=True
    )

    main(parser.parse_args())
