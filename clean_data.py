import pandas as pd

def lade_df_activity():
    return pd.read_csv("data/activity.csv", skipinitialspace=True)


def clean_df_activity(df_activity):
    return df_activity.dropna(subset=["PowerOriginal"])