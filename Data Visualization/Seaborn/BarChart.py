import matplotlib.pyplot as plt
import seaborn as sns

products = ["Skin Care", "Herbals", "Home Appliances","Electornics"]
sales = [56,78,34,50]
sns.barplot(x=products, y=sales)
sns.set_style("darkgrid")
plt.show()