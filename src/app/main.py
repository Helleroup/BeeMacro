import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from app import Root

if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon("./src/app/img/icons/logo.png"))

    root = Root()
    root.show()
    app.exec()
