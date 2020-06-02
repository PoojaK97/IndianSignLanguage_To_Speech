import tensorflow as tf
from tensorflow import keras
model = keras.models.load_model('model.h5')
#kerasFile = 'model.h5'
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
with tf.gfile.GFile('model.tflite', 'wb') as f:
    f.write(tflite_model)