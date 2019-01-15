from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap

from gui import Ui_ImageViewer
from api import detectSeeds, classifySeeds
from utils import Image


class ImageHandlerApp(QMainWindow, Ui_ImageViewer):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically

        self.actionOpen_Image.triggered["bool"].connect(self.openImage)
        self.actionDetect_Seeds.triggered["bool"].connect(self.detectSeeds)
        self.actionClassify_Seeds.triggered["bool"].connect(self.classifySeeds)

    def openImage(self, trigger=False, fileName=None):
        if fileName is None:
            fileName, _ = QFileDialog.getOpenFileName(self, "Open Image",
                        "", "Image Files (*.png *.jpg *.bmp)")
        if fileName is None or fileName is "":
            return

        self.currentImage = Image(path=fileName)
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

    def showImage(self, Image):
        pixmap01 = QPixmap.fromImage(Image.QT)
        pixmap_image = QPixmap(pixmap01)
        self.label.setPixmap(pixmap_image)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setScaledContents(True)
        self.label.setMinimumSize(100, 100)
        return
