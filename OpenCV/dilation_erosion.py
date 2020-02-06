import numpy as np
import cv2


def dilation_and_erosion(image, kernel):
    # Erosion
    eroded = cv2.erode(image, kernel, iterations=1)
    cv2.imshow('Eroded Image', eroded)

    dilated = cv2.dilate(image, kernel, iterations=1)
    cv2.imshow('Dilated Image', dilated)


# Morphological Operations
def opening_and_closing(image, kernel):
    # Opening: Good for removing noise
    opening_img = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    cv2.imshow('Opening', opening_img)

    # Closing: Good for removing noise
    closing_img = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('Closing', closing_img)


if __name__ == '__main__':
    kernal = np.ones((5, 5), np.uint8)

    img = cv2.imread('images/opencv_inv.png', 0)

    cv2.imshow('Original', img)

    dilation_and_erosion(img, kernal)
    opening_and_closing(img, kernal)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
