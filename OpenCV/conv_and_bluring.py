import numpy as np
import cv2


def custom_kernal(image):
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)

    kernal_3x3 = np.ones((3, 3), np.float32) / 9

    blurred = cv2.filter2D(image, -1, kernal_3x3)
    cv2.imshow('3x3 blurred Image', blurred)
    cv2.waitKey(0)

    kernal_7x7 = np.ones((7, 7), np.float32) / 49

    blurred = cv2.filter2D(image, -1, kernal_7x7)
    cv2.imshow('7x7 blurred Image', blurred)
    cv2.waitKey(0)

    cv2.destroyAllWindows()


def defined_blurring_funcs(image):
    # Blur using averaging filter / box filter
    blured_img = cv2.blur(image, (3, 3))
    cv2.imshow('Average Blurring', blured_img)
    cv2.waitKey(0)

    # Gaussian Blur
    gaussian = cv2.GaussianBlur(image, (7, 7), 0)
    cv2.imshow('Gaussian Blurring', gaussian)
    cv2.waitKey(0)

    # Meadian Blur
    median = cv2.medianBlur(image, 5)
    cv2.imshow('Median Blurring', median)
    cv2.waitKey(0)

    # Bilateral filter ( very effective in noise removel while keeping edges sharp
    bilateral = cv2.bilateralFilter(image, 9, 75, 75)
    cv2.imshow('Bilateral filter', bilateral)
    cv2.waitKey(0)

    cv2.destroyAllWindows()


def image_denoising(image):
    img = cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21)
    cv2.imshow('Image Denoising - Non-local Means Denoising', img)
    cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('./images/elephant.jpg')
    custom_kernal(img)
    defined_blurring_funcs(img)
    image_denoising(img)
