import cv2
import numpy as np
import matplotlib.pyplot as plt


def clean_up_image(imgpath):

    rawImg=cv2.imread(imgpath,cv2.IMREAD_GRAYSCALE)

    # print(rawImg)
    plt.imshow(rawImg)

    plt.show()


    # normalize image
    norm=np.zeros_like(rawImg)
    norm=cv2.normalize(rawImg,norm,0,255,cv2.NORM_MINMAX)
    plt.imshow(norm)
    plt.show()

    # add threshold
    norm[norm < 70] = 0
    norm[norm>=70]=255
    plt.imshow(norm)
    plt.show()


    # close holes

    kern=np.ones((9,9),np.uint8)
    erode=cv2.erode(norm,kern,iterations=1)

    plt.imshow(erode)
    plt.show()

    dilate=cv2.dilate(erode,kern,iterations=1)

    plt.imshow(dilate)
    plt.show()

    # thres=cv2.adaptiveThreshold(norm,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,2)

    # plt.imshow(thres)
    # plt.show()



if __name__ == "__main__":
    filepath="C:/datafile/Fall2020/Senior Project/FontGenerator/TestImages/ErinnHandWrite.jpg"
    filepath_2="C:/datafile/Fall2020/Senior Project/FontGenerator/TestImages/Erinn_No_flash.jpg"

    clean_up_image(filepath)
    clean_up_image(filepath_2)







    