import os
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QVBoxLayout, QFrame

class Navbar(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.navbar = QFrame()
        self.navbar.setObjectName("Navbar")
        self.navbar.setFixedWidth(50)

        # Add the buttons to the navbar

        button_container = QVBoxLayout(self.navbar)
        button_container.setContentsMargins(0, 0, 0, 0)
        button_container.setSpacing(20)

        gather_button = QPushButton("")
        gather_button.setObjectName("GatherButton")
        gather_button.setFixedSize(40, 40)
        gather_button.clicked.connect(lambda: print("Gather button clicked"))  # Placeholder for actual functionality
        button_container.addWidget(gather_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        collect_button = QPushButton("")
        collect_button.setObjectName("CollectButton")
        collect_button.setFixedSize(40, 40)
        collect_button.clicked.connect(lambda: print("Collect button clicked"))  # Placeholder for actual functionality
        button_container.addWidget(collect_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        kill_button = QPushButton("")
        kill_button.setObjectName("KillButton")
        kill_button.setFixedSize(40, 40)
        kill_button.clicked.connect(lambda: print("Kill button clicked"))  # Placeholder for actual functionality
        button_container.addWidget(kill_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        quest_button = QPushButton("")
        quest_button.setObjectName("QuestButton")
        quest_button.setFixedSize(40, 40)
        quest_button.clicked.connect(lambda: print("Quest button clicked"))  # Placeholder for actual functionality
        button_container.addWidget(quest_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        planter_button = QPushButton("")
        planter_button.setObjectName("PlanterButton")
        planter_button.setFixedSize(40, 40)
        planter_button.clicked.connect(lambda: print("Planter button clicked"))  # Placeholder for actual
        button_container.addWidget(planter_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        user_button = QPushButton("")
        user_button.setObjectName("UserButton")
        user_button.setFixedSize(40, 40)
        user_button.clicked.connect(lambda: print("User button clicked"))  # Placeholder for actual functionality
        button_container.addWidget(user_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        settings_button = QPushButton("")
        settings_button.setObjectName("SettingsButton")
        settings_button.setFixedSize(40, 40)
        settings_button.clicked.connect(lambda: print("Settings button clicked"))
        button_container.addWidget(settings_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        stylesheet = os.path.join(os.path.dirname(__file__), "navbar.qss")
        with open(stylesheet, "r") as fh:
            self.navbar.setStyleSheet(fh.read())

        layout.addWidget(self.navbar)
