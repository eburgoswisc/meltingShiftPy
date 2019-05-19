#!/usr/bin/env python3

import string
import pandas as pd

#from meltingShiftPy.utils import melting_shift, tm_calculate



def format_df(df): 
    """ Parses given dataframe and returns the averages of readings and temperature shift calculation."""
    # Iterables for alphabet letters
    alpha_iter = iter(list(string.ascii_uppercase))
    letter = next(alpha_iter)

    position = 1
    new_df = pd.DataFrame()
    for i in range(1,97):
        replicate = letter + str(position)
        # Grab a replicate
        sub_df = (df.loc[df["Well Position"] == replicate ]).set_index("Temperature")
        # Do once
        if i == 1:
            new_df["Reading"] = sub_df["Reading"]
        # Drop Reading column
        sub_df = sub_df.drop(columns="Reading")

        # Rename for sample specific
        sub_df = sub_df.rename(columns={c: f"{c}_{replicate}" for c in sub_df.columns})
        new_df = new_df.join(sub_df, how="right")

        position += 1
        # Increment letter after 12 wells
        if position > 12:
            letter = next(alpha_iter)
            position = 1



        # if len(replicates) == 3:
        #     output_average_df = qs7_averages(temp_df, output_average_df, replicates, temperature_df)
        #
        #     temp_df = pd.DataFrame()
        #     replicates = []

    return new_df


""" FOR DEVELOPMENT """

if __name__ == "__main__":
    # Import packages
    from averages import qs7_averages
    from utils import split_every
    import sys
    # Read in data
    df = pd.read_excel("../../data/2019-01-25_BinK_Thermofluor-PM1-a_copy.xls", sheet_name="Melt_Curve_Raw_Data")
    # Call format_df()
    formatted_df = format_df(df)

    print(qs7_averages(formatted_df))
