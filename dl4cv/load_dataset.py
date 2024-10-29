import os
import cv2
import numpy as np

from tensorflow.keras.preprocessing.image import img_to_array


def load_dataset(image_paths, verbose=500):
    data = []
    labels = []
    for i, path in enumerate(image_paths):
        # Show an update
        if verbose > 0 and i > 0 and (i + 1) % verbose == 0:
            print(f"Loading {i+1} of {len(image_paths)} images...")
        # Load the image
        image = cv2.imread(path)
        # Extract the class label
        label = path.split(os.path.sep)[-2]

        # Simple Preprocessor
        # Resize the image to a fixed size (ignore the aspect ratio)
        height = 32
        width = 32
        image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

        # Image To Array Preprocessor
        image = img_to_array(image)

        data.append(image)
        labels.append(label)

    return (np.array(data), np.array(labels))
