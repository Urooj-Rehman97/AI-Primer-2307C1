from sklearn.linear_model import LogisticRegression  
###Example 1
    Pass / Fail  (1/0)

    x = [[30],[40],[50],[60]]  #Marks
    y = [0,0,1,1]

    model = LogisticRegression()

    model.fit(x,y) # Model train kryega fit ka method

    print(model.predict([[70]]))
    print(model.predict([[45]]))





