import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
image_raw_data = tf.gfile.FastGFile("1.jpg","rb").read();
with tf.Session() as sess:
     img_data = tf.image.decode_jpeg(image_raw_data)
     print("Digital type: ", img_data.dtype)
     plt.imshow(img_data.eval())
     plt.show()
     img_data=tf.image.resize_images(img_data,[180,267],method=1)
     print("Digital type: ", img_data.dtype)
     batched=tf.expand_dims(tf.image.convert_image_dtype(img_data,tf.float32),0)
     boxes=tf.constant([[[0.05,0.05,0.9,0.7],[0.35,0.47,0.5,0.56]]])
     result=tf.image.draw_bounding_boxes(batched,boxes)
     plt.figure(1)
     plt.imshow(result.eval().reshape([180, 267, 3]))
     plt.show()
