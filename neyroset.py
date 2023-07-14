import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('my_model4.h5')   

def predict_img(img):
    processed_image = np.expand_dims(img, axis=0)
    predictions = model.predict(processed_image)
    predicted_class = tf.argmax(predictions[0]).numpy()
    print(predicted_class)
    return predicted_class