import cv2
import numpy as np

image = cv2.imread("images/blobs.jpg",0)
cv2.imshow('Original Image', image)
cv2.waitKey(0)

detector = cv2.SimpleBlobDetector()

keypoints = detector.detect(image)

blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = 'Total number of blobs: '+ str(number_of_blobs)
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 0, 255), 2)

cv2.imshow("Blobs with default parameters", blobs)
cv2.imshow(0)
cv2.destroyAllWindows()