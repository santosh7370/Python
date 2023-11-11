import tensorflow as tf
from tensorflow.keras import layers

# Generate sequential data
seq_length = 10
data = tf.random.normal([100, seq_length, 5])

# Build an LSTM model
model = tf.keras.Sequential([
    layers.LSTM(10, input_shape=(None, 5)),
    layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(data, tf.random.normal([100, 1]), epochs=10)
