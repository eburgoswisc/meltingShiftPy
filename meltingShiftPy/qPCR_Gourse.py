#!/usr/bin/env python3

import pandas as pd
import string
import os

from itertools import islice

def split_every(n, iterable):
    i = iter(iterable)
    piece = list(islice(i, n))
    while piece:
        yield piece
        piece = list(islice(i, n))

def calculate(df, name):
    """ Returns mean of given dataframe """
    return pd.DataFrame(df.mean(axis=1), columns=[name], index=df.index)


def single_cfx_averages(df: pd.DataFrame):
    # Setup
    alpha = iter(string.ascii_uppercase)
    result_df = pd.DataFrame(index=df.index)
    i = 1
    for rep in split_every(3, df.columns[1:]):
        try:
            name = f"{next(alpha)}{i}"
            result_df = result_df.join(calculate(df[rep], name))
        except StopIteration:
            i += 1
            alpha = iter(string.ascii_uppercase)
            name = f"{next(alpha)}{i}"
            result_df = result_df.join(calculate(df[rep], name))
    return



def mult_cfx_averages(list_df):
    """ Take averages of multiple dataframes where index in each column is replicate"""
    result_df = pd.DataFrame(index=list_df[0].index)
    # Loop through index of columns
    j = 0
    for i in range(len(list_df[0].columns)):
        replicate_df = pd.DataFrame(index=list_df[0].index)
        # Loop through each dataframe
        for df in list_df:
            # j is int suffix, append to replicate dataframe
            j += 1
            replicate_df = replicate_df.join(df.iloc[:,i], rsuffix=j)
        # Reset suffix, add mea to results df
        j = 0
        result_df[replicate_df.columns[0]] = replicate_df.mean(axis=1)
        replicate_df = pd.DataFrame(index=list_df[0].index)
    return result_df







""" DEVELOPMENT """
if __name__ == "__main__":
    single_cfx_averages(pd.read_csv("../../raw/2018-11-27_Melt-Curve_BinK_Melt_Curve_RFU_Results_FRET.csv"))
