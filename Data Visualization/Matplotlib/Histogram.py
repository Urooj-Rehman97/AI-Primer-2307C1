import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(1000)
# data = [12,15,13,10,18,20,22,25,18,17,16,19,21,23,24]

plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Freqruency')
plt.title('Matplotlib HistogramChart')
plt.show()