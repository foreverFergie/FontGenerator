

class Img_storage:

    def __init__(self):
        self.lowerCase=[26]
        self.upperCase=[26]
        self.nums=[10]
        self.specialChars=[32]


    def add_char(self,imgPath, char):
        if char.isupper():
#             add img to upperCase
            ind=ord(char)-65
            self.upperCase[ind]=imgPath
        elif char.islower():
            ind=ord(char)-97
            self.lowerCase[ind]=imgPath
        elif char.isdigit():
            ind=ord(char)-48
            self.nums[ind]=imgPath
        else:
#         special chars
#         ascii values of 33-47, 58-64, 91-96, 123-126
#                           15      7   6           4  =32
            ascii=ord(char)
            # ind=0
            if 47 >= ascii >= 33:
                ind=ascii-33
            elif 64 >=ascii<=58:
                ind=(ascii-58)+15
            elif 96>=ascii<=91:
                ind=(ascii-91)+22
            else:
                ind=(ascii-123)+28
            self.specialChars[ind] = imgPath