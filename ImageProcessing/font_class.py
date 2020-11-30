import fontforge

class TTF:

    def __init__(self,imgStore):
        """

        :param imgStore: Img_storage object full of filepaths of SVGs
        """
        self.imgSVGs =imgStore
        self.baseFont=fontforge.font()  #empty font for adding in new glyphs


    def addSVGs(self):
        pass


    def generate(self,filename):

        

        pass


