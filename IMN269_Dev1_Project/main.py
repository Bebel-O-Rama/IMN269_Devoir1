import math

from numpy import array
from PIL import Image
import numpy as np
import cv2

def get_tf_matrix():
    print("For the first set of parallel lines")
    # print("The first line")
    # point1a = float(input("Insert the \"x\" coordinate of the first point  : "))
    # point1b = float(input("The \"y\" coordinate of that point : "))
    # point2a = float(input("Insert the \"x\" coordinate of the second point : "))
    # point2b = float(input("The \"y\" coordinate of that point : "))
    # print("The second line")
    # point3a = int(input("Insert the \"x\" coordinate of the first point  : "))
    # point3b = int(input("The \"y\" coordinate of that point : "))
    # point4a = int(input("Insert the \"x\" coordinate of the second point : "))
    # point4b = int(input("The \"y\" coordinate of that point : "))
    # print("For the second set of parallel lines")
    # print("The first line")
    # point5a = int(input("Insert the \"x\" coordinate of the first point  : "))
    # point5b = int(input("The \"y\" coordinate of that point : "))
    # point6a = int(input("Insert the \"x\" coordinate of the second point : "))
    # point6b = int(input("The \"y\" coordinate of that point : "))
    # print("The second line")
    # point7a = int(input("Insert the \"x\" coordinate of the first point  : "))
    # point7b = int(input("The \"y\" coordinate of that point : "))
    # point8a = int(input("Insert the \"x\" coordinate of the second point : "))
    # point8b = int(input("The \"y\" coordinate of that point : "))
    #
    # line1 = np.cross([point1a, point1b, 1], [point2a, point2b, 1])
    # line2 = np.cross([point3a, point3b, 1], [point4a, point4b, 1])
    # line3 = np.cross([point5a, point5b, 1], [point6a, point6b, 1])
    # line4 = np.cross([point7a, point7b, 1], [point8a, point8b, 1])
    #
    # vanishing_point1 = np.cross(line1, line2)
    # vanishing_point2 = np.cross(line3, line4)
    #
    # vanishing_line = np.cross(vanishing_point1, vanishing_point2)
    # print(vanishing_line)
    #
    # print(line1)

    # TEST
    point1a = 315/100
    point1b = 11/100
    point2a = 102/100
    point2b = 172/100
    point3a = 301/100
    point3b = 236/100
    point4a = 108/100
    point4b = 287/100
    point5a = 315/100
    point5b = 11/100
    point6a = 500/100
    point6b = 175/100
    point7a = 332/100
    point7b = 316/100
    point8a = 500/100
    point8b = 328/100

    line1 = np.cross([point1a, point1b, 1], [point2a, point2b, 1])
    line2 = np.cross([point3a, point3b, 1], [point4a, point4b, 1])
    line3 = np.cross([point5a, point5b, 1], [point6a, point6b, 1])
    line4 = np.cross([point7a, point7b, 1], [point8a, point8b, 1])
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    vanishing_point1 = np.cross(line1, line2)
    vanishing_point2 = np.cross(line3, line4)
    print(vanishing_point1)
    print(vanishing_point2)
    vanishing_line = np.cross(vanishing_point1, vanishing_point2)
    print(vanishing_line)
    vanishing_line = [abs(vanishing_line[0]/vanishing_line[2]), abs(vanishing_line[1]/vanishing_line[2]), abs(vanishing_line[2]/vanishing_line[2])]
    H = array([[1, 0, 0], [0, 1, 0], vanishing_line])
    print(H)
    return H

def get_image():
    image_name = input("Enter the name of a image in the folder \"Perspective\" : ")
    if image_name == "":
        image_name = "beau_cube.jpg"
    return __file__[:-7] + "Images/Perspective/" + image_name

def apply_trans_to_image(image: np.array, matrix: np.array):
    y1, x1, z1 = np.shape(image)
    print(y1, "  ", matrix[2, 1])
    print(x1, "  ", matrix[2, 0])
    print(z1)
    x_new_image_size = math.floor(x1 * matrix[2, 1]) + x1 + 1
    y_new_image_size = math.floor(y1 * matrix[2, 0]) + y1 + 1
    print(x_new_image_size)
    print(y_new_image_size)
    test1 = np.zeros((y_new_image_size, x_new_image_size, z1), image.dtype)

    for x in range(len(image)):

        for y in range(len(image[0])):
            temp = [(matrix[2, 0] * x) + x, (matrix[2, 1]*y) + y, matrix[2, 2]]
            test1[math.floor(temp[0]), math.floor(temp[1])] = image[x, y]

    # test1 = np.dot(image, matrix)

    return test1



im_1 = np.array(Image.open(get_image()))

H = get_tf_matrix()

# matrixTF = np.array([[-1, 0.57, 0], [0, -1, 0], [0, 0, 1]])
# test = apply_trans_to_image(im_1, H)

reworkedImage = Image.fromarray(apply_trans_to_image(im_1, H), 'RGB')

reworkedImage.save('test.jpg')
reworkedImage.show()

#reworkedImage.save("../Images/Parallèle/test.jpeg")