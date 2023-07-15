import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('my_model8_(15_epochs_0.2_sm).keras')   

def predict_img(img):
    processed_image = np.expand_dims(img, axis=0)
    predictions = model.predict(processed_image)
    predicted_class = tf.argmax(predictions[0]).numpy()
    #for i, prob in enumerate(predictions[0]):
        #print("Уверенность в цифре", i, ":", prob*100)
    return [predicted_class, predictions[0]]