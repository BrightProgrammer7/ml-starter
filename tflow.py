import tensorflow as tf
print("TensorFlow version:", tf.__version__)

tf.config.list_physical_devices('GPU')
tf.test.is_gpu_available()
