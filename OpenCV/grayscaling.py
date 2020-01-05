# import libraries
import cv2
import numpy as np

# Read image
image_input = cv2.imread('./images/cat.jpg')

# Display image
cv2.imshow('Original', image_input)
cv2.waitKey(0)

# convert to Gray Scale
gray_image = cv2.cvtColor(image_input, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# #----------- Alternative way -------------
# image_input = cv2.imread('./images/cat.jpg', 0) # '0' indicates grayscaling
#
# cv2.imshow('Gray Image', image_input)
# cv2.waitKey(0)
# cv2.destroyAllWindows()