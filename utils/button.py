from .settings import *
from .image import *
from tkinter import ttk
from tkinter import filedialog as fd

class FileButton(ttk.Button):
    
    def __init__(self, root, text, imageFrame:ImageFrame):
        super().__init__(root, text=text, command=self.select_file)
        self.__filePath = ""
        self.__imageFrame = imageFrame
       
    def select_file(self):
        filetypes = (
            ('file', '*.png'),
        )

        self.__filePath = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        
        self.updateImage()

    def filePath(self):
        return self.__filePath

    def updateImage(self):
        self.__imageFrame.addImg(self.__filePath)
