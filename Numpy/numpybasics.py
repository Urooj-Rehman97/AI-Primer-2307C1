import numpy as np

data = np.array([10,20,30,40,50])
print("Actual Data: ",data)

print("After multiply by 5: ",data * 5)  #yeh loopkbagair hr element papply hota h or issy Vectorization kehty hn
print("After Adding 4: ",data + 4)  #Vectorization

print("Type of Data:",type(data))

#built in functions
print(np.zeros(5))
print(np.ones(5))
print(np.arange(1,10,2))
print(np.linspace(0,1,3))
print(np.linspace(0,2,6))

#Aggregate function
marks = np.array([56,78,90,45,88])
avg = marks.mean()
obtainedMarks = marks.sum()
maxMarks = marks.max()
minMarks = marks.min()

print(f"Student Marks: {marks}")
print(f"Obtained Marks: {obtainedMarks}")
print(f"Average: {avg}")
print(f"Max Marks: {maxMarks}")
print(f"Min Marks: {minMarks}")

arr =np.array([[1,3,5],
              [2,4,6]])

#Shape,ndim, size
print(f"Shapeof arr: {arr.shape}")
print(f"Shape of data: {data.shape}")

print(f"dimension of arr: {arr.ndim}")
print(f"dimension of data: {data.ndim}")

print(f"Size of arr: {arr.size}")
print(f"Size of data: {data.size}")

#Indexing and Slicing
print(f"Data at first index: {data[0]}")
print(f"Data at last index: {data[-1]}")  #-1 is used to aceess last indexing value

#array[start:end] (slicing)
print(f"First 3 values in our data: {data[:3]}")
print(f"Value from index 1 to 3: {data[1:4]}")
print(f"Last 3 values in outr data: {data[2:]}")

print(f"2D Indexing: {arr[1,2]}")

print(f"2D Indexing: {arr[:,2]}")

print(f"Square of data: {data ** 2}")

