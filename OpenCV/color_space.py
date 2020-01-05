# import libraries
import cv2
import numpy as np


def extract_pixel_RGB(image_input):
    # BGR color levels of a pixel
    B, G, R = image_input[10, 50]
    print(B, G, R)

    # Gray levels of pixel values
    gray_image = cv2.cvtColor(image_input, cv2.COLOR_BGR2GRAY)
    print(gray_image.shape)

    print(gray_image[10, 50])


# ----------------------- HSV channels---------------------------
def extract_hsv_channels(image_input):
    hsv_image = cv2.cvtColor(image_input, cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV image', hsv_image)
    cv2.imshow('Hue', hsv_image[:, :, 0])
    cv2.imshow('Saturation', hsv_image[:, :, 1])
    cv2.imshow('Value', hsv_image[:, :, 2])

    cv2.waitKey()
    cv2.destroyAllWindows()


# ----------------------- RGB channels---------------------------
def extract_rgb_channels(image_input):
    B, G, R = cv2.split(image_input)

    cv2.imshow('RGB image', image_input)
    cv2.imshow('R', R)
    cv2.imshow('G', G)
    cv2.imshow('B', B)

    cv2.waitKey()
    cv2.destroyAllWindows()

    # Image Remake
    merged = cv2.merge([B, G, R])
    cv2.imshow('Merged image', merged)

    # Amplify the blue color
    merged = cv2.merge([B + 100, G, R])
    cv2.imshow('Merged with blue amplified', merged)

    cv2.waitKey()
    cv2.destroyAllWindows()


def extract_actual_rgb_channels(input):
    B, G, R = cv2.split(input)

    zeros = np.zeros(input.shape[:2], dtype="uint8")

    cv2.imshow('R', cv2.merge([zeros, zeros, R]))
    cv2.imshow('G', cv2.merge([zeros, G, zeros]))
    cv2.imshow('B', cv2.merge([B, zeros, zeros]))

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # Read image
    image_input = cv2.imread('./images/cat.jpg')
    # extract_pixel_RGB(image_input)
    # extract_hsv_channels(image_input)
    # extract_rgb_channels(image_input)
    extract_actual_rgb_channels(image_input)
