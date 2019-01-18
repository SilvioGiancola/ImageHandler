# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageViewer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImageViewer(object):
    def setupUi(self, ImageViewer):
        ImageViewer.setObjectName("ImageViewer")
        ImageViewer.resize(471, 407)
        self.centralwidget = QtWidgets.QWidget(ImageViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_addImages = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_addImages.setObjectName("pushButton_addImages")
        self.verticalLayout.addWidget(self.pushButton_addImages)
        self.pushButton_addFolder = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_addFolder.setObjectName("pushButton_addFolder")
        self.verticalLayout.addWidget(self.pushButton_addFolder)
        self.pushButton_removeImage = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_removeImage.setObjectName("pushButton_removeImage")
        self.verticalLayout.addWidget(self.pushButton_removeImage)
        self.pushButton_removeAllImages = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_removeAllImages.setObjectName("pushButton_removeAllImages")
        self.verticalLayout.addWidget(self.pushButton_removeAllImages)
        self.listView_listImages = QtWidgets.QListView(self.verticalLayoutWidget)
        self.listView_listImages.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView_listImages.setObjectName("listView_listImages")
        self.verticalLayout.addWidget(self.listView_listImages)
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.splitter, 0, 0, 2, 2)
        ImageViewer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ImageViewer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        ImageViewer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ImageViewer)
        self.statusbar.setObjectName("statusbar")
        ImageViewer.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(ImageViewer)
        self.toolBar.setObjectName("toolBar")
        ImageViewer.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionDetect_Seeds = QtWidgets.QAction(ImageViewer)
        self.actionDetect_Seeds.setObjectName("actionDetect_Seeds")
        self.actionClassify_Seeds = QtWidgets.QAction(ImageViewer)
        self.actionClassify_Seeds.setObjectName("actionClassify_Seeds")
        self.menuEdit.addAction(self.actionDetect_Seeds)
        self.menuEdit.addAction(self.actionClassify_Seeds)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.toolBar.addAction(self.actionDetect_Seeds)
        self.toolBar.addAction(self.actionClassify_Seeds)

        self.retranslateUi(ImageViewer)
        QtCore.QMetaObject.connectSlotsByName(ImageViewer)

    def retranslateUi(self, ImageViewer):
        _translate = QtCore.QCoreApplication.translate
        ImageViewer.setWindowTitle(_translate("ImageViewer", "ImageViewer"))
        self.pushButton_addImages.setText(_translate("ImageViewer", "Add Images"))
        self.pushButton_addFolder.setText(_translate("ImageViewer", "Add Folder"))
        self.pushButton_removeImage.setText(_translate("ImageViewer", "Remove Image"))
        self.pushButton_removeAllImages.setText(_translate("ImageViewer", "Remove all Images"))
        self.label.setText(_translate("ImageViewer", "Image"))
        self.menuFile.setTitle(_translate("ImageViewer", "File"))
        self.menuEdit.setTitle(_translate("ImageViewer", "Edit"))
        self.toolBar.setWindowTitle(_translate("ImageViewer", "toolBar"))
        self.actionDetect_Seeds.setText(_translate("ImageViewer", "Detect Seeds"))
        self.actionClassify_Seeds.setText(_translate("ImageViewer", "Classify Seeds"))

