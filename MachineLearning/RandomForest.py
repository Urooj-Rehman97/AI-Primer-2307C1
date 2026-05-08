#Step 1
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

#Step 2
#Study hours input
x = np.array([[1],[2],[3],[4],[5],[6],[7],[8]] )

#Result 0 Fail, 1Pass Output 
y = np.array([0,0,0,1,1,1,1,1] ) 

#Step 3
model = RandomForestClassifier(n_estimators = 5, random_state = 42)  #n_estimators kitny trees bnyengy yeh define krta h or randomstate outputstate ko balance rkhta

#Step 4
model.fit(x,y)

#Step 5
user_input = 3.6

#Step 6
prediction = model.predict([[user_input]])



# Step 7
print("Study Hours: ",user_input)
print("Predicted Output: ", prediction , "(0 = Fail, 1 = Pass)")

#Step 8
plt.figure()

plt.scatter(x,y ,label="Train Data") #for original Dataset
plt.scatter([user_input], [prediction], label="Your Prediction") #for prediction

plt.xlabel("Study Hours")
plt.ylabel("Result: (0=Fail,1=Pass)")
plt.title("Random Forest Visualization")

plt.legend()
plt.show()
