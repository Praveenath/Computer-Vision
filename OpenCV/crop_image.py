import cv2
import numpy as np


def crop_image(img):
    height, width = img.shape[:2]

    start_row, start_col = int(height * 0.25), int(width * 0.25)

    end_row, end_col = int(height * 0.75), int(width * 0.75)

    cropped_image = img[start_row: end_row, start_col:end_col]

    cv2.imshow("Original Image", img)
    cv2.waitKey(0)
    cv2.imshow("Cropped Image", cropped_image)
    cv2.waitKey(0)


if __name__ == '__main__':
    img = cv2.imread('./images/cat.jpg')
    crop_image(img)
    cv2.destroyAllWindows()
