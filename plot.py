import matplotlib.pyplot as plt


def plot_power_curve(df_power_curve):
    plt.figure(figsize=(10, 6))

    plt.plot(
        df_power_curve["Zeit_s"],
        df_power_curve["Leistung_W"]
    )

    plt.xscale("log")

    plt.xlabel("Zeit")
    plt.ylabel("Power [W]")
    plt.title("Power Curve")
    plt.grid(True, which="both")

    ticks = [5, 10, 20, 60, 300, 1800]
    labels = ["5 s", "10 s", "20 s", "1 min", "5 min", "30 min"]

    plt.xticks(ticks, labels)

    plt.show()
