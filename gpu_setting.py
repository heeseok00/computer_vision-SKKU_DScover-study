import tensorflow as tf
import time

print("TF version:", tf.__version__)
print("GPU devices:", tf.config.list_physical_devices('GPU'))

with tf.device('/GPU:0'):
    a = tf.random.normal([3000, 3000])
    b = tf.random.normal([3000, 3000])

    start = time.time()
    c = tf.matmul(a, b)
    _ = c.numpy()
    end = time.time()

print("done")
print("elapsed:", end - start)