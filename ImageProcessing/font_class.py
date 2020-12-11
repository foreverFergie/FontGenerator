import fontforge
import json
import os,sys


"""
uses processedSVG.json file to generate .ttf file
"""



def addSVGs(fontFile,fileDict):
    temp=fontFile.createMappedChar(' ')
    
    for x,y in fileDict.items():
        glyph=fontFile.createMappedChar(x)
        
        # check to see if there is .svg file name associated with character
        if not y=="":
            

            glyph.importOutlines(y)
            glyph.removeOverlap()

        # otherwise, make empty lowercase=uppercase or vice versa
        # leave special chars empty
        else:
            # check to see if upper/lower
            if x.isupper():
                temp=x.lower()
                # get svg for lowercase
                fileTemp=fileDict.get(temp)
                glyph.importOutlines(fileTemp)
                glyph.removeOverlap()
            elif x.islower():
                temp=x.upper()
                # get svg for uppercase
                fileTemp=fileDict.get(temp)
                glyph.importOutlines(fileTemp)
                glyph.removeOverlap()
            else:
                pass


    pass

def generate(filename,font):

    name=filename.get('filename')

    if type(name) is list:
        for elem in name:
            
            font.fullname=filename.get('save')
            font.fontname=filename.get('save')
            font.familyname=filename.get('family')
            print("writing file: "+elem)
            
            font.generate(elem)
    else:

        font.fullname=filename.get('save')
        font.fontname=filename.get('save')
        font.familyname=filename.get('family')
        print("writing file: "+name)
        
        font.generate(name)
    # delete temp folder

    font.save()
    font.close()


if __name__ == "__main__":
    
    baseFont=fontforge.font()  #empty font for adding in new glyphs
    # set properties for fontforge file
    
    # open processedSVG.json file

    # with open('processedSVG.json','r') as fileDict:
    #     json.load(fileDict)

    fileDict=open('processedSVG.json','r')

    data=json.loads(fileDict.read())
    # print(type(fileDict))
    # print(data.items())
    filenames=data.get('glyphs')

    addSVGs(baseFont,filenames)

    generate(data['output'],baseFont)

    
    