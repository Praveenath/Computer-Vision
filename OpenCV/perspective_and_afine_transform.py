import numpy as np
import cv2


def perspective_transform(image):
    # Co-ordinates of the 4 corners of the original image
    points_A = np.float32([[320, 15], [700, 215], [85, 610], [530, 780]])

    # Co-ordinates of the 4 corners of the desired output
    points_B = np.float32([[0, 0], [420, 0], [0, 594], [420, 594]])

    # Perform perspective transformation
    M = cv2.getPerspectiveTransform(points_A, points_B)

    warped_output = cv2.warpPerspective(image, M, (420, 594))

    cv2.imshow('warp perspective', warped_output)


def affine_transform(image):
    rows, cols, ch = image.shape

    # Co-ordinates of the 4 corners of the original image
    points_A = np.float32([[320, 15], [700, 215], [85, 610]])

    # Co-ordinates of the 4 corners of the desired output
    points_B = np.float32([[0, 0], [420, 0], [0, 594]])

    # Perform perspective transformation
    M = cv2.getAffineTransform(points_A, points_B)

    warped_output = cv2.warpAffine(image, M, (cols, rows))

    cv2.imshow('warp affine', warped_output)


if __name__ == '__main__':
    img1 = cv2.imread('images/scan.jpg')

    cv2.imshow('Original Perspective', img1)

    perspective_transform(img1)

    img2 = cv2.imread('images/ex2.jpg')

    cv2.imshow('Original Affine', img2)

    affine_transform(img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
