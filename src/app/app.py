from PySide6.QtWidgets import QWidget, QGridLayout
import widgets

class Root(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BeeMacro")
        self.setGeometry(100, 100, 860, 540)

        root = QGridLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        root.setColumnMinimumWidth(0, 60)  # Set minimum width for the first column
        root.setColumnMinimumWidth(1, 800)  # Set minimum width for the second column
        root.setRowMinimumHeight(0, 50)  # Set minimum height for the first row
        root.setRowMinimumHeight(1, 490)

        root.addWidget(widgets.Navbar(), 1, 0, 1, 1)
        # === Navbar ===
#        self.navbar = QFrame()
#        self.navbar.setFixedWidth(50)
#        self.navbar.setStyleSheet("background-color: red;")

#        navbar_layout = QVBoxLayout(self.navbar)
#        navbar_layout.setContentsMargins(0, 0, 0, 0)
#        navbar_layout.setSpacing(5)

        # Gather button
#        gather_icon = QIcon("./src/app/img/gather_icon.png")
#        self.gather_button = QPushButton()
#        self.gather_button.setFixedSize(48, 48)
#        self.gather_button.setIcon(gather_icon)
#        self.gather_button.setIconSize(QSize(48, 48))  # Use QSize directly
#        self.gather_button.setStyleSheet("background-color: blue; border: none;")
#        self.gather_button.clicked.connect(lambda: print("Gather button clicked"))  # Placeholder for actual functionality

        # Collect button
#        collect_icon = QIcon("./src/app/img/collect_icon.png")
#        self.collect_button = QPushButton()
#        self.collect_button.setFixedSize(48, 48)
#        self.collect_button.setIcon(collect_icon)
#        self.collect_button.setIconSize(QSize(48, 48))  # Use QSize directly
#        self.collect_button.setStyleSheet("background-color: blue; border: none;")
#        self.collect_button.clicked.connect(lambda: print("Collect button clicked"))  # Placeholder for actual functionality

#        navbar_layout.addWidget(self.gather_button)
#        navbar_layout.addWidget(self.collect_button)
#        navbar_layout.addStretch()

        # === Main Content Area ===
#        self.main = QFrame()
#        self.main.setStyleSheet("background-color: green;")

        # Allow main area to expand
#        root.addWidget(self.navbar)
#        root.addWidget(self.main, 1)
