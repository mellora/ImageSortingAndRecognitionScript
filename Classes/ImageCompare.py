import cv2
import numpy as np
import os


class ImageCompare:
    original = ""
    duplicate = ""

    def __init__(self):
        pass

    # Load original image into the class for comparison
    def load_original_image(self, img_path):
        self.original = cv2.imread(img_path)
        return

    # Load possible duplicate image into the class for comparison
    def load_duplicate_image(self, img_path):
        self.duplicate = cv2.imread(img_path)
        return

    # Check if image's are equals
    def check_if_duplicate(self):
        if self.original.shape == self.duplicate.shape:
            difference = cv2.subtract(self.original, self.duplicate)
            b, g, r = cv2.split(difference)
            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                return True
        return False


if __name__ == "__main__":
    test = ImageCompare()
    test.load_original_image(os.path.normpath("D:/Mega/Media/60875344_p0.jpg"))
    test.load_duplicate_image(os.path.normpath("D:/Pictures/image0 - 2020-05-18T211552.602.jpg"))
    print(test.check_if_duplicate())
