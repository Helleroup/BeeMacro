import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QHBoxLayout, QFrame

class Toolbar(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.toolbar = QFrame()
        self.toolbar.setObjectName("Toolbar")
        self.toolbar.setFixedHeight(30)

        stylesheet = os.path.join(os.path.dirname(__file__), "toolbar.qss")
        with open(stylesheet, "r") as fh:
            self.toolbar.setStyleSheet(fh.read())

        layout.addWidget(self.toolbar)
