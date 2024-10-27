import tensorflow as tf

# Check if TensorFlow can access any GPU devices
gpus = tf.config.list_physical_devices("GPU")
if gpus:
    print("TensorFlow can access the following GPUs:")
    for gpu in gpus:
        print(gpu)
else:
    print("TensorFlow cannot access any GPUs.")
