import pandas as pd
from find_peaks import find_peaks

def berechne_power_curve(power, zeitaufloesung=1):
    """
    Berechnet die Power-Curve aus Leistungsdaten.    
    """

    power = pd.Series(power).reset_index(drop=True)

    ergebnisse = []

    for fensterbreite in range(1, len(power) + 1):

        dauer_s = fensterbreite * zeitaufloesung

        mittelwerte = power.rolling(
            window=fensterbreite,
            min_periods=fensterbreite
        ).mean()

        mittelwerte = mittelwerte.dropna()

        if len(mittelwerte) == 0:
            continue

        threshold = mittelwerte.mean()

        peaks = find_peaks(
            series=mittelwerte,
            threshold=threshold,
            respacing_factor=5
        )

        if len(peaks) > 0:
            max_leistung = mittelwerte.loc[peaks].max()
        else:
            max_leistung = mittelwerte.max()

        ergebnisse.append({
            "Zeit_s": dauer_s,
            "Leistung_W": max_leistung
        })

    df_power_curve = pd.DataFrame(ergebnisse)

    return df_power_curve