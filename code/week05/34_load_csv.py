import pandas as pd


filename = "SacramentocrimeJanuary2006.csv"
df = pd.read_csv(filename)

keys = df.keys()
print(keys)
print(df)

# count the number of rows
print(df.shape)
print(df['cdatetime'])