import os
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QVBoxLayout, QFrame
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize  # Import QSize directly

class Navbar(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.navbar = QFrame()
        self.navbar.setObjectName("Navbar")
        self.navbar.setFixedWidth(50)

        stylesheet = os.path.join(os.path.dirname(__file__), "navbar.qss")
        with open(stylesheet, "r") as fh:
            self.navbar.setStyleSheet(fh.read())

        layout.addWidget(self.navbar)
