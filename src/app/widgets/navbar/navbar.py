import os
from PySide6.QtCore import Qt, QPropertyAnimation
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QVBoxLayout, QFrame

class Navbar(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.navbar = QFrame()
        self.navbar.setObjectName("Navbar")
        self.navbar.setMaximumWidth(60)

        # Add the buttons to the navbar

        self.animation = QPropertyAnimation(self.navbar, b"maximumWidth")
        self.animation.setDuration(300)  # milliseconds
        self.animation.setStartValue(60)
        self.animation.setEndValue(200)

        button_container = QVBoxLayout(self.navbar)
        button_container.setContentsMargins(0, 0, 0, 0)
        button_container.setSpacing(0)

        def add_button(name):
            button = QPushButton("")
            button.setObjectName(name + "Button")
            button.setFixedSize(35, 35)
            button.clicked.connect(lambda: print(f"{name} button clicked"))
            button_container.addWidget(button, alignment=Qt.AlignmentFlag.AlignHCenter)

        add_button("Gather")
        add_button("Collect")
        add_button("Kill")
        add_button("Quest")
        add_button("Planter")
        add_button("User")
        add_button("Settings")

        stylesheet = os.path.join(os.path.dirname(__file__), "navbar.qss")
        with open(stylesheet, "r") as fh:
            self.navbar.setStyleSheet(fh.read())

        layout.addWidget(self.navbar)

    def enterEvent(self, event):
            self.setCursor(Qt.CursorShape.PointingHandCursor)
            self.animation.setDirection(QPropertyAnimation.Direction.Forward)
            self.animation.start()

    def leaveEvent(self, event):
            self.setCursor(Qt.CursorShape.ArrowCursor)
            self.animation.setDirection(QPropertyAnimation.Direction.Backward)
            self.animation.start()
