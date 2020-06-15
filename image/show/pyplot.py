import matplotlib.pyplot as plt
import glob
import os


if __name__ == "__main__":
    script_path = os.path.realpath(__file__)
    dir = os.path.dirname(script_path)
    img = None
    for jpg in glob.glob(os.path.join(dir, "..", "*.jpg")):
        im = plt.imread(jpg)
        if img is None:
            img = plt.imshow(im)
        else:
            img.set_data(im)
        plt.pause(3)
