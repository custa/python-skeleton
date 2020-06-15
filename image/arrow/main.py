import cv2
import numpy as np
im = np.zeros((600, 800, 3), np.uint8)

cv2.arrowedLine(im, (0, 0), (500, 500), (0, 0, 255), thickness=2)

cv2.arrowedLine(im, (10, 50), (100, 500), (0, 0, 255),
                line_type=cv2.LINE_4,
                thickness=2)

cv2.arrowedLine(im, (110, 50), (210, 500), (0, 0, 255),
                line_type=cv2.LINE_8,
                thickness=2)

cv2.arrowedLine(im, (210, 50), (310, 500), (0, 0, 255),
                line_type=cv2.LINE_AA,
                thickness=2,
                tipLength=0.02)

cv2.imshow("blank", im)
cv2.waitKey(0)
