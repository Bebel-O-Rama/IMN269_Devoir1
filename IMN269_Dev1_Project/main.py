import math

from numpy import array
from PIL import Image
import numpy as np
import cv2

def get_tf_matrix():
    # print("For the first set of parallel lines")
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
    point1a = 79/100
    point1b = 247/100
    point2a = 231/100
    point2b = 85/100
    point3a = 92/100
    point3b = 347/100
    point4a = 224/100
    point4b = 378/100
    point5a = 450/100
    point5b = 172/100
    point6a = 231/100
    point6b = 85/100
    point7a = 392/100
    point7b = 364/100
    point8a = 266/100
    point8b = 373/100
    #
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
        image_name = "maison.jpg"
    return __file__[:-7] + "Images/Perspective/" + image_name

def apply_trans_to_image(image: np.array, matrix: np.array):
    y1, x1, z1 = np.shape(image)
    x_new_image_size = math.floor(x1 * matrix[2, 1]) + x1 + 1
    y_new_image_size = math.floor(y1 * matrix[2, 0]) + y1 + 1

    output = np.zeros((y_new_image_size, x_new_image_size, z1), image.dtype)

    for x in range(len(image)):
        for y in range(len(image[0])):
            temp = [(matrix[2, 0] * x) + x, (matrix[2, 1]*y) + y, matrix[2, 2]]
            output[math.floor(temp[0]), math.floor(temp[1])] = image[x, y]

    for x in range(len(output)):
        for y in range(len(output[0])):
            if not np.all(output[x, y, [0, 0, 0]]):
                lock_down = y != 0
                lock_left = x != 0
                lock_up = y < x_new_image_size - 1
                lock_right = x < y_new_image_size - 1

                list_average = []
                lock_down and lock_left and np.all(output[x-1, y-1, [0, 0, 0]]) and list_average.append(output[x-1, y-1])
                lock_down and np.all(output[x, y-1, [0]] != [0, 0, 0]) and list_average.append(output[x, y-1])
                lock_down and lock_right and np.all(output[x+1, y-1, [0, 0, 0]]) and list_average.append(output[x+1, y-1])
                lock_left and np.all(output[x-1, y, [0, 0, 0]]) and list_average.append(output[x-1, y])
                lock_right and np.all(output[x+1, y, [0, 0, 0]]) and list_average.append(output[x+1, y])
                lock_up and lock_left and np.all(output[x-1, y+1, [0, 0, 0]]) and list_average.append(output[x-1, y+1])
                lock_up and np.all(output[x, y+1, [0, 0, 0]]) and list_average.append(output[x, y+1])
                lock_up and lock_right and np.all(output[x+1, y+1, [0, 0, 0]]) and list_average.append(output[x+1, y+1])

                if len(list_average) != 0:
                    # print("LEN : ", len(list_average))
                    # print(output[x, y], list_average)
                    average = [0, 0, 0]
                    for i in range(len(list_average)):
                        # print("ALLO ", list_average[i])
                        average += list_average[i]
                        # print(average)
                        # average[1] += list_average[i, 1]
                        # average[2] += list_average[i, 2]
                    for j in range(0, 3):
                        average[j] = average[j]/len(list_average)
                    # print(average)
                    # print(average)
                    output[x, y] = average
    return output



im_1 = np.array(Image.open(get_image()))

H = get_tf_matrix()

# matrixTF = np.array([[-1, 0.57, 0], [0, -1, 0], [0, 0, 1]])
# test = apply_trans_to_image(im_1, H)

reworkedImage = Image.fromarray(apply_trans_to_image(im_1, H), 'RGB')

reworkedImage.save('test.jpg')
reworkedImage.show()

#reworkedImage.save("../Images/Parallèle/test.jpeg")