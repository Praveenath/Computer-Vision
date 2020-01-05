# import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt


def calculate_histogram(img):
    histogram = cv2.calcHist([img], [0], None, [256], [0, 256])

    # Flatten the image
    plt.hist(img.ravel(), 256, [0, 256]);
    plt.show()

    # view separate color channels
    color = ('b', 'g', 'r')

    # seprating colors and plots
    for i, col in enumerate(color):
        histogram2 = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histogram2, color=col)
        plt.xlim([0, 256])

    plt.show()


if __name__ == '__main__':
    # Read image
    image_input = cv2.imread('./images/cat.jpg')
    calculate_histogram(image_input)
