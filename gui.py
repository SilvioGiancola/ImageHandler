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
        ImageViewer.resize(1115, 604)
        self.centralwidget = QtWidgets.QWidget(ImageViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        ImageViewer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ImageViewer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 22))
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
        self.dockWidget_ImageHandler = QtWidgets.QDockWidget(ImageViewer)
        self.dockWidget_ImageHandler.setMaximumSize(QtCore.QSize(200, 524287))
        self.dockWidget_ImageHandler.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable)
        self.dockWidget_ImageHandler.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.dockWidget_ImageHandler.setObjectName("dockWidget_ImageHandler")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_addImages = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_addImages.setObjectName("pushButton_addImages")
        self.verticalLayout_2.addWidget(self.pushButton_addImages)
        self.pushButton_addFolder = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_addFolder.setObjectName("pushButton_addFolder")
        self.verticalLayout_2.addWidget(self.pushButton_addFolder)
        self.pushButton_removeImage = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_removeImage.setObjectName("pushButton_removeImage")
        self.verticalLayout_2.addWidget(self.pushButton_removeImage)
        self.pushButton_removeAllImages = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_removeAllImages.setObjectName("pushButton_removeAllImages")
        self.verticalLayout_2.addWidget(self.pushButton_removeAllImages)
        self.listView_listImages = QtWidgets.QListView(self.dockWidgetContents)
        self.listView_listImages.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView_listImages.setObjectName("listView_listImages")
        self.verticalLayout_2.addWidget(self.listView_listImages)
        self.dockWidget_ImageHandler.setWidget(self.dockWidgetContents)
        ImageViewer.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_ImageHandler)
        self.dockWidget_Logging = QtWidgets.QDockWidget(ImageViewer)
        self.dockWidget_Logging.setMaximumSize(QtCore.QSize(524287, 150))
        self.dockWidget_Logging.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable)
        self.dockWidget_Logging.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea)
        self.dockWidget_Logging.setObjectName("dockWidget_Logging")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser_Logging = QtWidgets.QTextBrowser(self.dockWidgetContents_2)
        self.textBrowser_Logging.setObjectName("textBrowser_Logging")
        self.gridLayout_2.addWidget(self.textBrowser_Logging, 0, 0, 1, 1)
        self.dockWidget_Logging.setWidget(self.dockWidgetContents_2)
        ImageViewer.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_Logging)
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
        self.label.setText(_translate("ImageViewer", "Image"))
        self.menuFile.setTitle(_translate("ImageViewer", "File"))
        self.menuEdit.setTitle(_translate("ImageViewer", "Edit"))
        self.toolBar.setWindowTitle(_translate("ImageViewer", "toolBar"))
        self.dockWidget_ImageHandler.setWindowTitle(_translate("ImageViewer", "Image Handler"))
        self.pushButton_addImages.setText(_translate("ImageViewer", "Add Images"))
        self.pushButton_addFolder.setText(_translate("ImageViewer", "Add Folder"))
        self.pushButton_removeImage.setText(_translate("ImageViewer", "Remove Image"))
        self.pushButton_removeAllImages.setText(_translate("ImageViewer", "Remove all Images"))
        self.dockWidget_Logging.setWindowTitle(_translate("ImageViewer", "Logging"))
        self.actionDetect_Seeds.setText(_translate("ImageViewer", "Detect Seeds"))
        self.actionClassify_Seeds.setText(_translate("ImageViewer", "Classify Seeds"))

