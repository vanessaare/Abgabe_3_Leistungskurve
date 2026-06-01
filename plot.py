import matplotlib.pyplot as plt

def plot_power_curve(curve_df):
    plt.figure(figsize=(10, 5))

    plt.plot(
        curve_df["Zeit_s"],
        curve_df["Leistung_W"],
        linewidth=2
    )

    plt.xscale("log")
    plt.xlim(1, 1800)

    ticks = [1, 5, 10, 20, 60, 300, 1200, 1800]
    labels = ["1 s", "5 s", "10 s", "20 s", "1 min", "5 min", "20 min", "30 min"] 

    plt.xticks(ticks, labels)

    plt.xlabel("Zeit")
    plt.ylabel("Leistung [W]")
    plt.title("Power Curve")
    plt.grid(True)

    plt.tight_layout()
    plt.show()