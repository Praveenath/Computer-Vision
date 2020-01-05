# import libraries
import cv2
import numpy as np

# Read image
image_input = cv2.imread('./images/cat.jpg')

# Display image
cv2.imshow('Image',image_input)

# Wait for keyboard input
cv2.waitKey(0)
cv2.destroyAllWindows()