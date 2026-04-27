import numpy as np

arr = np.array([10,20,30,40,50,60])

# a = arr>30
print(arr>30)

print(arr[arr>30])

print((arr>10) & (arr<45))
print(arr[(arr>10) & (arr<45)])

