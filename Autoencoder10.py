import tensorflow as tf
from tensorflow.keras import layers

# Create a simple autoencoder
encoder = tf.keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu')
])

decoder = tf.keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(32,)),
    layers.Dense(128, activation='relu'),
    layers.Dense(784, activation='sigmoid')
])

autoencoder = tf.keras.Sequential([encoder, decoder])

# Compile the model
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
