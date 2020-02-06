import numpy as np
import cv2


def detect_edges(image):
    # Edge Extraction using Sobel
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

    cv2.imshow('Sobel X', sobel_x)
    cv2.imshow('Sobel Y', sobel_y)

    # Combine sobel_x(vertical) and sobel_y(horizontal) edges
    sobel = cv2.bitwise_or(sobel_x, sobel_y)
    cv2.imshow('Sobel Combined', sobel)

    # Laplacian Edge Detector
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    cv2.imshow('Laplacian', laplacian)

    # Canny Edge Detector
    canny = cv2.Canny(image, 20, 170)
    cv2.imshow('Canny', canny)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('images/input.jpg', 0)

    cv2.imshow('Original', img)
    
    detect_edges(img)
