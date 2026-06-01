import pandas as pd


def lade_df_activity():
    """
    Lädt activity.csv-Datei und entfernt Zeilen ohne PowerOriginal.
    """

    df = pd.read_csv("data/activity.csv", skipinitialspace=True)



def clean_df_activity():
    df = df.dropna(subset=["PowerOriginal"])

    df["Time"] = range(len(df))

    return df
    