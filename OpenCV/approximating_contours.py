import cv2
import numpy as np


def find_approximated_polygon(image):
    image_cpy = image.copy()

    # Grayscale and Binarization
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    # Iterate through each contour and compute bounding rectangles
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(image_cpy, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('Bounding Rectangles', image_cpy)

    cv2.waitKey(0)

    # Iterate through each contour and compute approximated contours
    for c in contours:
        # Calculate accuracy as a percent of the contour perimeter
        accuracy = 0.03 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, accuracy, True)
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
        cv2.imshow("Approx Poly DP", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def fine_convex_hull(image):
    # Grayscale and Binarization
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 176, 255, 0)

    # Find contours
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    # Sort contours by area and then remove the largest frame contour
    n = len(contours) - 1
    contours = sorted(contours, key=cv2.contourArea, reverse=False)[:n]

    # Iterate through each contour and compute bounding rectangles
    for c in contours:
        hull = cv2.convexHull(c)
        cv2.drawContours(image, [hull], 0, (0, 255, 0), 2)
        cv2.imshow('Convex Hull', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img1 = cv2.imread('images/house.jpg')

    cv2.imshow('Original Image', img1)
    cv2.waitKey(0)

    find_approximated_polygon(img1)

    img2 = cv2.imread('images/hand.jpg')

    cv2.imshow('Original Image 2', img2)
    cv2.waitKey(0)

    fine_convex_hull(img2)
