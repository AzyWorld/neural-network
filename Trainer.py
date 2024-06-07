import tensorflow as tf
import numpy as np

# Загрузка данных
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
loaded_x_additional = np.load('imgs.npy')
loaded_y_additional = np.load('answers.npy')
# Предобработка данных
x_train, x_test = x_train / 255.0, x_test / 255.0
loaded_x_additional = loaded_x_additional / 255.0

x_train = np.concatenate((x_train, loaded_x_additional))
y_train = np.concatenate((y_train, loaded_y_additional))

# Создание модели нейронной сети
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

# Компиляция модели
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['accuracy'])

# Обучение модели
model.fit(x_train, y_train, epochs=5)

# Оценка точности модели
print(model.evaluate(x_test, y_test))

model.save('my_model11_(5_epochs_0.2_sm).keras')