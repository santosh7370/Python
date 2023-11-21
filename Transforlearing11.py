import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np

# Load MobileNetV2 pre-trained on ImageNet
base_model = MobileNetV2(weights='imagenet', include_top=True)

# Load and preprocess an image
img_path = 'path_to_your_image.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Make predictions
preds = base_model.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])
