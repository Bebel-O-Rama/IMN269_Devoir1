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
    div = 100
    point1a = 315 / div
    point1b = 11 / div
    point2a = 102 / div
    point2b = 172 / div
    point3a = 301 / div
    point3b = 236 / div
    point4a = 108 / div
    point4b = 287 / div
    point5a = 315 / div
    point5b = 11 / div
    point6a = 500 / div
    point6b = 175 / div
    point7a = 332 / div
    point7b = 316 / div
    point8a = 500 / div
    point8b = 328 / div



    #pour carre
    # point1a = 592 / div
    # point1b = 422 / div
    # point2a = 703 / div
    # point2b = 355 / div
    # point3a = 471 / div
    # point3b = 371 / div
    # point4a = 586 / div
    # point4b = 314 / div
    # point5a = 592 / div
    # point5b = 422 / div
    # point6a = 471 / div
    # point6b = 371 / div
    # point7a = 703 / div
    # point7b = 355 / div
    # point8a = 314 / div
    # point8b = 328 / div

    # TEST
    # point1a = 79/100
    # point1b = 247/100
    # point2a = 231/100
    # point2b = 85/100
    # point3a = 92/100
    # point3b = 347/100
    # point4a = 224/100
    # point4b = 378/100
    # point5a = 450/100
    # point5b = 172/100
    # point6a = 231/100
    # point6b = 85/100
    # point7a = 392/100
    # point7b = 364/100
    # point8a = 266/100
    # point8b = 373/100
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
    vanishing_line = [vanishing_line[0] * (-1), vanishing_line[1] * (-1), abs(vanishing_line[2] * (1))]
    # vanishing_line = vanishing_line/vanishing_line[2]
    H = array([[1, 0, 0], [0, 1, 0], vanishing_line])
    print(H)
    return H


def get_image():
    # image_name = input("Enter the name of a image in the folder \"Perspective\" : ")
    # if image_name == "":
    image_name = "beau_cube.jpg"
    return __file__[:-7] + "Images/Perspective/" + image_name


def apply_trans_to_image(image: np.array, matrix: np.array):
    x1, y1, z1 = np.shape(image)

    x_new_image_size = math.floor(x1 * abs(matrix[2, 1])) + x1 + 1
    y_new_image_size = math.floor(y1 * abs(matrix[2, 0])) + y1 + 1


    rangevar = range(len(image))
    rangevar0 = range(len(image[0]))
    output = np.zeros((x_new_image_size, y_new_image_size, z1), image.dtype)

    print(matrix.transpose(1, 0))
    print(matrix.transpose(0, 1))
    for x in range(len(image)):
        for y in range(len(image[0])):
            # test1 = (matrix[2, 0] * matrix[2, 2] * matrix[2, 1])
            temp = [(((matrix[2, 1] * x)+x) / matrix[2, 2]) * x1, (((matrix[2, 0] * y) + y) / matrix[2, 2]) * y1, matrix[2, 2]]
            #temp = np.dot([x, y, 1], matrix)


            temp[0] = ((temp[0]) / (temp[2]))
            temp[1] = ((temp[1]) / (temp[2]))
            #print(temp[0], temp[1], temp[2])
            if temp[0] < x_new_image_size and temp[1] < y_new_image_size and temp[0] > -1 and temp[1] > -1:
                output[math.floor(temp[0]), math.floor(temp[1])] = image[x, y]

            # if math.floor(temp[0]) < 600 and math.floor(temp[1]) < 400:
            #     output[x, y] = image[math.floor(temp[0]), math.floor(temp[1])]

    # for x in range(len(output)):
    #     for y in range(len(output[0])):
    #         if not np.all(output[x, y, [0, 0, 0]]):
    #             lock_down = y != 0
    #             lock_left = x != 0
    #             lock_up = y < (y_new_image_size - 1)
    #             lock_right = x < (x_new_image_size - 1)
    #
    #             list_average = []
    #             lock_down and lock_left and np.all(output[x-1, y-1, [0, 0, 0]]) and list_average.append(output[x-1, y-1])
    #             lock_down and np.all(output[x, y-1, [0]] != [0, 0, 0]) and list_average.append(output[x, y-1])
    #             lock_down and lock_right and np.all(output[x+1, y-1, [0, 0, 0]]) and list_average.append(output[x+1, y-1])
    #             lock_left and np.all(output[x-1, y, [0, 0, 0]]) and list_average.append(output[x-1, y])
    #             lock_right and np.all(output[x+1, y, [0, 0, 0]]) and list_average.append(output[x+1, y])
    #             lock_up and lock_left and np.all(output[x-1, y+1, [0, 0, 0]]) and list_average.append(output[x-1, y+1])
    #             lock_up and np.all(output[x, y+1, [0, 0, 0]]) and list_average.append(output[x, y+1])
    #             lock_up and lock_right and np.all(output[x+1, y+1, [0, 0, 0]]) and list_average.append(output[x+1, y+1])
    #
    #             if len(list_average) != 0:
    #                 # print("LEN : ", len(list_average))
    #                 # print(output[x, y], list_average)
    #                 average = [0, 0, 0]
    #                 for i in range(len(list_average)):
    #                     # print("ALLO ", list_average[i])
    #                     average += list_average[i]
    #                     # print(average)
    #                     # average[1] += list_average[i, 1]
    #                     # average[2] += list_average[i, 2]
    #                 for j in range(0, 3):
    #                     average[j] = average[j]/len(list_average)
    #                 # print(average)
    #                 # print(average)
    #                 output[x, y] = average
    return output.transpose(1, 0, 2)


im_1 = np.array(Image.open(get_image())).transpose(1, 0, 2)

H = get_tf_matrix()

# matrixTF = np.array([[-1, 0.57, 0], [0, -1, 0], [0, 0, 1]])
# test = apply_trans_to_image(im_1, H)

reworkedImage = Image.fromarray(apply_trans_to_image(im_1, H), 'RGB')

reworkedImage.save('test.jpg')
reworkedImage.show()
