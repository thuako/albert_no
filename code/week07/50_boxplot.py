import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the data
filename = "tmdb_5000_movies.csv"

# read the file
df = pd.read_csv(filename, encoding='utf-8', parse_dates=['release_date'])
df['year'] = df['release_date'].dt.year
df = df.dropna()
df['decade'] = (df['year'].astype(int) // 10) * 10
print(df.keys())

# boxplot
sns.boxplot(x="decade", y="budget", data=df)

# pairplot
sns.pairplot(df, vars=['year', 'budget', 'popularity', 'vote_count', 'vote_average'])

# Show plot
plt.show()
