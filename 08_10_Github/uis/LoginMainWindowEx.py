import base64
import traceback
import os
import mysql.connector
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox, QMainWindow
from PyQt5.QtCore import Qt
from .LoginMainWindow import Ui_MainWindow
from connectors.employee_connect import EmployeeConnect

class LoginMainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindow = QMainWindow()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_login.clicked.connect(self.processLogin)
    def processLogin(self):
        email = self.lineEdit_email.text()
        password = self.lineEdit_password.text()
        ec=EmployeeConnect()
        ec.connect()
        em=ec.login(email,password)
        if em==None:
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Login failed")
            msg.exec()
        else:
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Login successful")
            msg.exec()
            self.MainWindow.close()
            self.MainWindow.show()
            