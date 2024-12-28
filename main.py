from PIL import Image, ImageFilter, ImageEnhance
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem
from qt_material import apply_stylesheet
import sys
import os



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('untitled.ui', self)
        

class ImageEditor:  
    def __init__(self,):  
        self.original = None
        self.image = None  
        self.save_path = 'edited/'
        self.ui = Ui() 
        self.connects()
        self.ui.show()

    def connects(self):  
        self.ui.folder_btn.clicked.connect(self.open_folder)  
        self.ui.open_folder.triggered.connect(self.open_folder)
        self.ui.open_file.triggered.connect(self.open_file)  

    def get_images(self):
        self.folder_images = []
        if self.workdir:  
            filenames = os.listdir(self.workdir)
            for file in filenames:
                if file.endwith(".png") or file.endwith(".jpg") or file.endwith(".jpeg"):
                    self.folder_images.append(file)

    def open_folder(self):
        self.workdir = QFileDialog.getExistingDirectory()
        if self.workdir:
            self.get_images()
            self.ui.image_list.addItems(self.folder_images)

    def open_file(self):  
        file_path, _ = QFileDialog.getOpenFileName(self.ui,
                                                   "Виберіть фото", "", "Зображення (*.png *.jpg *.jpeg)")
        if file_path:
            self.open(file_path)

    def open(self, filename):  
        self.image = Image.open(filename)
        self.original = self.image

    def do_black_white(self):  
        self.image = self.image.convert("L")  # перетворити на чорно-біле  
  
    def do_blur(self):  
        self.image = self.image.filter(ImageFilter.BLUR)

    def rotate_90(self):  
        self.image = self.image.transpose(Image.ROTATE_96) #поворот
    
    def sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN) #чіткість
        

app = QApplication([])  
editor = ImageEditor()  
apply_stylesheet(app, theme='dark_pink.xml')  
app.exec_() #кінець