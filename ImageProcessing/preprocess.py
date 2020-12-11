import cv2
import numpy as np
import matplotlib.pyplot as plt
import os,sys
from svgtrace import trace
from pathlib import Path
# import pytesseract
import glob
import json


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
        # plt.show()

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
    # # plt.show()
    # binName="binary_"+fileName
    # cv2.imwrite(binName,dilate)

    return dilate


def convertToVector(bitmap,char,tempDir):
    """

    :param bitmap: cv2/numpy image
    :return: none?
    """
    # DIR=str(Path(__file__).resolve().parent)
    temp="temp_vector.png"
    svgName='temp/'+char+'.svg'
    cv2.imwrite(temp,bitmap)
    passPath=os.path.abspath(temp)
    svg=trace(passPath,True)
    svg_save=open(svgName,"w")
    svg_save.write(svg)
    svg_save.close()
    # print("SVG saved to: "+char+".svg")
    print('.')
    return svgName

# def getCharacter(bitmap):
#     """

#     :param bitmap:
#     :return:
#     """
#     let=pytesseract.image_to_string(bitmap,config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     print(type(let))
#     print(let[0])



def crop(binImg):
    """
    crop binary image to remove as much white background as possible
    finds the top most, bottom most, left most, and right most black value and crops out everything
    around said values
    :param binImg: binary image from clean_up_image
    :return: cropped img
    """
    # rawImg=cv2.imread(imgPath)

    # crop=binImg
    # print(binImg.shape)
    height,width =binImg.shape

    # find top most black value
    top=0
    search=True
    while search:
        black=np.any(binImg[top,:]==0)
        if black:
            search=False
        else:
            top+=1


    # find bottom most black value
    bottom=height-1
    search=True
    while search:
        black = np.any(binImg[bottom,:] == 0)
        if black:
            search = False
        else:
            bottom -= 1

    left=0
    search=True
    while search:
        black = np.any(binImg[:,left] == 0)
        if black:
            search = False
        else:
            left += 1

    right=width-1
    search=True
    while search:
        black = np.any(binImg[:,right] == 0)
        if black:
            search = False
        else:
            right -= 1

    newHeight=bottom-top+1
    newWidth=right-left+1

    # cropImg=np.zeros_like(newHeight,newWidth)

    cropImg=binImg[top:bottom+1,left:right+1]


    # plt.imshow(cropImg)
    # plt.show()
    return cropImg


def checkFileExtension(listImgs):

    """
    Check to see if imgs submitted are bitmaps or svgs
    :param listImgs: list of img filenames
    :return true if bitmaps, false if svgs

    """

    bitmaps=True

    for file in listImgs:
        dir,file=os.path.split(file)

        name,ext=os.path.splitext(file)
        if ext=='.svg':
            bitmaps=False
            break

    return bitmaps
    
def generateEmptyDictionary(empty):
    
    for elem in range(ord('!'),ord('~')):
        char=chr(elem)
        empty[char]=""
    
    


if __name__ == "__main__":
    # base=os.curdir
    # base=sys.prefix
    # print("Current directory"+base)
    #
    # print("svdsldnvlasknclndlvn'\n")
    # a_file="C:/datafile/Fall2020/Senior Project/FontGenerator/TestImages/a_erinn.jpg"
    # filepath="C:/datafile/Fall2020/Senior Project/FontGenerator/TestImages/ErinnHandWrite.jpg"
    # filepath_2="C:/datafile/Fall2020/Senior Project/FontGenerator/TestImages/Erinn_No_flash.jpg"
    #
    # bit1=clean_up_image(filepath)
    # bit2=clean_up_image(filepath_2)

    curr=os.path.dirname(os.path.realpath(__file__))

    # print(curr)
    base,fold=os.path.split(curr)

    # testUpper = "C:/datafile/Fall2020/Senior Project/FontGenerator/TestImages/IndividualGlyphs/Upper"
    # testLower = "C:/datafile/Fall2020/Senior Project/FontGenerator/TestImages/IndividualGlyphs/Lower"
    # testNums = "C:/datafile/Fall2020/Senior Project/FontGenerator/TestImages/IndividualGlyphs/nums"
    # svgTemps="C:/datafile/Fall2020/Senior Project/FontGenerator/ImageProcessing/temp"

    svgTemps=os.path.join(curr,'temp')
    testUpper=os.path.join(base,'TestImages/IndividualGlyphs/Upper')
    testLower=os.path.join(base,'TestImages/IndividualGlyphs/Lower')
    testNums=os.path.join(base,'TestImages/IndividualGlyphs/nums')
    # *********** hard coded for testing**************
    
    if not os.path.isdir(svgTemps):
        print("Creating temp directory\n")
        os.mkdir('temp')

    svgDict={}
    generateEmptyDictionary(svgDict)
    
    # print(svgDict.keys())

    # add uppercase
    
    num=65
    for imgName in glob.glob(testUpper +'/*.jpg'):
        temp=clean_up_image(imgName)
        cropped = crop(temp)
        # getCharacter(temp)
        # char=input("letter: ")

        # ************get character here from user

        # using hardcoded value for testing
        charTemp=chr(num)

        if charTemp.isupper():
            svgFile=charTemp.lower()+charTemp.lower()
        else:
            svgFile=charTemp

        save=convertToVector(cropped,svgFile,svgTemps)
        svgDict[charTemp]=save
        
        
        num+=1

     # add lowercase
    num=97
    for imgName in glob.glob(testLower +'/*.jpg'):
        temp=clean_up_image(imgName)
        cropped = crop(temp)
        # getCharacter(temp)
        # char=input("letter: ")

        # ************get character here from user

        # using hardcoded value for testing
        charTemp=chr(num)

        if charTemp.isupper():
            svgFile=charTemp.lower()+charTemp.lower()
        else:
            svgFile=charTemp

        save=convertToVector(cropped,svgFile,svgTemps)
        svgDict[charTemp]=save
        
        
        num+=1


     # add uppercase
    num=48
    for imgName in glob.glob(testNums +'/*.jpg'):
        temp=clean_up_image(imgName)
        cropped = crop(temp)
        # getCharacter(temp)
        # char=input("letter: ")

        # ************get character here from user

        # using hardcoded value for testing
        charTemp=chr(num)

        if charTemp.isupper():
            svgFile=charTemp.lower()+charTemp.lower()
        else:
            svgFile=charTemp

        save=convertToVector(cropped,svgFile,svgTemps)
        svgDict[charTemp]=save
        
        
        num+=1
    # upperSVG=glob.glob(svgTemps+"/*.svg")

    # create dictionary with filenames and what character they are

    # svgDict={}
    # generateEmptyDictionary(svgDict)

    outName={}

    outName['filename']="erinn.ttf","erinn.otf","erinn.woff"
    outName['save']='erinn'
    outName['family']='Erinn\'s Handwritting'


    # print(svgDict.items())


    # create json file

    jsonOut={}
    jsonOut['glyphs']=svgDict
    jsonOut['output']=outName


    # print(jsonOut.items())
    jsonOb=json.dumps(jsonOut,indent=4)

    with open("processedSVG.json","w") as outfile:
        outfile.write(jsonOb)
    

    os.system('cmd /k "fontforge -lang=py -script font_class.py"')    

    




    