import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('my_model11_(5_epochs_0.2_sm).keras')   


def predict_img(img):
    img1 = img/255.0
    processed_image = np.expand_dims(img1, axis=0)
    predictions = model.predict(processed_image)
    predicted_class = tf.argmax(predictions[0]).numpy()
    return [predicted_class, predictions[0]]