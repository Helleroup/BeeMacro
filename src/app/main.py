from PySide6.QtWidgets import QApplication
from app import Root

if __name__ == "__main__":
    app = QApplication([])
    root = Root()
    root.show()
    app.exec()
