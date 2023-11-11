import tensorflow as tf
import numpy as np

# Generate random data
np.random.seed(0)
X_train = np.random.rand(100, 1)
y_train = 3 * X_train + 2 + 0.1 * np.random.randn(100, 1)

# Define the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=50)

# Make predictions
X_new = np.array([[0.5]])
y_pred = model.predict(X_new)
print("Prediction:", y_pred)
