import os
from PySide6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QMainWindow, QScrollArea, QLabel, QSizePolicy
from PySide6.QtCore import Qt

class GatherPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gather Page")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove all margins
        layout.setSpacing(0)  # Remove spacing

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        # This ensures the content widget expands to full width
        content_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        # Add content to the content_layout
        for i in range(50):
            label = QLabel(f"Item {i + 1}")
            content_layout.addWidget(label)

        content_layout.addStretch(1)

        scroll_area.setWidget(content_widget)

        layout.addWidget(scroll_area)

        stylesheet = os.path.join(os.path.dirname(__file__), "gather.qss")
        with open(stylesheet, "r") as fh:
            scroll_area.setStyleSheet(fh.read())
