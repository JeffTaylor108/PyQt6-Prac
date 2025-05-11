from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout
from PyQt6.QtCore import QSize, Qt
from random import choice

# enables command line arguments
import sys

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

app = QApplication(sys.argv) # if no command line arguments needed, pass an empty list [] instead

# subclasses QMainWindow to allow for customization of the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.times_clicked = 0
        self.setWindowTitle("My App")

        # calling self.button_is_checked creates an instance variable that can be used by any methods passing the MainWindow as a variable
        self.button_is_checked = True

        self.button = QPushButton("Button")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_was_clicked)
        self.button.clicked.connect(self.button_was_toggled)
        self.button.setChecked(self.button_is_checked)

        # creates label and input box, connecting the textChange signal of input to setText of the label to whatever is being input
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        # creates layout to add all Widgets to
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # creates parent Widget that contains everything in layout
        container = QWidget()
        container.setLayout(layout)

        self.windowTitleChanged.connect(self.window_title_changed)
        self.setFixedSize(QSize(500, 400))

        # sets window to display the container
        self.setCentralWidget(container)

    # executes on button click, changes window title to random name
    def button_was_clicked(self):
        new_window_title = choice(window_titles)
        print("setting title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)

        print("Clicked!")

    # executes on button click, checks status of button toggle
    def button_was_toggled(self, checked):
        self.button_is_checked = checked
        print("Toggle status: ", self.button_is_checked)

    # executes when window title changes, checking if window title == 'something went wrong' and disabling button if true
    def window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)

window = MainWindow()
window.show() # windows are hidden by default, so show() must be called

# starts app
app.exec()