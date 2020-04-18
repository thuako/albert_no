import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


filename = "tmdb_5000_movies.csv"
# read the file
df = pd.read_csv(filename, encoding='utf-8')

# extract the movies with vote_count > 2000 and vote_average > 8
loc = df['vote_count'] > 2000
df_short = df[loc]
short_loc = df_short['vote_average'] > 8
df_tiny = df_short[short_loc]
print(df_tiny[['title', 'vote_count', 'vote_average']])

# plot vote_count vs vote_average
plt.plot(df['vote_count'], df['vote_average'], '.')
plt.show()
