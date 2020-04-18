import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


filename = "tmdb_5000_movies.csv"
# read the file
df = pd.read_csv(filename, encoding='utf-8')

# create 'year' column using release_date column
# df['year'] = df['release_date']

df['year'] = df['release_date'].str.slice(0,4)
df['month'] = df['release_date'].str.slice(5,7)
df['day'] = df['release_date'].str.slice(8,10)

print(df['release_date'])
print(df['year'])
print(df['month'])
print(df['day'])
