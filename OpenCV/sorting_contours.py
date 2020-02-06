import cv2
import numpy as np


def extract_contours(image):
    # black image
    black_image = np.zeros((image.shape[0], image.shape[1], 3))

    # copy of original image
    original_img = image

    # BGR to Gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find Canny Edges
    edged = cv2.Canny(gray, 50, 100)
    cv2.imshow('1.Canny Edges', edged)
    cv2.waitKey(0)

    # Find contours
    contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print("Number of contours found: ", len(contours))

    # Draw all counters
    cv2.drawContours(black_image, contours, -1, (0, 255, 0), 3)
    cv2.imshow('2.Contours over black image', black_image)
    cv2.waitKey(0)

    # Draw all counters
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
    cv2.imshow('3.Contours over original image', image)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

    return contours, original_img


def sort_contours_by_area(image, contours):
    def get_contour_areas(contours):
        # Returns area of all countours
        all_area = []
        for cnt in contours:
            all_area.append(cv2.contourArea(cnt))

        return all_area

    original_image = image

    # Contours area before sorting
    print('Contours area before sorting: ', get_contour_areas(contours))

    # Sort contours large to small
    sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Contours area after sorting
    print('Contours area after sorting: ', get_contour_areas(sorted_contours))

    # Draw sorted contours in the decending order
    for c in sorted_contours:
        cv2.drawContours(original_image, [c], -1, (255, 0, 0), 3)
        cv2.waitKey(0)
        cv2.imshow('Contours by area', original_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def sort_contors_from_left2right(image):
    def x_coordinate_contours(contours):

        # Returns the X coordinate for the contour centroid
        if cv2.contourArea(contours) > 10:
            M = cv2.moments(contours)
            return (int(M['m10'] / M['m00']))

    def label_countour_center(image, c):
        # Put a red circle on the centers of contours
        M = cv2.moments(c)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])

        # Draw contour number on the image
        cv2.circle(image, (cx, cy), 10, (0, 0, 255), -1)

        return image

    original_img = image.copy()

    # Compute center of mass
    for (i, c) in enumerate(contours):
        orig = label_countour_center(image, c)

    cv2.imshow("4 - Contour centers", image)
    cv2.waitKey(0)

    # Sort contours by lef to right
    contours_left_to_right = sorted(contours, key=x_coordinate_contours, reverse=False)

    # Labelling contours left to right
    for (i, c) in enumerate(contours_left_to_right):
        cv2.drawContours(original_img, [c], -1, (0, 0, 255), 3)
        M = cv2.moments(c)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.putText(original_img, str(i + 1), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("6 - Left to Right Contours", original_img)

        cv2.waitKey(0)
        (x, y, w, h) = cv2.boundingRect(c)

        # Crop and Save images
        cropped = original_img[y:y + h, x: x + w]
        img_name = "output_shape_" + str(i + 1) + ".jpg"
        cv2.imwrite('./outputs/' + img_name, cropped)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('images/bunchofshapes.jpg')
    cv2.imshow('Original', img)
    cv2.waitKey(0)

    contours, image = extract_contours(img)
    sort_contours_by_area(image, contours)
    sort_contors_from_left2right(image)
