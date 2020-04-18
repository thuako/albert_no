import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the data
filename = "tmdb_5000_movies.csv"
df = pd.read_csv(filename, encoding='utf-8', parse_dates=['release_date'])

# Using FacetGrid draw scatter plots vote_average vs vote_count for 80's, 90's, 00's, and 10's
df['year'] = df['release_date'].dt.year
df = df.dropna()
df = df[df['year']>1980]
df['decade'] = (df['year'].astype(int) // 10) * 10

g = sns.FacetGrid(df, col="decade", margin_titles=True)
g.map(plt.scatter, "vote_average", "vote_count")
g.set(xlim=(0, 10), xticks=[1, 3, 5, 7, 9])

# Show plot
plt.show()
