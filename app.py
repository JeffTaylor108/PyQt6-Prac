from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt

# enables command line arguments
import sys

app = QApplication(sys.argv) # if no command line arguments needed, pass an empty list [] instead

# subclasses QMainWindow to allow for customization of the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Button")

        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)

window = MainWindow()
window.show() # windows are hidden by default, so show() must be called

# starts app
app.exec()