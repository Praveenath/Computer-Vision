import  cv2
import numpy as np

def find_matching_contours(template, target):
    # Convert target image to gray scale
    target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

    # Binarize both images
    ret, thresh1 = cv2.threshold(template, 127, 255, 0)
    ret, thresh2 = cv2.threshold(target_gray, 127, 255, 0)

    # Find contours in template
    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours
    sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Extract 2nd largest contour
    template_contour = contours[1]

    # Extract contours target image
    contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:

        # Iterate through each countour in the target image
        match = cv2.matchShapes(template_contour, c, 3, 0.0)
        print(match)

        if match < 0.15:
            closest_contour = c
        else:
            closest_contour = []

    cv2.drawContours(target, [closest_contour], -1, (0, 255, 0), 3)
    cv2.imshow('Output', target)
    cv2.waitKey(0)

if __name__ == '__main__':

    template = cv2.imread('images/4star.jpg', 0)
    cv2.imshow('Tempate', template)

    cv2.waitKey(0)

    target = cv2.imread('images/shapestomatch.jpg')
    cv2.imshow('Target', target)
    cv2.waitKey(0)

    find_matching_contours(template, target)





