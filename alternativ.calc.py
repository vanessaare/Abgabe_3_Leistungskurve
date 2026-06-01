import pandas as pd


def calculate_power_curve(df, power_col="power", time_col=None):
    """
    Berechnet die Leistungskurve aus den Leistungsdaten.
    
    Parameters:
    - df: DataFrame mit den Leistungsdaten
    - power_col: Name der Spalte mit den Leistungswerten
    - time_col: Name der Spalte mit den Zeitstempeln (optional)
    
    Returns:
    - DataFrame mit den berechneten Leistungskurvenwerten
    """
    
    if time_col is not None:
        df = df.sort_values(by=time_col).reset_index(drop=True)
    
    power_values = df[power_col].values
    n = len(power_values)
    
    results = []
    
    for window_size in range(1, n + 1):
        rolling_mean = pd.Series(power_values).rolling(window=window_size).mean().dropna()
        
        if len(rolling_mean) == 0:
            continue
        
        max_power = rolling_mean.max()
        results.append({"Zeit_s": window_size, "Leistung_W": max_power})
    
    return pd.DataFrame(results)