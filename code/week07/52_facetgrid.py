import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
titanic = sns.load_dataset("titanic")
titanic.dropna()
print(titanic.keys())

# Create violin plots
g = sns.FacetGrid(titanic, col="survived", row="who", margin_titles=True)
g.map(sns.violinplot, "pclass", "age")

# Show the plot
plt.show()
