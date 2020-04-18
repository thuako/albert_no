import pandas as pd


filename = "SacramentocrimeJanuary2006.csv"
df = pd.read_csv(filename)

loc = (df['district'] == 3)
print(df[loc])
print(df.size)
print(df[loc].size)

# find the number of rows that latitude > 38.5
loc = (df['latitude'] > 38.5)
print(df[loc])
print(df[loc].size)

# which district has the largest number of crimes?
for i in range(1, 7):
    loc = (df['district'] == i)
    df_short_shape = df[loc].shape
    num = df_short_shape[0]
    print(f"district {i} : {num}")
