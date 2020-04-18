import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


filename = "tmdb_5000_movies.csv"
# read the file
df = pd.read_csv(filename, encoding='utf8')

# 1. plot popularity vs vote_average for rows with popularity < 200 and vote_count > 100

# 2. count the number of japanese movie

# 3. create a column that computes profit = revenue - budget
# then sort dataframe according to profit
