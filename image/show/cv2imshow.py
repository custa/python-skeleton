import cv2
import threading
import sys


def show(file_path):
    img = cv2.imread(file_path)
    cv2.namedWindow("Image")
    cv2.imshow("Image", img)
    if cv2.waitKey(0) == 27:
        sys.exit(0)


if __name__ == "__main__":
    t1 = threading.Thread(target=show, args=("../1.jpg", ), name='Thread-A')
    t1.start()
    t2 = threading.Thread(target=show, args=("../30.jpg", ), name='Thread-A')
    t2.start()
    t1.join()
    t2.join()
