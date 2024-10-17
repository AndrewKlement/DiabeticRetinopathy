import tkinter
from PIL import Image, ImageTk

class ImageFrame(tkinter.Frame):
    
    def __init__(self, root, width:int, height:int):
        super().__init__(root, width=width, height=height);
        self.width = width
        self.height = height
        self.pack_propagate(False)
        self.label = tkinter.Label(self)
        self.label.pack(anchor="center", fill="both", expand=True)

    def addImg(self, path:str):
        try:
            image = Image.open(path)
            image = image.resize((self.width, self.height))
            self.photo = ImageTk.PhotoImage(image)
            self.label.config(image=self.photo)

        except Exception as e:
            print(f"Error loading image: {e}")
