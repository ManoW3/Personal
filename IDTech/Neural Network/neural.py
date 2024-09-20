# Import TensorFlow and Keras to create the neural network
import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.datasets import mnist
from tensorflow.keras import backend as K
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
    plt.title(" Digit " + str(labels[i]))
    plt.xticks([])
    plt.yticks([])
    plt.show

# Create variables for the image row and column to keep track of your image size.
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


# Change the image values to between 0 and 1, convert that test data into float32.


# Divide the images by 255 to make sure that each pixel is stored as a value between 0 and 1.


# Call the plot_image function to print out the 100th image in train_images.


# Call the show_min_max function to print the min and max values of the image.







# Employ one-hot encoding on your training labels.


# Employ one-hot encoding on your test labels.





# Import the Sequential model.


# Import the Dense and Flatten layers.





# Create a variable called epochs and set the value as 10.


# Create a new model object using the Keras Sequential.


# Add a Flatten layer and pass the input shape as an argument.


# Add a Dense layer to your network with the size of the layers in neurons and relu as the activation function.


# Add an output layer.


# Print a summary of your network so far.
