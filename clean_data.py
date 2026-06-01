import pandas as pd


def lade_df_activity():
    """
    Lädt activity.csv-Datei und entfernt Zeilen ohne PowerOriginal.
    """

    df_activity = pd.read_csv("data/activity.csv", skipinitialspace=True)

    df_activity = df_activity.dropna(subset=["PowerOriginal"])

    df_activity["Time"] = range(len(df_activity))

    return df_activity
    