import cv2
import numpy as np


def add_sub_images(img_org):
    M = np.ones(img_org.shape, dtype="uint8") * 75

    added = cv2.add(img_org, M)

    cv2.imshow("Added", added)

    subtracted = cv2.subtract(img_org, M)

    cv2.imshow("Subtracted", subtracted)


if __name__ == '__main__':
    img = cv2.imread('./images/input.jpg')

    add_sub_images(img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
