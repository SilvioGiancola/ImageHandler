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
        self.centralwidget = QtWidgets.QWidget(ImageViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        ImageViewer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ImageViewer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 22))
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
        self.actionOpen_Image = QtWidgets.QAction(ImageViewer)
        self.actionOpen_Image.setObjectName("actionOpen_Image")
        self.actionDetect_Seeds = QtWidgets.QAction(ImageViewer)
        self.actionDetect_Seeds.setObjectName("actionDetect_Seeds")
        self.actionClassify_Seeds = QtWidgets.QAction(ImageViewer)
        self.actionClassify_Seeds.setObjectName("actionClassify_Seeds")
        self.menuFile.addAction(self.actionOpen_Image)
        self.menuEdit.addAction(self.actionDetect_Seeds)
        self.menuEdit.addAction(self.actionClassify_Seeds)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.toolBar.addAction(self.actionOpen_Image)
        self.toolBar.addAction(self.actionDetect_Seeds)
        self.toolBar.addAction(self.actionClassify_Seeds)

        self.retranslateUi(ImageViewer)
        QtCore.QMetaObject.connectSlotsByName(ImageViewer)

    def retranslateUi(self, ImageViewer):
        _translate = QtCore.QCoreApplication.translate
        ImageViewer.setWindowTitle(_translate("ImageViewer", "ImageViewer"))
        self.label.setText(_translate("ImageViewer", "Image"))
        self.menuFile.setTitle(_translate("ImageViewer", "File"))
        self.menuEdit.setTitle(_translate("ImageViewer", "Edit"))
        self.toolBar.setWindowTitle(_translate("ImageViewer", "toolBar"))
        self.actionOpen_Image.setText(_translate("ImageViewer", "Open Image"))
        self.actionOpen_Image.setToolTip(_translate("ImageViewer", "Open Image"))
        self.actionDetect_Seeds.setText(_translate("ImageViewer", "Detect Seeds"))
        self.actionClassify_Seeds.setText(_translate("ImageViewer", "Classify Seeds"))

