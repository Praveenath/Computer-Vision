import cv2
import numpy as np

car_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_car.xml')

cap = cv2.VideoCapture('images/cars.avi')

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    bodies = car_classifier.detectMultiScale(gray, 1.2, 3)

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.imshow('Cars', frame)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
