import pandas as pd

from clean_data import lade_df_activity, clean_df_activity


def berechne_power_curve(val_col="PowerOriginal"):
    results = []

    df_activity = lade_df_activity()
    df_activity = clean_df_activity(df_activity)

    max_dauer = min(len(df_activity), 1800)

    intervals = range(1, max_dauer + 1)

    for seconds in intervals:
        max_avg = df_activity[val_col].rolling(window=seconds).mean().max()

        results.append({
            "Intervall": f"{seconds}s" if seconds < 60 else f"{seconds // 60}min",
            "Zeit_s": seconds,
            "Leistung_W": round(max_avg, 2),
        })

    return pd.DataFrame(results)