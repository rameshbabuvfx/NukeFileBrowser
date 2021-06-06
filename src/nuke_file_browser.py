import sys

# import nuke
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from ui import nuke_file_browser_ui


class NukeFileBrowser(nuke_file_browser_ui.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(NukeFileBrowser, self).__init__()
        self.setupUi(self)
        self.file_path = None
        self.ext_list = []
        self.add_model()
        self.connect_ui()
        self.FileExplorerTreeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.FileExplorerTreeView.customContextMenuRequested.connect(self.context_menu)
        self.FileExplorerTreeView.setColumnWidth(0, 175)

    def connect_ui(self):
        self.NukeFilescheckBox.clicked.connect(self.create_ext_list)
        self.MOVFilescheckBox.clicked.connect(self.create_ext_list)
        self.PNGfilesCheckbox.clicked.connect(self.create_ext_list)
        self.JPGfilescheckBox.clicked.connect(self.create_ext_list)

    def create_ext_list(self):
        self.ext_list.clear()
        nuke_files = self.NukeFilescheckBox.isChecked()
        if nuke_files:
            self.ext_list.append(self.NukeFilescheckBox.text())
        mov_files = self.MOVFilescheckBox.isChecked()
        if mov_files:
            self.ext_list.append(self.MOVFilescheckBox.text())
        png_files = self.PNGfilesCheckbox.isChecked()
        if png_files:
            self.ext_list.append(self.PNGfilesCheckbox.text())
        jpg_files = self.JPGfilescheckBox.isChecked()
        if jpg_files:
            self.ext_list.append(self.JPGfilescheckBox.text())
        print(self.ext_list)
        self.add_model()

    def add_model(self):
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())
        self.model.setNameFilters(self.ext_list)
        self.model.setNameFilterDisables(False)
        self.FileExplorerTreeView.setModel(self.model)
        self.FileExplorerTreeView.setSortingEnabled(True)
        self.FileExplorerTreeView.clicked.connect(self.selected_file_path)

    def context_menu(self):
        menu = QMenu()
        open_comp = menu.addAction("Open Comp")
        open_comp.triggered.connect(self.open_workfile)
        menu.exec_(QCursor.pos())

    def selected_file_path(self, index):
        self.file_path = self.model.filePath(index)

    def open_workfile(self):
        nuke.scriptOpen(self.file_path)


if __name__ == '__main__':
    app = QApplication()
    window = NukeFileBrowser()
    window.show()
    sys.exit(app.exec_())
