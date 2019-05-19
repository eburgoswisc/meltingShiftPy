#!/usr/bin/env python3

import pandas as pd
from itertools import islice


def write_output(df, out_file, suffix="", sep=","):
    df.to_csv(f"{out_file}{suffix}.csv", sep=sep)
    return


def split_every(n: int, iterable: iter) -> iter:
    i = iter(iterable)
    piece = list(islice(i, n))
    while piece:
        yield piece
        piece = list(islice(i, n))