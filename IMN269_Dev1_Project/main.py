import math

from numpy import array
from PIL import Image
import numpy as np

def get_tf_matrix():
    # List of points for the image "beau_cube.jpg
    point1a = 315/100
    point1b = 11/100
    point2a = 102/100
    point2b = 172/100
    point3a = 316/100
    point3b = 370/100
    point4a = 104/100
    point4b = 360/100
    point5a = 315/100
    point5b = 11/100
    point6a = 500/100
    point6b = 175/100
    point7a = 317/100
    point7b = 371/100
    point8a = 503/100
    point8b = 355/100

    line1 = np.cross([point1a, point1b, 1], [point2a, point2b, 1])
    line2 = np.cross([point3a, point3b, 1], [point4a, point4b, 1])
    line3 = np.cross([point5a, point5b, 1], [point6a, point6b, 1])
    line4 = np.cross([point7a, point7b, 1], [point8a, point8b, 1])
    vanishing_point1 = np.cross(line1, line2)
    vanishing_point2 = np.cross(line3, line4)
    print("The first vanishing point : ", vanishing_point1)
    print("The second vanishing point : ", vanishing_point2)
    vanishing_line = np.cross(vanishing_point1, vanishing_point2)
    print("The vanishing line : ", vanishing_line)
    vanishing_line = [abs(vanishing_line[0]/vanishing_line[2]), abs(vanishing_line[1]/vanishing_line[2]), abs(vanishing_line[2]/vanishing_line[2])]
    H = array([[1, 0, 0], [0, 1, 0], vanishing_line])
    print("The H matrix normalized with z = 1")
    print(H)
    return H

def get_image():
    print("This program will remove the perspective of the image \"beau_cube.jpg\"")
    print("The program might take a minute or two")
    return __file__[:-7] + "beau_cube.jpg"

def apply_trans_to_image(image: np.array, matrix: np.array):
    y1, x1, z1 = np.shape(image)
    x_new_image_size = math.floor(x1 * matrix[2, 1]) + x1 + 1
    y_new_image_size = math.floor(y1 * matrix[2, 0]) + y1 + 1

    output = np.zeros((y_new_image_size, x_new_image_size, z1), image.dtype)


    print("The program is now repairing the image with the matrix H")
    for x in range(len(image)):
        for y in range(len(image[0])):
            temp = [(matrix[2, 0] * x) + x, (matrix[2, 1]*y) + y, matrix[2, 2]]
            output[math.floor(temp[0]), math.floor(temp[1])] = image[x, y]

    print("The program is now interpolating the image to remove any holes that could have appeared during the last step")
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
                    average = [0, 0, 0]
                    for i in range(len(list_average)):
                        average += list_average[i]
                    for j in range(0, 3):
                        average[j] = average[j]/len(list_average)
                    output[x, y] = average
    return output



im_1 = Image.open(get_image())
im_1 = np.array(im_1)

H = get_tf_matrix()

reworkedImage = Image.fromarray(apply_trans_to_image(im_1, H), 'RGB')
print("The image has been saved under the name \"beau_cube_paral.jpg\"")
reworkedImage.save('beau_cube_paral.jpg')
reworkedImage.show()