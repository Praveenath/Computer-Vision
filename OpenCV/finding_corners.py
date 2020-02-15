import cv2
import numpy as np


def find_corners(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)

    harris_corners = cv2.cornerHarris(gray, 3, 3, 0.05)

    kernal = np.ones((7, 7), np.uint8)
    harris_corners = cv2.dilate(harris_corners, kernal, iterations=2)

    image[harris_corners > 0.025 * harris_corners.max()] = [255, 127, 127]

    cv2.imshow('Harris Corners', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def find_good_features_to_track(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 15)

    for corner in corners:
        x, y = corner[0]
        x, y = int(x), int(y)
        cv2.rectangle(image, (x - 10, y - 10), (x + 10, y + 10), (0, 255, 0), 2)

    cv2.imshow('Corners', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('images/chess.jpg')
    img2 = img.copy()
    
    find_corners(img)
    find_good_features_to_track(img2)
