import cv2
import numpy as np
import matplotlib.pyplot as plt
import os,sys
from svgtrace import trace
from pathlib import Path
import pytesseract
# import fontforge
import font_class
import fontTools


def clean_up_image(imgpath,showResults=False):
    """

    :param imgpath: abs path to image
    :param showResults: boolean for whether to show images as it is processed
    :return: binary image
    """

    fileName=os.path.split(imgpath)[1]
    rawImg=cv2.imread(imgpath,cv2.IMREAD_GRAYSCALE)

    if showResults:
    # print(rawImg)
        plt.imshow(rawImg)

        plt.show()


    # normalize image
    norm=np.zeros_like(rawImg)
    norm=cv2.normalize(rawImg,norm,0,255,cv2.NORM_MINMAX)

    if showResults:
        plt.imshow(norm)
        plt.show()

    gaus=cv2.GaussianBlur(norm,(9,9),0)

    if showResults:
        plt.imshow(gaus)
        plt.show()

    # add threshold
    gaus[gaus < 80] = 0
    gaus[gaus>=80]=255

    if showResults:
        plt.imshow(gaus)
        plt.show()


    # close holes

    kern=np.ones((9,9),np.uint8)
    erode=cv2.erode(gaus,kern,iterations=1)

    if showResults:
        plt.imshow(erode)
        plt.show()

    dilate=cv2.dilate(erode,kern,iterations=1)

    if showResults:
        plt.imshow(dilate)
        plt.show()

    # thres=cv2.adaptiveThreshold(norm,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,2)

    # plt.imshow(thres)
    # plt.show()
    binName="binary_"+fileName
    cv2.imwrite(binName,dilate)

    return dilate


def convertToVector(bitmap):
    """

    :param bitmap: cv2/numpy image
    :return: none?
    """
    # DIR=str(Path(__file__).resolve().parent)
    temp="temp_vector.png"
    cv2.imwrite(temp,bitmap)
    passPath=os.path.abspath(temp)
    svg=trace(passPath,True)
    svg_save=open("temp.svg","w")
    svg_save.write(svg)
    svg_save.close()
    print("SVG saved to: temp.svg")

def getCharacter(bitmap):
    """

    :param bitmap:
    :return:
    """

    print(pytesseract.image_to_string(bitmap))


def crop(imgPath):
    """

    :param imgPath:
    :return:
    """
    rawImg=cv2.imread(imgPath)


#     get coordinates from web gui

    (x,y)=(0,0)
    (height,width)=(200,200)




if __name__ == "__main__":
    base=os.curdir
    # base=sys.prefix
    # print("Current directory"+base)

    # print("svdsldnvlasknclndlvn'\n")
    # a_file="C:/datafile/Fall2020/Senior Project/FontGenerator/TestImages/a_erinn.jpg"
    # filepath="C:/datafile/Fall2020/Senior Project/FontGenerator/TestImages/ErinnHandWrite.jpg"
    # filepath_2="C:/datafile/Fall2020/Senior Project/FontGenerator/TestImages/Erinn_No_flash.jpg"
    #
    # bit1=clean_up_image(filepath)
    # bit2=clean_up_image(filepath_2)
    # a=clean_up_image(a_file,True)
    # getCharacter(a)
    #
    #
    # convertToVector(bit1)
    test="C:/Users/fergusone1/Downloads/Kitten-Thin-19464/Web Fonts/Kitten Thin/Kitten-Thin.ttf"


    fontTools.







    