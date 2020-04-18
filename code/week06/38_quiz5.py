import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


filename = "SacramentocrimeJanuary2006.csv"
df = pd.read_csv(filename)

# 1. plot only district 2 and 3 with legend
fig, ax = plt.subplots()
for i in range(2, 4):
    loc = df['district'] == i
    df_short = df[loc]
    ax.plot(df_short['longitude'], df_short['latitude'], '.', label=f"district{i}")
ax.legend()
plt.show()

# 2. count ncic codes for each district
df_list = []
for i in range(1, 7):
    loc = (df['district']==i)
    df_short = df[loc]
    cnts = df_short['ucr_ncic_code'].value_counts()
    df_list.append(cnts)

# 3. create dataframe where the keys are district and rows are ncic_codes
df_ncic = pd.concat(df_list, axis=1)
nan_loc = np.isnan(df_ncic)
df_ncic[nan_loc] = 0
print(df_ncic)