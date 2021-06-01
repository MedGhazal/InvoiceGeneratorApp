import sys
import gui
from PyQt5.QtWidgets import QApplication
import script_methods


if __name__ == '__main__':
    script_methods.check_path()
    application = QApplication(sys.argv)
    main_w = gui.MainWindow()
    main_w.show()
    application.quitOnLastWindowClosed()
    application.exec_()
