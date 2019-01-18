from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
# from PyQt5 import QStandardItemModel
from PyQt5.QtGui import QStandardItemModel


from gui import Ui_ImageViewer
from api import detectSeeds, classifySeeds
from utils import Image
import os


class ImageHandlerApp(QMainWindow, Ui_ImageViewer):

    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super().__init__()
        self.setupUi(self)  # This is defined in design.py file automatically

        self.model = QStandardItemModel(self.listView_listImages)
        self.listView_listImages.doubleClicked.connect(self.on_item_changed)

        self.currentImage = None

        self.actionDetect_Seeds.triggered["bool"].connect(self.detectSeeds)
        self.actionClassify_Seeds.triggered["bool"].connect(self.classifySeeds)

        self.pushButton_addImages.clicked["bool"].connect(self.addImages)
        self.pushButton_removeImage.clicked["bool"].connect(
            self.removeCurrentImage)
        self.pushButton_addFolder.clicked["bool"].connect(self.addFolder)
        self.pushButton_removeAllImages.clicked["bool"].connect(
            self.removeAllImages)

    def openImage(self, trigger=False, fileName=None):
        if fileName is None:
            fileName, _ = QFileDialog.getOpenFileName(
                self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if fileName is None or fileName is "":
            return

        self.currentImage = Image(path=fileName)
        self.showImage(self.currentImage)

        return

    def addImage(self, trigger=False, fileName=None):
        if fileName is None:
            fileName, _ = QFileDialog.getOpenFileName(
                self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if fileName is None or fileName is "":
            return

        self.model.appendRow(Image(path=fileName))
        self.listView_listImages.setModel(self.model)

        return

    def addImages(self, trigger=False, fileNames=None):
        if fileNames is None:
            fileNames, _ = QFileDialog.getOpenFileNames(
                self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if fileNames is None or fileNames is []:
            return

        for fileName in fileNames:
            self.addImage(fileName=fileName)

        return

    def addFolder(self, trigger=False, folder=None):
        if folder is None:
            folder = QFileDialog.getExistingDirectory(
                self, "Select Folder", "")
        print(folder)
        valid_images = [".jpg", ".gif", ".png", ".tga"]
        for f in os.listdir(folder):
            ext = os.path.splitext(f)[1]
            if ext.lower() not in valid_images:
                continue

            self.addImage(fileName=os.path.join(folder, f))

        return

    def removeCurrentImage(self, trigger=False):
        # for item in model.findItems('something'):
        self.model.removeRow(self.currentImage.row())
        self.listView_listImages.setModel(self.model)
        self.showImage()

    def removeAllImages(self, trigger=False):
        print("removeAllImages")
        print(self.model.rowCount())
        self.model.removeRows(0, self.model.rowCount())
        self.listView_listImages.setModel(self.model)
        self.showImage()

    def on_item_changed(self, index):
        print("on_item_changed")
        self.currentImage = self.model.itemFromIndex(index)
        self.showImage(self.currentImage)

        return

    def detectSeeds(self):
        resultimage, good_cnt = detectSeeds(self.currentImage.CV)
        self.showImage(Image(cv_img=resultimage))
        return

    def classifySeeds(self):
        resultimage = classifySeeds(self.currentImage.CV)
        self.showImage(Image(cv_img=resultimage))
        return

    def showImage(self, Image=None):
        if Image is None:
            self.label.setText("Image")
            return

        pixmap01 = QPixmap.fromImage(Image.QT)
        pixmap_image = QPixmap(pixmap01)
        self.label.setPixmap(pixmap_image)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setScaledContents(True)
        self.label.setMinimumSize(100, 100)
        return
