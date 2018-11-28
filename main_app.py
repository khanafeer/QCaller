# -*- coding: utf-8 -*-
from PySide.QtGui import *
from controller.home import Home
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    for lppath in app.libraryPaths():
        print(lppath)
    h = Home()
    app.exec_()