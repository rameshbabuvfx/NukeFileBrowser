import sys

import nuke
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from ui import nuke_file_browser_ui



class NukeFileBrowser(nuke_file_browser_ui.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(NukeFileBrowser, self).__init__()
        self.setupUi(self)
        self.file_path = None
        self.add_model()
        self.FileExplorerTreeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.FileExplorerTreeView.customContextMenuRequested.connect(self.context_menu)
        self.FileExplorerTreeView.setColumnWidth(0, 175)

    def add_model(self):
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())
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
