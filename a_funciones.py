import pandas as pd


def info_columns(df):
    for i in df.columns:
        print(i, df[i].unique())

