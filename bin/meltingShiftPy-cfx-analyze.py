#!/usr/bin/env python3

import argparse
import pandas as pd
import os

from meltingShiftPy import qPCR_Gourse

def main(args):
    try:
        # Check if directory was given
        if os.path.isdir(args.input):
            for f in os.listdir(args.input):
                if f.endswith(".csv"):
                    #Call average function
                    df = pd.read_csv(args.input, index=[0])
                    qPCR_Gourse(df, args.index)
                    pass
        # If csv file
        else:
            df = pd.read_csv(args.input)
    pass


if __name__ == "__main__":

    """ Parse command line arguments """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i", "--input", help="input csv file or directory with raw data", required=True
    )
    parser.add_argument(
        "-o", "--output", help="name for file output", required=True
    )
    parser.add_argument(
        "--index", help="index for control column", required=True
    )

    main(parser.parse_args())
