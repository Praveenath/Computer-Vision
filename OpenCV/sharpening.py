import cv2
import numpy as np


def image_sharpening(image):
    # Sharpening Kernal
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])

    # Apply kernel to image
    sharpened_image = cv2.filter2D(image, -1, kernel)

    cv2.imshow('Sharpened imgae', sharpened_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('images/input.jpg')
    cv2.imshow('original image', img)
    image_sharpening(img)
