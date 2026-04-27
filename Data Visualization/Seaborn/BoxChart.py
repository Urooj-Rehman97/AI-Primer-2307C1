import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# data = [10,20,30,40,50,100]
# sns.boxplot(data= data)
# plt.show()

data = {
    "Marks" : [90,67,76,89,-1]
}

df = pd.DataFrame(data)

sns.boxplot(x=df["Marks"])
plt.show()