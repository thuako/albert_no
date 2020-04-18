import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset("iris")

g = sns.pairplot(iris)
g = sns.pairplot(iris, hue='species')
g = sns.pairplot(iris, kind="reg", hue="species")

plt.show()
