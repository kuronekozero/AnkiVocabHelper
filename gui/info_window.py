from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, \
    QVBoxLayout, QWidget, QMessageBox, QLabel
from PyQt5.QtCore import Qt

class InfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("info")

        self.setStyleSheet("""
            QMainWindow {
                background-color: #282828;
                color: #ffffff;
            }
        """)

        title = QLabel("How to use this program.")
        title.setStyleSheet("font-size: 18pt; font-weight: bold; color: #ffffff;")

        info = QLabel("Just click on 'add' to add new word to the table. "
                      "\nif you have more than one word to add you can just write them in one line divided by spaces."
                      "\nEach word will be added to the table separately."
                      "\n"
                      "\nAfter that you can just sort the table by difficulty by clicking on 'difficulty' button."
                      "\nCongrats! Now you know what word you should add next to your anki deck!"
                      "\nCheck readme.md for more information.")
        info.setStyleSheet("font-size: 10pt; color: #ffffff;")

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(info)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
