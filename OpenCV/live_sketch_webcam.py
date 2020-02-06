import cv2
import numpy as np


def sketch(image):
    # Convert BGR to Gray
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Clean up image using blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # Extarct edges
    edges = cv2.Canny(img_gray_blur, 10, 70)

    # invert image
    ret, mask = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)

    return mask


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()
        cv2.imshow('Live Sketch', sketch(frame))
        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()
