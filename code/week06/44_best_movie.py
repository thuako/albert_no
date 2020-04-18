import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


filename = "tmdb_5000_movies.csv"
# read the file
df = pd.read_csv(filename, encoding='utf-8')

# Find the best vote_average movie
vote_count_idx = (df['vote_count'] > 1000)
df_short = df[vote_count_idx]
idx = df_short['vote_average'].idxmax()
print(df_short.loc[idx])

# Find the best vote_average Korean movie
idx_korean = df['original_language'] == 'ko'
df_korean = df[idx_korean]
print(df_korean)
idx_max = df_korean['vote_average'].idxmax()
print(df_korean.loc[idx_max])
