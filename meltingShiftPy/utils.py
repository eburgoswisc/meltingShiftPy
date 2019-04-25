#!/usr/bin/env python3

import pandas as pd

def tm_calculate(s: pd.Series) -> float:
    return (s["maxTemp"])/ ( 2 * (s["maxTemp"] - s["minTemp"]) )

def melting_shift(sample:pd.Series, control=pd.Series):
    return (sample["Melting Temperature"] - control["Melting Temperature"]) >= 1

def write_output(df, out_file, suffix="", sep=","):
    df.to_csv(f"{out_file}{suffix}.csv", sep=sep)
    return