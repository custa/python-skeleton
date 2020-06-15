import io
import time

import cv2
import numpy as np
from PIL import Image

binary_data = open("image.jpg", 'rb').read()

repeat = 10
start_time = time.time()
for _ in range(repeat):
    img = Image.open(io.BytesIO(binary_data))
    im = np.asarray(img)
end_time = time.time()
print("Binary to ndarray takes time: {}".format(
    (end_time - start_time) / repeat))
