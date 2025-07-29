from PySide6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QMainWindow
from PySide6.QtCore import Qt
import widgets

class Root(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BeeMacro")
        self.setGeometry(100, 100, 860, 540)
        self.setFixedSize(860, 540)

        root = QGridLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        root.setColumnMinimumWidth(0, 60)  # Set minimum width for the first column
        root.setColumnMinimumWidth(1, 800)  # Set minimum width for the second column
        root.setRowMinimumHeight(0, 30)  # Set minimum height for the first row
        root.setRowMinimumHeight(1, 510)

        page_container = QWidget(self)
        page_layout = QGridLayout(page_container)
        page_layout.setContentsMargins(0, 0, 0, 0)  # Remove all margins
        page_layout.setSpacing(0)  # Remove spacing

        page_layout.addWidget(widgets.GatherPage())

        root.addWidget(page_container, 1, 1, 1, 1)

        overlay = QWidget(self)

        overlay_layout = QGridLayout(overlay)

        overlay_layout.setContentsMargins(0, 0, 0, 0)
        overlay_layout.setSpacing(0)

        overlay_layout.setColumnMinimumWidth(0, 60)
        overlay_layout.setColumnMinimumWidth(1, 800)
        overlay_layout.setRowMinimumHeight(0, 30)
        overlay_layout.setRowMinimumHeight(1, 510)

        overlay_layout.addWidget(widgets.Navbar(), 1, 0, 1, 2)
        overlay_layout.addWidget(widgets.Toolbar(), 0, 0, 1, 2)

        root.addWidget(overlay, 0, 0, 2, 2)

        overlay.raise_()
