# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nuke_file_browser_ui.ui',
# licensing of 'nuke_file_browser_ui.ui' applies.
#
# Created: Sun Jun  6 15:56:02 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 647)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(4, -1, 4, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.NukeFilescheckBox = QtWidgets.QCheckBox(self.frame)
        self.NukeFilescheckBox.setChecked(False)
        self.NukeFilescheckBox.setTristate(False)
        self.NukeFilescheckBox.setObjectName("NukeFilescheckBox")
        self.horizontalLayout.addWidget(self.NukeFilescheckBox)
        self.MOVFilescheckBox = QtWidgets.QCheckBox(self.frame)
        self.MOVFilescheckBox.setObjectName("MOVFilescheckBox")
        self.horizontalLayout.addWidget(self.MOVFilescheckBox)
        self.JPGfilescheckBox = QtWidgets.QCheckBox(self.frame)
        self.JPGfilescheckBox.setObjectName("JPGfilescheckBox")
        self.horizontalLayout.addWidget(self.JPGfilescheckBox)
        self.PNGfilesCheckbox = QtWidgets.QCheckBox(self.frame)
        self.PNGfilesCheckbox.setObjectName("PNGfilesCheckbox")
        self.horizontalLayout.addWidget(self.PNGfilesCheckbox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.FileExplorerTreeView = QtWidgets.QTreeView(self.frame)
        self.FileExplorerTreeView.setStyleSheet("QTreeView { selection-background-color: lightblue}")
        self.FileExplorerTreeView.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.FileExplorerTreeView.setDragEnabled(True)
        self.FileExplorerTreeView.setWordWrap(False)
        self.FileExplorerTreeView.setObjectName("FileExplorerTreeView")
        self.gridLayout_2.addWidget(self.FileExplorerTreeView, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.NukeFilescheckBox.setText(QtWidgets.QApplication.translate("MainWindow", "*.nk", None, -1))
        self.MOVFilescheckBox.setText(QtWidgets.QApplication.translate("MainWindow", "*.mov", None, -1))
        self.JPGfilescheckBox.setText(QtWidgets.QApplication.translate("MainWindow", "*.jpg", None, -1))
        self.PNGfilesCheckbox.setText(QtWidgets.QApplication.translate("MainWindow", "*.png", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", " File Browser", None, -1))

