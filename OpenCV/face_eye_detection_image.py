import cv2
import numpy as np


def detect_face_and_eye(image, face_classifier, eye_classifier):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        print("Face not found!")

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (127, 0, 255), 2)
        cv2.imshow('img', image)
        cv2.waitKey(0)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = image[y:y + h, x:x + w]

        eyes = eye_classifier.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 2)
            cv2.imshow('img', image)
            cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('images/Trump.jpg')

    face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
    eye_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')

    detect_face_and_eye(img, face_classifier, eye_classifier)
