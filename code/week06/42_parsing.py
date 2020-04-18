import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


filename = "tmdb_5000_movies.csv"
# read the file
# df = pd.read_csv(filename, parse_dates=['release_date'])
df = pd.read_csv(filename, encoding='utf-8', parse_dates=['release_date'])
df['year'] = df['release_date'].dt.year
df['month'] = df['release_date'].dt.month
df['day'] = df['release_date'].dt.day

# create 'year' column using release_date column
print(df['day'])
