import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


filename = "tmdb_5000_movies.csv"
# read the file
df = pd.read_csv(filename, encoding='utf8')

# plot popularity vs vote_average for rows with popularity < 200 and vote_count > 100
df_short = df[df['popularity']<200]
df_tiny = df_short[df_short['vote_count']>100]
plt.plot(df_tiny['popularity'], df_tiny['vote_average'], 'b.')

# count the number of japanese movie
df_japan = df[df['original_language']=='ja']
print(df_japan.shape[0])

# create a column that computes profit = revenue - budget
# then sort dataframe according to profit
df['profit'] = df['revenue'] - df['budget']
df.sort_values('profit', inplace=True, ascending=False)
print(df['title'])
keys = ['title', 'profit']
print(df[keys])

plt.show()
