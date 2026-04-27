import matplotlib.pyplot as plt

x = [1,2,3,4]
y1 = [10,20,30,40]
y2 = [40,30,20,10]

#First Graph
plt.subplot(1,2,1)
plt.plot(x,y1)
plt.title("Graph 1")

#Second Graph
plt.subplot(1,2,2)
plt.plot(x,y2)
plt.title("Graph 2")
plt.show()