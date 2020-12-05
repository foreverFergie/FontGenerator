import fontforge

class TTF:

    def __init__(self,imgStore):
        """

        :param imgStore: Img_storage object full of filepaths of SVGs
        """
        self.imgSVGs =imgStore
        self.baseFont=fontforge.font()  #empty font for adding in new glyphs


    def addSVGs(self):
        if not self.imgSVGs.lowercase.isempty():
            # add lowercase letters to font
            pass
        if not self.imgSVGs.uppercase.isempty():
            # add uppercase letters to font
            pass
        if not self.imgSVGs.nums.isempty():
            # add numbers to font
            pass

        if not self.imgSVGs.specialChars.isempty():
            # add special chars to font

            pass


    def generate(self,filename):

        

        pass


