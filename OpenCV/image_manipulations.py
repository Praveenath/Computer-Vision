import cv2
import numpy as np


def image_resized(img):
    scale_percent = 60
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    return resized


def translation(img):
    height, width = img.shape[:2]

    quarter_h, quarter_w = height / 4, width / 4

    #   T =     | 1 0 Tx |
    #           | 0 1 Ty |

    # Create translation matrix
    T = np.float32([[1, 0, quarter_w], [0, 1, quarter_h]])

    # Perform translation
    img_translated = cv2.warpAffine(img, T, (width, height))
    cv2.imshow('Translation', img_translated)


def rotation(img):
    height, width = img.shape[:2]

    # Define Rotation matrix
    rotation_m = cv2.getRotationMatrix2D((width / 2, height / 2), 30, 0.5)

    rotated_image = cv2.warpAffine(img, rotation_m, (width, height))

    cv2.imshow('Rotation', rotated_image)


def transpose_image(img):
    '''
    Image transpose will not generate any black pixels like rotation
    '''
    rotated = cv2.transpose(img)
    cv2.imshow('Rotation', rotated)


def scaling(img):
    '''
    Scaling, resizing and interpolation
    '''
    # resize image by 3/4 of it's dimensions
    image_scaled = cv2.resize(img, None, fx=0.75, fy=0.75)
    cv2.imshow('Scaling- Linear Interpolation', image_scaled)
    cv2.waitKey()

    img_scaled = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    cv2.imshow('Scaling- Cubic Interpolation', img_scaled)
    cv2.waitKey()

    im_scaled = cv2.resize(img, (900, 400), interpolation=cv2.INTER_AREA)
    cv2.imshow('Scaling- Skewed Size', img_scaled)


def image_pyramids(img):
    smaller = cv2.pyrDown(img)
    larger = cv2.pyrUp(img)

    cv2.imshow('Original', img)
    cv2.imshow('Smaller', smaller)
    cv2.imshow('Larger', larger)


if __name__ == '__main__':
    image = cv2.imread('./images/cat.jpg')
    img = image_resized(image)

    # translation(img)
    # rotation(img)
    # scaling(img)
    image_pyramids(img)

    cv2.waitKey()
    cv2.destroyAllWindows()
