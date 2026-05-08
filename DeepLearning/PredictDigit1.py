from tensorflow import keras #Keras Library DeppLearning bnany ka kmkr rhi h
import matplotlib.pyplot as plt
import numpy as np
#Load Data Set
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

#normalized
x_train = x_train / 255.0
x_test = x_test / 255.0

#0 black
#255 white (data ko 0 or 1 m convert kr rhy hn)

#create model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

#compile
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']

)

# Train
model.fit(x_train, y_train, epochs=4)

#input
image = x_test[0]

#Test
model.evaluate(x_test, y_test)

#Prediction

prediction = model.predict(np.array([image]))

#Result
digit = np.argmax(prediction)

#show Image
plt.imshow(image, cmap='gray')
plt.title(f"Predicted Digit: = {digit}")
plt.show()
print(image)


