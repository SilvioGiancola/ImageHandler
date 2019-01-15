from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import QtCore

from gui import Ui_ImageViewer # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer


class ImageHandlerApp(QMainWindow, Ui_ImageViewer):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined
        # self.actionopen_image.
        
        self.actionOpen_Images.triggered["bool"].connect(self.openImages)
        self.actionOpen_Folder.triggered["bool"].connect(self.openFolder)

        self.list_of_images=[]

    def openImages(self):
        print("openImages")
        _translate = QtCore.QCoreApplication.translate

        fileNames, _ = QFileDialog.getOpenFileNames(self,
            "Open Images", "", "Image Files (*.png *.jpg *.bmp)");
        print(fileNames)
        self.list_of_images = fileNames



    def openFolder(self):
        print("openFolder")
        folderName = QFileDialog.getExistingDirectory(self,
            "Select directory");
        print(folderName)
        # QtGui.QFileDialog.getExistingDirectory(self, 'Select directory')

