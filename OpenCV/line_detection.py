import cv2
import numpy as np


def hough_lines(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 100, 170, apertureSize=3)

    lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)
    print(lines)

    for rho, theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cv2.imshow('Hough Lines', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def probabilistic_hough_line(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 100, 170, apertureSize=3)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, 5, 10)
    print(lines)

    for x1, y1, x2, y2 in lines[0]:
        cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)

    cv2.imshow('Probabilistic Hough Lines', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('images/soduku.jpg')

    hough_lines(img)

    probabilistic_hough_line(img)
