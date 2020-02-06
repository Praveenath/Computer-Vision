import cv2
import numpy as np


def draw_contour(image):
    # Convert BGR to Gray
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find canny edges
    edged = cv2.Canny(img_gray, 30, 200)
    cv2.imshow('Canny Edges', edged)
    cv2.waitKey(0)

    # Find edges
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.imshow('Final Contours', edged)
    cv2.waitKey(0)

    print("Number pf contours found = " + str(len(contours)))

    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    cv2.imshow('Contours', image)
    cv2.waitKey(0)


if __name__ == '__main__':
    img = cv2.imread('images/shapes.jpg')
    cv2.imshow('Original', img)

    draw_contour(img)

    cv2.destroyAllWindows()
