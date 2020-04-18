import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


filename = "tmdb_5000_movies.csv"
# read the file
df = pd.read_csv(filename, encoding='utf-8', parse_dates=['release_date'])

# plot vote_count vs vote_average
plt.plot(df['vote_count'], df['vote_average'], '.')
plt.show()

# NOTE: need to extract year first (check file 4,5)
# plot year vs vote_average
df['year'] = df['release_date'].dt.year
plt.plot(df['year'], df['vote_average'], '.')
plt.show()

# plot year vs revenue
plt.plot(df['year'], df['revenue'], '.')
plt.show()
