import pandas as pd

from clean_data import lade_df_activity, entferne_leere_werte
 
 
def berechne_power_curve(val_col="PowerOriginal", intervals=[5, 10, 20, 60, 300, 1800]):
    results = []
    df_activity = lade_df_activity()
    df_activity = entferne_leere_werte(df_activity)
    for seconds in intervals:
        if len(df_activity) >= seconds:
            max_avg = df_activity[val_col].fillna(0).rolling(window=seconds).mean().max()
            results.append({
                "Intervall": f"{seconds}s" if seconds < 60 else f"{seconds // 60}min",
                "Zeit_s": seconds,
                "Leistung_W": round(max_avg, 2),
            })
    return pd.DataFrame(results)

