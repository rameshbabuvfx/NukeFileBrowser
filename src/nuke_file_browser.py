import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from ui import nuke_file_browser_ui


class NukeFileBrowser(nuke_file_browser_ui.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(NukeFileBrowser, self).__init__()
        self.setupUi(self)
        self.FileExplorerTreeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.FileExplorerTreeView.customContextMenuRequested.connect(self.context_menu)
        self.add_model()

    def add_model(self):
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())
        self.FileExplorerTreeView.setModel(self.model)
        self.FileExplorerTreeView.setSortingEnabled(True)

    def context_menu(self):
        menu = QMenu()
        menu.addAction("Open Comp")
        cursor = QCursor()
        menu.exec_(QCursor.pos())


if __name__ == '__main__':
    app = QApplication()
    window = NukeFileBrowser()
    window.show()
    sys.exit(app.exec_())
