import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder #import for Step 2
from sklearn.model_selection import train_test_split #import for Step 3
from sklearn.preprocessing import StandardScaler  #import for step 4
from sklearn.linear_model import LogisticRegression #import forstep 5 and 6
from sklearn.metrics import accuracy_score
#read data set using pandas
# dt = pd.read_csv("titanic.csv")
data = {
    "Age":[25,32,np.nan,78,23,np.nan,23,45,67],
    "Salary": [45000,np.nan, 56000,70000,23000, np.nan,80000,23000,55000],
    "Gender": ["Male","Female",np.nan,np.nan,"Female","Male","Male","Male","Female"],
    "City": ["Karachi","Lahore","Lahore","Islamabad","Karachi","Peshawar","Karachi","Islamabad","Peshawar"],
    "Purchased":[0,1,1,1,0,0,1,1,0]
}
dt = pd.DataFrame(data)
print("\n Original Dataset \n")

print(dt)

#handle missing values in data set using pandas
dt["Age"] =dt["Age"].fillna(dt["Age"].mean())
dt["Salary"] =dt["Salary"].fillna(dt["Salary"].mean())
dt["Gender"] =dt["Gender"].fillna(dt["Gender"].mode()[0])
print("\n After Handling Missing Values\n")

print(dt)

##Step 2: --------------------------------------------------------
#Label Encoding
#Label Encoding (Handling Categorical Data)
#Example Male/Female -> 1/0
le = LabelEncoder()

dt["Gender"] = le.fit_transform(dt["Gender"])
print("\n Label Encoding \n")
print(dt)

#One-Hot Encoding (Separate Columns Karachi, Lahore, Islamabad)

dt = pd.get_dummies(dt, columns=["City"])
print("\n One-Hot Encoding \n")
print(dt)

##Step 3: --------------------------------------------------------Assigning x or y
x = dt.drop("Purchased", axis=1)
y= dt["Purchased"]
##Step : --------------------------------------------------------Data Splitting

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=42
)


print("\n--------------------- OutPut Training and Testing Data -------------------\n")
print("X Train Data: \n",X_train)
print("\nX Test Data: \n",X_test)
print("\nY Train Data: \n",y_train.values)
print("\nY Test Data: \n",y_test.values)


##Step 4: --------------------------------------------------------Scaling (dasta ko balance krta h)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


##Step 5: --------------------------------------------------------Model Train

model = LogisticRegression()
model.fit(X_train,y_train) #Model train hojata h or predict krta h

#Step6 : -------------------------------------------------------Prediction
y_pred = model.predict(X_test)

print("Prediction: ",y_pred)

#Step 7:------------------------------------------------------------Accuracy

accuracy = accuracy_score(y_test,y_pred)
print("Accuracy: ",accuracy)



