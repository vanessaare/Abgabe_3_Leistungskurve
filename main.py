from calc import berechne_power_curve
from plot import plot_power_curve


if __name__ == "__main__":
    curve_df = berechne_power_curve()
    plot_power_curve(curve_df)