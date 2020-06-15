import os
import datetime
import cv2

if __name__ == "__main__":
    location_path = os.path.realpath(os.path.dirname(__file__))
    jpg = os.path.join(location_path, "..", "1.jpg")
    image = cv2.imread(jpg)
    now = str(datetime.datetime.now())
    cv2.putText(image, now, (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
    cv2.imshow("put text", image)
    cv2.waitKey(0)
