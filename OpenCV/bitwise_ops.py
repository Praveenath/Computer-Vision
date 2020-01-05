import cv2
import numpy as np


def bit_ops(square, ellipse):
    And_out = cv2.bitwise_and(square, ellipse)
    cv2.imshow("AND", And_out)
    cv2.waitKey(0)

    Or_out = cv2.bitwise_or(square, ellipse)
    cv2.imshow("OR", Or_out)
    cv2.waitKey(0)

    Xor_out = cv2.bitwise_xor(square, ellipse)
    cv2.imshow("XOR", Xor_out)
    cv2.waitKey(0)

    Not_out = cv2.bitwise_not(square)
    cv2.imshow("NOT", Not_out)
    cv2.waitKey(0)


if __name__ == '__main__':
    # Make square
    square = np.zeros((300, 300), np.uint8)
    cv2.rectangle(square, (50, 50), (250, 250), 255, -2)
    # cv2.imshow("square", square)
    # cv2.waitKey(0)

    # Make ellipse
    ellipse = np.zeros((300, 300), np.uint8)
    cv2.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)
    # cv2.imshow("ellipse", ellipse)
    # cv2.waitKey(0)

    bit_ops(square, ellipse)
    cv2.destroyAllWindows()
