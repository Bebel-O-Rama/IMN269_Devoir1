from numpy import array
from PIL import Image
import cv2


def get_image():
    image_name = input("Enter the name of a image in the folder \"Perspective\" : ")
    if image_name == "":
        image_name = "P5150542.JPG"
    return __file__[:-7] + "Images/Perspective/" + image_name


im_1 = Image.open(get_image())

im_1.show()