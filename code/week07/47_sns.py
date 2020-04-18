import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the data
filename = "tmdb_5000_movies.csv"

# read the file
df = pd.read_csv(filename, encoding='utf-8')

# Create violin plot
sns.violinplot(x="vote_average", data=df)

# Show the plot
plt.show()