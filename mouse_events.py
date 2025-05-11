import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)  # mouse tracking must be enabled on all widgets that could potentially block it
        self.label = QLabel("Click in this window")
        self.label.setMouseTracking(True) # enables mouse tracking so the mouseMoveEvent triggers even without first clicking
        self.setCentralWidget(self.label)

    # subclasses that override normal event handler and intercept event (e)
    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    # mousePressEvent can trigger different behavior depending on button clicked
    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mousePressEvent RIGHT")

        elif e.button() == Qt.MouseButton.XButton1:
            self.label.setText("mousePressEvent BACK")

        elif e.button() == Qt.MouseButton.XButton2:
            self.label.setText("mousePressEvent FORWARD")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()