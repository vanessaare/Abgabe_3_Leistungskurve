#from clean_data import lade_df_activity
from calc import berechne_power_curve
from plot import plot_power_curve

df_power_curve = berechne_power_curve()
plot_power_curve(df_power_curve)
