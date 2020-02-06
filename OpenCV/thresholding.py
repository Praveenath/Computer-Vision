import cv2
import numpy as np


def perform_thresholding(image):
    # <127 -> 0 and >127 -> 255
    ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('Binary Threshold', thresh1)

    # <127 -> 255 and >127 -> 0
    ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('Binary Inverse Threshold', thresh2)

    # >127 are truncated at 127
    ret, thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
    cv2.imshow('Threshold Truncate', thresh3)

    # <127 -> 0, above 127 are unchanged
    ret, thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
    cv2.imshow('Threshold To Zero', thresh4)

    # >127 -> 0, below 127 are unchanged
    ret, thresh5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow('Threshold To Zero', thresh5)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def perform_advance_thresholding(image):
    # <127 -> 0 and >127 -> 255
    ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('Binary Threshold', thresh1)

    # blur image as it removes noise
    image = cv2.GaussianBlur(image, (3, 3), 0)

    # Adaptive thresholding
    thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
    cv2.imshow('Adaptive threshold', thresh)

    # Otsu's thresholding
    _, thresh2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imshow('Otsu threshold', thresh2)

    # Otsu's threshold after gaussian filtering
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    _, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imshow('Gaussian Otsu\'s threshold', th3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('images/Origin_of_Species.jpg', 0)
    # img = cv2.imread('images/gradient.jpg', 0)
    cv2.imshow('Original', img)
    # perform_thresholding(img)
    perform_advance_thresholding(img)
