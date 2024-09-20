# Import TensorFlow and Keras to create the neural network
import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.datasets import mnist # type: ignore
from tensorflow.keras import backend as K # type: ignore
import numpy as np
# Matplotlib to plot info to show the results
import matplotlib.pyplot as plt



# Load the MNIST Data
def show_min_max(array, i):
    random_image = array[i]
    print("Min and max values in image:", random_image.min(), random_image.max())



# Create a function that will plot a image from the dataset and display the digit label.
def plot_image(array, i, labels):
    plt.imshow(np.squeeze(array[i]))
    plt.title(" Digit ")
    plt.xticks()
    plt.yticks()
    plt.show


# Create a variable called num_classes and set the value to 10 output classes.
img_rows, img_cols = 28, 28

# Create a variable called num_classes and set the value to 10 output classes.
num_classes = 10



# Load the data to train and test the model, as well as the labels to test the data against.
(train_images, train_labels), (test_images, test_labels) = mnist.load_data() 

# Load a backup copy of the untouched data, while the first copy will be processing the data and manipulating it.
(train_images_backup, train_labels_backup), (test_images_backup, test_labels_backup) = mnist.load_data()


# Print the shape of the training image dataset.
print(train_images.shape)

# Print the shape of the test image dataset.
print(test_images.shape)



# Reshape the training data by converting the list of pixels into a 28x28 grid.
train_images = train_images.reshape(train_images.shape[0],  img_rows, img_cols, 1)

# Reshape the test data by converting the list of pixels into a 28x28 grid.
test_images = test_images.reshape(test_images.shape[0],  img_rows, img_cols, 1)

# Create an input_shape variable to keep track of the data's shape.
input_shape = (img_rows, img_cols, 1)   




# Call the plot_image function to print out the 100th image in train_images.
plot_image(train_images, 100, train_labels)

# Call the show_min_max function to print the min and max values of the image.
show_min_max(train_images, 100)

# Change the image values to between 0 and 1, convert that training data into float32.
train_images = train_images.astype('float32')

# Change the image values to between 0 and 1, convert that test data into float32.
test_images = test_images.astype('float32')


# Divide the images by 255 to make sure that each pixel is stored as a value between 0 and 1.
train_images /= 255
test_images /= 255

# Call the plot_image function to print out the 100th image in train_images.
plot_image(train_images, 100, train_labels)

# Call the show_min_max function to print the min and max values of the image.
show_min_max(train_images, 100)


# Employ one-hot encoding on your training labels.
train_labels = keras.utils.to_categorical(train_labels, num_classes)

# Employ one-hot encoding on your test labels.
test_labels = keras.utils.to_categorical(test_labels, num_classes)


# Import the Sequential model.
from tensorflow.keras.models import Sequential # type: ignore


# Import the Dense and Flatten layers.
from tensorflow.keras.layers import Dense, Flatten # type: ignore



# Create a variable called epochs and set the value as 10.
epochs = 100

# Create a new model object using the Keras Sequential.
model = Sequential()


# Add a Flatten layer and pass the input shape as an argument.
model.add(Flatten(input_shape=input_shape))


# Add a Dense layer to your network with the size of the layers in neurons and relu as the activation function.
model.add(Dense(10, activation='relu'))





# Add an output layer.
model.add(Dense(10, activation='softmax'))


# Print a summary of your network so far.
model.summary()



# Add the compile function that calculates the loss and uses the optimizer parameter to set the optimization algorithm.
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# Add the fit function and set the input data for the model so the network doesn't rely on a pattern to learn.
model.fit(train_images, train_labels, epochs=epochs, shuffle=True)



# Calculate the loss and accuracy of your model.
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

# Print out the test accuracy.
print('\nTest accuracy:', test_acc)


# Export your model
model.save("my_model.h5")