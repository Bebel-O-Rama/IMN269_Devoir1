import math

from numpy import array
from PIL import Image
import numpy as np
import cv2


def get_image():
    image_name = input("Enter the name of a image in the folder \"Perspective\" : ")
    if image_name == "":
        image_name = "P5150542.JPG"
    return __file__[:-7] + "Images/Perspective/" + image_name


def apply_trans_to_image(image: np.array, matrix: np.array):
    y1, x1, z1 = np.shape(image)
    test1 = np.zeros(image.shape, image.dtype)

    for x in range(len(image)):

        for y in range(len(image[x])):
            temp1, temp2, temp3 = np.matmul(([x, y, 1]), matrix)
            temp1 = math.floor((temp1/temp3))
            temp2 = math.floor((temp2/temp3))
            #print(temp1, temp2)
            test1[temp1, temp2] = image[x, y]

    return test1


im_1 = cv2.imread(get_image())

matrix1 = np.array([[1, 0, 0], [0, 1, 0], [0.5, 0.5, 1]])

test = apply_trans_to_image(im_1, matrix1)

cv2.imwrite("test.JPG", test)
