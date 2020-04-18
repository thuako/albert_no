import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the data
filename = "tmdb_5000_movies.csv"
df = pd.read_csv(filename, encoding='utf-8', parse_dates=['release_date'])

# Using FacetGrid draw scatter plots "vote_average" vs "vote_count" for 80's, 90's, 00's, and 10's

# Show plot
plt.show()
