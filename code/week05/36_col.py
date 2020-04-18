import pandas as pd


filename = "SacramentocrimeJanuary2006.csv"
df = pd.read_csv(filename)

key_of_interest = ['district', 'latitude', 'longitude']
df_short = df[key_of_interest]

print(df_short)

# category of crime
print(df['ucr_ncic_code'])
print(df['latitude'].mean())

# find ncic codes that appeared more than three times in the database
cnts = df['ucr_ncic_code'].value_counts()
loc = cnts > 2
print(cnts[loc])
