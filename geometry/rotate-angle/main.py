import numpy as np


def getRotateAngle(x1, x2, y1, y2):
    dot = np.inner([x1, y1], [x2, y2])
