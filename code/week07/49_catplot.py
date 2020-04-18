import matplotlib.pyplot as plt
import seaborn as sns

# Load data
titanic = sns.load_dataset("titanic")
print(titanic.keys())

# Set up a catplot
sns.catplot("class", "age", "who", data=titanic)
sns.catplot("class", "age", "who", data=titanic, kind='violin')
sns.catplot("class", "survived", "who", data=titanic, kind='bar')

# Show plot
plt.show()