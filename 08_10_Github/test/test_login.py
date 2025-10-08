import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from uis.LoginMainWindowEx import LoginMainWindowEx

app=QApplication([])
login_ui=LoginMainWindowEx()
login_ui.setupUi(login_ui.MainWindow)
login_ui.MainWindow.show()
sys.exit(app.exec_())