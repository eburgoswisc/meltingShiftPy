#!/usr/bin/env python3

import string
import pandas as pd

from meltingShiftPy.averages import get_averages
from meltingShiftPy.utils import melting_shift, tm_calculate

def format_df(df): 
    """ Parses given dataframe and returns the averages of readings and temperature shift calculation."""
    alphaiter = iter(list(string.ascii_uppercase))
    letter = next(alphaiter)

    temp_df = pd.DataFrame()

    position = 1
    replicates = []
    output_average_df = pd.DataFrame()
    temperature_df = pd.DataFrame()

    for i in range(1,97):
        replicates.append(f"{letter + str(position)}")

        sub_df = (df.loc[df["Well Position"] == letter + str(position) ]).set_index("Temperature")

        # Do once
        if i == 1:
            output_average_df["Readings"] = sub_df["Reading"]

        # Always rename
        sub_df = sub_df.rename(columns = { c: f"{c}_{letter + str(position)}" for c in sub_df.columns })

        temp_df = temp_df.join(sub_df, how="right")

        position += 1
        # Increment letter after 12 wells
        if position > 12:
            letter = next(alphaiter)
            position = 1

        if len(replicates) == 3:
            (output_average_df, temperature_df) = get_averages(temp_df, output_average_df, replicates, temperature_df)

            temp_df = pd.DataFrame()
            replicates = []


    ## Calculate tm_Shift

    temperature_df["Melting Temperature"] = temperature_df.apply(tm_calculate, axis=1)
    # This can be changed to select with arguments

    ## Grab control sample and calculate tm
    control = temperature_df.iloc[0,:]

    ## Apply melting_shift
    temperature_df["Melting Shift"] = temperature_df.apply(melting_shift, axis=1, args=[control])
    
    return (output_average_df, temperature_df)