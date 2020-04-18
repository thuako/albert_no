import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


filename = "SacramentocrimeJanuary2006.csv"
df = pd.read_csv(filename)

# which district has the largest number of crimes?

# the following shows the map of crimes
plt.plot(df['longitude'], df['latitude'], '.')
plt.show()

for i in range(1, 7):
    loc = df['district'] == i
    df_short = df[loc]
    plt.plot(df_short['longitude'], df_short['latitude'], '.')
plt.show()

