# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageViewer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImageViewer(object):
    def setupUi(self, ImageViewer):
        ImageViewer.setObjectName("ImageViewer")
        ImageViewer.resize(888, 655)
        self.centralwidget = QtWidgets.QWidget(ImageViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        ImageViewer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ImageViewer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 888, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        ImageViewer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ImageViewer)
        self.statusbar.setObjectName("statusbar")
        ImageViewer.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(ImageViewer)
        self.toolBar.setObjectName("toolBar")
        ImageViewer.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen_Images = QtWidgets.QAction(ImageViewer)
        self.actionOpen_Images.setObjectName("actionOpen_Images")
        self.actionOpen_Folder = QtWidgets.QAction(ImageViewer)
        self.actionOpen_Folder.setObjectName("actionOpen_Folder")
        self.menuFile.addAction(self.actionOpen_Images)
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionOpen_Images)
        self.toolBar.addAction(self.actionOpen_Folder)

        self.retranslateUi(ImageViewer)
        QtCore.QMetaObject.connectSlotsByName(ImageViewer)

    def retranslateUi(self, ImageViewer):
        _translate = QtCore.QCoreApplication.translate
        ImageViewer.setWindowTitle(_translate("ImageViewer", "MainWindow"))
        self.menuFile.setTitle(_translate("ImageViewer", "File"))
        self.toolBar.setWindowTitle(_translate("ImageViewer", "toolBar"))
        self.actionOpen_Images.setText(_translate("ImageViewer", "Open Images"))
        self.actionOpen_Images.setToolTip(_translate("ImageViewer", "Open Images"))
        self.actionOpen_Folder.setText(_translate("ImageViewer", "Open Folder"))

