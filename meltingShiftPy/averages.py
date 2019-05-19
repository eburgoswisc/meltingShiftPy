#!/usr/bin/env python3

""" This script is used to calculate averages of replicates from results. """

import pandas as pd
import string
import os
import traceback

from meltingShiftPy.utils import split_every
from meltingShiftPy.format import format_df


def qs7_averages(df: pd.DataFrame) -> pd.DataFrame:
    """ Take averages of qs7 results """
    # Grab fluorescence values
    fluorescence_df = df.loc[:, [c for c in df.columns if c.split("_")[0] == "Fluorescence"]]
    fluorescence_mean_df = pd.DataFrame(index=df.index)

    # Every three replicates, take the average
    for rep in split_every(3, fluorescence_df):
        set_name = "Fluorescence_" + rep[0].split("_")[1] + "_" +  rep[2].split("_")[1]
        fluorescence_mean_df[set_name] = fluorescence_df[rep].mean(axis=1)
    # Grab derivative values
    derivative_df = df.loc[:, [c for c in df.columns if c.split("_")[0] == "Derivative"]]
    derivative_mean_df = pd.DataFrame(index=df.index)
    # Every three replicates, take the average
    for rep in split_every(3, derivative_df):
        set_name = "Derivative_" + rep[0].split("_")[1] + "_" + rep[2].split("_")[1]
        derivative_mean_df[set_name] = derivative_df[rep].mean(axis=1)
    # TODO: Join both dataframes
    return fluorescence_mean_df, derivative_mean_df

# TODO: Remove, completely unnecessary
def calculate(df: pd.DataFrame, names: list) -> pd.DataFrame:
    """ Returns mean of given DataFrame """
    return pd.DataFrame(df.mean(axis=1), columns=[names], index=df.index)


def single_cfx_averages(df: pd.DataFrame) -> pd.DataFrame:
    """ Take averages of a single DataFrame with three replicates"""
    result_df = pd.DataFrame(index=df.index)
    # For every three replicates, take average
    for rep in split_every(3, df.columns):
        name = rep[0]
        result_df[name] = df.loc[:, rep].mean(axis=1)
    return result_df


def mult_cfx_averages(list_df: list) -> pd.DataFrame:
    """ Take averages of multiple DataFrames where index in each column is replicate"""
    result_df = pd.DataFrame(index=list_df[0].index)
    # Loop through index of columns
    j = 0
    for i in range(len(list_df[0].columns)):
        replicate_df = pd.DataFrame(index=list_df[0].index)
        # Loop through each DataFrame
        for df in list_df:
            # j is int suffix, append to replicate DataFrame
            j += 1
            replicate_df = replicate_df.join(df.iloc[:,i], rsuffix=j)
        # Reset suffix, add mean to results df
        j = 0
        result_df[replicate_df.columns[0]] = replicate_df.mean(axis=1)
        replicate_df = pd.DataFrame(index=list_df[0].index)
    return result_df


def get_tm(f_mean_df: pd.DataFrame, control: int) -> pd.DataFrame:
    """ Calculate tm from average fluorescence values. """
    # Grab control name
    control_tm = f_mean_df.iloc[:, control].name
    result_df = pd.DataFrame()
    # Calculate tm
    for col in f_mean_df:
        # Grab series and name
        s = f_mean_df[col]
        name = s.name
        try:
            # Grab max fluorescence temperature
            max_temp = s.index[s == s.max()][0]
            # Split before max temp and find min temp
            lower_split = s[s.index < max_temp]
            min_temp = lower_split.index[lower_split == lower_split.min()][0]
            # Calculate melting tm
            melt_tm = (max_temp - 1) / (2 * (max_temp - min_temp))
            if control_tm == name:
                control_tm = melt_tm
            # Calculate melting shift
            melt_shift = melt_tm - control_tm
            # Add to results DataFrame
            result_df = result_df.append({"Sample": name, "Max Temperature": max_temp, "Min Temperature": min_temp, "Tm": melt_tm, "Melting Shift": melt_shift}, ignore_index=True)
        # If exception occurs, print sample with problem.
        except IndexError:
            print(f"Sample: {name} had a max temperature of {max_temp}")
            #traceback.print_exc()
            pass
    # Re-organize columns
    result_df = result_df[["Sample", "Max Temperature", "Min Temperature", "Tm", "Melting Shift"]]
    return result_df

""" DEVELOPMENT """
if __name__ == "__main__":

    # df = single_cfx_averages(pd.read_csv("../../data/2018-11-27_Melt-Curve_BinK_Melt_Curve_RFU_Results_FRET.csv",
    #                                      index_col=[0]))
    # print(df.dtypes)
    #ht6_df = pd.read_csv("../../output/HT6Bink_averages.csv", index_col=[0])
    #get_tm(ht6_df, 0).to_csv("test.csv")

    # Test qs7_averages
    df = format_df(pd.read_excel("../../data/2019-01-25_BinK_Thermofluor-PM1-a.xls", sheet_name="Melt Curve Raw Data"))
