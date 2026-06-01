import pandas as pd

def lade_df_activity():
    df_activity = pd.read_csv("data/activity.csv", skipinitialspace=True)
    df_activity["Time"] = df_activity.index


    df_activity["PowerOriginal"] = df_activity["PowerOriginal"].fillna(0)
    
    return df_activity
    