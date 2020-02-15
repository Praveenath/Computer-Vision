import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')


def detect_face_and_eye(image, size=0.5):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        return image

    for (x, y, w, h) in faces:

        x = x - 50
        y = y - 50
        w = w + 50
        h = h + 50
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = image[y:y + h, x:x + w]

        eyes = eye_classifier.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    roi_color = cv2.flip(roi_color, 1)

    return roi_color


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imshow('Face Extractor', detect_face_and_eye(frame))
        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()
