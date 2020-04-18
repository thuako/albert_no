import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


filename = "tmdb_5000_movies.csv"
# read the file
df = pd.read_csv(filename, encoding='utf-8')

keys = df.keys()
print(keys)
print(df.shape)

print(df[['vote_count', 'vote_average']])



