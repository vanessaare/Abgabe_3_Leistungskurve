import matplotlib.pyplot as plt

from clean_data import lade_df_activity
from calc import berechne_power_curve


def plot_power_curve(zeitaufloesung=1):
    """
    Berechnet und plottet die Power Curve.
    """

    # 1. Daten laden
    df = lade_df_activity()

    power = df["PowerOriginal"]

    # 2. Power Curve berechnen
    curve_df = berechne_power_curve(
        power=power,
        zeitaufloesung=zeitaufloesung
    )

    # 3. Plot
    plt.figure(figsize=(10, 5))

    plt.plot(
        curve_df["Zeit_s"],
        curve_df["Leistung_W"],
        linewidth=2
    )

    plt.xlabel("Zeit [s]")
    plt.ylabel("Leistung [W]")
    plt.title("Power Curve")
    plt.grid(True)

    plt.tight_layout()
    plt.show()