import pandas as pd
data = {
    "Name": ["Abc", "Xyz", "Mno", "Pqr"],
    "Marks": [67,89,87,65]
}

df = pd.DataFrame(data)
print(df)

dt = pd.read_csv("example.csv")
print(dt)
#Access single Column
print(dt["Marks"])
#Pandas Built method to read data
print("---------- First 5 Students Data ---------------")
print(dt.head())
print("---------- Last 5 Students Data ---------------")
print(dt.tail())
print("---------- Structure of example.csv ---------------")
print(dt.info())
print("---------- Nu8merical Data Summary ---------------")
print(dt.describe())

print("Total Marks: ",dt["Marks"].sum())
print("Maximum Marks: ",dt["Marks"].max())
print("Minimum Marks: ",dt["Marks"].min())
