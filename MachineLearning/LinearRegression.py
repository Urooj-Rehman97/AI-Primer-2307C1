from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
x = [[1],[2],[4],[5]]  #experience
y = [30000, 45000, 75000, 90000]

model = LinearRegression()

model.fit(x,y) # Model train kryega fit ka method

print(model.predict([[3]]))
print(model.predict([[6]]))

#Graph Visualization
plt.scatter(x,y)
plt.plot(x, model.predict(x))
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()