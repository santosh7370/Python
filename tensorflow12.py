import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Example text data
texts = ["This is a positive sentence.", "Negative sentiment here."]

# Tokenize and pad sequences
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
padded_sequences = pad_sequences(sequences, maxlen=5)

# Build a simple model
model = tf.keras.Sequential([layers.Embedding(input_dim=1000, output_dim=16, input_length=5),layers.Flatten(),layers.Dense(1, activation='sigmoid')])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
labels = [1, 0]
model.fit(padded_sequences, labels, epochs=5)
