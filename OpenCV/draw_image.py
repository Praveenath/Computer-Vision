import cv2
import numpy as np

# Create black image
image = np.zeros((512, 512, 3), np.uint8)

image_bw = np.zeros((512, 512), np.uint8)


def draw_line(image):
    cv2.line(image, (0, 0), (511, 511), (255, 127, 0), 5)
    cv2.imshow("Blue Line", image)


def draw_rectangle(image):
    cv2.rectangle(image, (100, 100), (300, 250), (127, 50, 127), 5)
    cv2.imshow("Rectangle", image)


def draw_circle(image):
    cv2.circle(image, (300, 350), 100, (15, 75, 50), -1)
    cv2.imshow("Circle", image)


def draw_polygon(image):
    pts = np.array([[10, 50], [400, 50], [90, 200], [50, 500]], np.int32)

    pts = pts.reshape((-1, 1, 2))

    cv2.polylines(image, [pts], True, (0, 0, 255), 3)
    cv2.imshow("Polygon", image)


def put_text(image):
    cv2.putText(image, "Hello World!", (75, 290), cv2.FONT_HERSHEY_COMPLEX, 2, (100, 170, 0), 3)
    cv2.imshow("Hello World!", image)
    

if __name__ == '__main__':
    # draw_line(image)
    # draw_rectangle(image)
    # draw_circle(image)
    # draw_polygon(image)
    put_text(image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
