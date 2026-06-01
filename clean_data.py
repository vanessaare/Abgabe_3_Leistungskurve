import pandas as pd

def lade_df_activity():
    """
    Lädt activity.csv-Datei
    """
    df_activity = pd.read_csv("data/activity.csv", skipinitialspace=True)
    df_activity["Time"] = df_activity.index
    return df_activity


def entferne_leere_werte(df):
    """
    Entfernt alle Zeilen ohne PowerOriginal
    """
    df_activity = df.dropna(subset=["PowerOriginal"])
    return df_activity
    