from sklearn.tree import DecisionTreeClassifier  # Predict classification (0/1), (no/yes)
###Example 1
    # Pass / Fail  (1/0)
    
x = [[30],[40],[50],[60]]  
y = [0,0,1,1]

model = DecisionTreeClassifier()

model.fit(x,y) # Model train kryega fit ka method

print(model.predict([[70]]))
print(model.predict([[45]]))
