import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow
from MainWindowEx import MainWindowEx

def main():
    app = QApplication(sys.argv)
    
    # Tạo MainWindow
    main_window = QMainWindow()
    
    # Tạo MainWindowEx và setup UI
    ui = MainWindowEx()
    ui.setupUi(main_window)
    
    # Hiển thị cửa sổ
    main_window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
