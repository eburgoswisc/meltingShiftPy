#!/usr/bin/env python3

import pandas as pd

def qs7_averages(df, averages_df, replicates:list, tm_df):
    name_set = f"{str( replicates[0])}_{str( replicates[-1])}"

    flourescence_df = pd.DataFrame()
    derivative_df = pd.DataFrame()
    for rep in replicates:
        # For Fluorescence
        flourescence_df[f"Fluorescence_{rep}"] = (df[f"Fluorescence_{rep}"])
        # For Derivatives
        derivative_df[f"Derivative_{rep}"] = (df[f"Derivative_{rep}"])
    
    ## Get temperatures
    flourescence_mean_df = flourescence_df.mean(axis=1)
    maxTemp = flourescence_mean_df[flourescence_mean_df.max() == flourescence_mean_df].index[0]
    ## Split dataframe
    lower_split = flourescence_mean_df[flourescence_mean_df.index < maxTemp]
    minTemp = lower_split[lower_split.min() == lower_split].index[0]
    
    ## Calculate tm and store
    tm_row = pd.DataFrame(data={"Sample": [name_set], "minTemp": [minTemp], "maxTemp": [maxTemp]})
    tm_df = tm_df.append(tm_row)

    averages_df[f"Flourescence_{name_set}"] = flourescence_df.mean(axis=1)
    averages_df[f"Derivative_{name_set}"] = derivative_df.mean(axis=1)
    
    return [averages_df, tm_df]