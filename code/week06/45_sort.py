import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


filename = "tmdb_5000_movies.csv"
# read the file
df = pd.read_csv(filename, encoding='utf-8')

# sort by vote_average
df.sort_values(by='vote_average', inplace=True)
print(df[['original_title', 'vote_average']])
