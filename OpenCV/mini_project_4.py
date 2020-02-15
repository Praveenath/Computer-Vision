import cv2
import numpy as np


def find_woldo(image, template):
    cv2.imshow('Original', image)
    cv2.waitKey(0)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # bounding box
    top_left = max_loc
    bottom_right = (top_left[0] + 50, top_left[1] + 50)

    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 2)

    cv2.imshow('Image found', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('images/WaldoBeach.jpg')

    temp = cv2.imread('images/waldo.jpg', 0)

    find_woldo(img, temp)
