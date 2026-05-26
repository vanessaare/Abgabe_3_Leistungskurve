def berechne_power_curve(power, dt=1):
    """
    Berechnet die Power-Curve aus Leistungsdaten.

    Args:
        power: pd.Series oder np.array mit Leistungswerten in Watt
        dt: zeitlicher Abstand zwischen zwei Messpunkten in Sekunden

    Returns:
        pd.DataFrame mit Zeit in Sekunden und maximaler Durchschnittsleistung
    """

    power = pd.Series(power).dropna().reset_index(drop=True)

    ergebnisse = []

    max_fenster = len(power)

    for fenster in range(1, max_fenster + 1):
        dauer = fenster * dt

        gleitender_mittelwert = power.rolling(window=fenster).mean()

        max_power = gleitender_mittelwert.max()

        ergebnisse.append({
            "Zeit_s": dauer,
            "Leistung_W": max_power
        })

    df_power_curve = pd.DataFrame(ergebnisse)

    return df_power_curve 