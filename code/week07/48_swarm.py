import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the data
filename = "tmdb_5000_movies.csv"

# read the file
df = pd.read_csv(filename, encoding='utf-8')
print(df.keys())

sns.swarmplot(x="vote_average", y="vote_count", data=df)
plt.xticks(rotation=40)
plt.show()