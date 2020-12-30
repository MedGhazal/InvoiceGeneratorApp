import sys
import gui
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    application = QApplication(sys.argv)
    main_w = gui.MainWindow()
    main_w.show()
    application.quitOnLastWindowClosed()
    application.exec_()
