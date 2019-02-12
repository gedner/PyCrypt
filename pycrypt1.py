# Imports
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QGridLayout, QWidget, QPlainTextEdit
from PyQt5.Qt import QLabel, QPushButton, Qt, QSize
import webbrowser


class MainWindow(QMainWindow):
    """Class for creating the main/first window"""
    def __init__(self):
        super().__init__()
        self.widgets()

    def on_click_readable(self):
        self.reaw = Readable()
        self.reaw.show()

    def on_click_unreadable(self):
        self.unreaw = Unreadable()
        self.unreaw.show()

    def email(self):
        """Opens default email-client and send email to designated contact address"""
        webbrowser.open("mailto: gorm90@gmail.com")

    def widgets(self):
        """Main function, places the widgets etc in the window, also controls window size"""
        self.setWindowTitle("PyCrypt")
        self.setMinimumSize(QSize(500, 500))
        self.setMaximumSize(QSize(500, 500))
# Adding the sub def for widgets etc
        self.add_menus_and_status()
        self.add_buttons()

    def add_menus_and_status(self):
        """Def for adding the menu and updating the statusbar"""
# Adding the statusbar and menubar
        self.statusBar().showMessage("")
        menubar = self.menuBar()
# Adding the first menu to the menubar
        menu = menubar.addMenu("Menu")
# Adding the first "choise" in the menu
        contact_action = QAction("Contact", self)
        contact_action.setStatusTip("Contact PyCrypt")
        contact_action.triggered.connect(self.email)
        menu.addAction(contact_action)
# Adding a separator line to the menu
        menu.addSeparator()
# Adding the second "choise" to the menu
        exit_action = QAction("Exit", self)  # Create an exit action
        exit_action.setStatusTip("Click to exit the application")
        exit_action.triggered.connect(self.close)  # Close application when clicked
        exit_action.setShortcut("Ctrl+Q")  # Keyboard shortcut to exit app
        menu.addAction(exit_action)

    def add_buttons(self):
        """Adding buttons and label to the window"""
# Buttons with text and the statusline update
        unreadable_button = QPushButton("Encrypt My Text")
        unreadable_button.setStatusTip("Click To Encrypt Text ")
        unreadable_button.clicked.connect(self.on_click_unreadable)
        readable_button = QPushButton("Decrypt My Text")
        readable_button.setStatusTip("Click To Decrypt Text")
        readable_button.clicked.connect(self.on_click_readable)
# Creating a label
        label_span = QLabel("Welcome to PyCrypt, please choose your action")
# Creating the grid to place buttons
        grid_layout = QGridLayout()
# Placing the buttons within the grid
        grid_layout.addWidget(unreadable_button, 5, 1)
        grid_layout.addWidget(readable_button, 5, 2)
        grid_layout.addWidget(label_span, 0, 1)
        grid_layout.setAlignment(label_span, Qt.AlignCenter)
# Create QWidget object
        layout_widget = QWidget()
        layout_widget.setLayout(grid_layout)
# Set the widget as central
        self.setCentralWidget(layout_widget)


class Readable(MainWindow):
    """Class for the decrypt window"""
    def __init__(self):
        super().__init__()

        self.add_buttons()

    def add_buttons(self):
        """Adding buttons and label to the window"""
# Creating buttons and updating statustips
        self.decrypt_button = QPushButton("Make The Text Readable")
        self.decrypt_button.setStatusTip("Click To Make The Text Readable")
# Creating the Textbox
        self.textbox = QPlainTextEdit(self)
        self.textbox.resize(400, 450)
# Creating the gridLayout and placing widgets within the window, also connects button to def
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.decrypt_button, 5, 30)
        self.decrypt_button.clicked.connect(self.de_cryptate)
        grid_layout.addWidget(self.textbox, 5, 1)
        layout_widget = QWidget()
        grid_layout.setAlignment(self.decrypt_button, Qt.AlignBottom)
        layout_widget.setLayout(grid_layout)

        self.setCentralWidget(layout_widget)

    def de_cryptate(self):

        """This is the actual decrypt process code, takes outtab1 and exchanges intab1"""

        intab1 = "abcdefghijklomnopqrstuvwxyz !,."
        outtab1 = "?2p=o)7i(u9/y&t3%r¤5e#w1q!>*'^;)"
# Fetching from written in textbox
        s = self.textbox.toPlainText()
        a = s.lower()
# Changing out the letters/numbers/etc
        crypted = (a.translate({ord(x): y for (y, x) in zip(intab1, outtab1)}))
# Clear the textbox
        self.textbox.clear()
# Write the Decrypted text
        self.textbox.setPlainText(crypted)


class Unreadable(MainWindow):
    """Class for the crypt window"""

    def __init__(self):
        super().__init__()

        self.add_buttons()

    def add_buttons(self):
        """Adding buttons and label to the window"""
# Create buttons and update statustip
        self.crypt_button = QPushButton("Make The Text Crypted")
        self.crypt_button.setStatusTip("Click To Make The Text Unreadable")
# Create the textbox
        self.textbox = QPlainTextEdit(self)
        self.textbox.resize(400, 450)
# Create the GridLayout and places the widgets within the window, also connect the button to def
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.crypt_button, 5, 30)
        self.crypt_button.clicked.connect(self.cryptate)
        grid_layout.addWidget(self.textbox, 5, 1)
        layout_widget = QWidget()
        grid_layout.setAlignment(self.crypt_button, Qt.AlignBottom)
        layout_widget.setLayout(grid_layout)

        self.setCentralWidget(layout_widget)

    def cryptate(self):

        """This is the actual cryptation code"""

        intab1 = "abcdefghijklomnopqrstuvwxyz"
        outtab1 = "?2p=o)7i(u9/y&t3%r¤5e#w1q!>)"
# Fetching the writing in textbox
        s = self.textbox.toPlainText()
        a = s.lower()
# The crypting process, replaces letters in intab1 with outtab1
        crypted = (a.translate({ord(x): y for (x, y) in zip(intab1, outtab1)}))
# Clear the textbox
        self.textbox.clear()
# Write the crypted text within textbox
        self.textbox.setPlainText(crypted)


if __name__ == "__main__":
    # Create application
    app = QApplication(sys.argv)
    # Create instance of class
    gui = MainWindow()
    # Show the constructed PyQt window
    gui.show()
    # Execute the application
    sys.exit(app.exec_())
