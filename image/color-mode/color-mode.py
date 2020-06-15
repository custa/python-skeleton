# https://blog.csdn.net/saltriver/article/details/78173219
# matplotlib 使用 RGB模式
# opencv 使用 BGR 模式
import os
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    location_path = os.path.realpath(os.path.dirname(__file__))
    image_file = os.path.join(location_path, "dog-cat.jpg")

    # JpegImageFile    image1.mode = "RGB"
    image0 = Image.open(image_file)
    # ndarray
    image1 = plt.imread(image_file)

    # ndarry
    image2 = cv2.imread(image_file)

    # Image.open 读取 plt.imshow 显示 -- 正常
    plt.imshow(image0)
    plt.show()

    # cv2.imread 读取 cv2.imshow 显示 -- 正常
    cv2.imshow("cv2.imread", image2)

    # Image.open 读取 cv2.imshow 显示 -- 色彩不对
    cv2.imshow("Image.open", np.array(image0))

    cv2.waitKey(0)
