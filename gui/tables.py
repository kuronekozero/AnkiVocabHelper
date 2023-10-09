import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QMessageBox, QListWidget, QDialog, QFormLayout, QComboBox

from window import MainWindow
from db import create_connection


class TableSelectionWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Select a table")

        self.table_list = QListWidget()

        self.table_list.itemDoubleClicked.connect(self.open_table)

        self.new_table_button = QPushButton("New table")
        self.new_table_button.clicked.connect(self.create_new_table)

        layout = QVBoxLayout()
        layout.addWidget(self.table_list)
        layout.addWidget(self.new_table_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.update_table_list()  # Добавьте эту строку

        self.main_window = None  # Добавьте это поле

    def create_new_table(self):
        dialog = NewTableDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            table_name = dialog.table_name_input.text()
            language = dialog.language_input.currentText()

            # Создайте новую базу данных с указанным именем таблицы
            conn = create_connection(table_name)

            # Добавьте новую таблицу в table_list
            self.update_table_list()

    def update_table_list(self):
        # Очистите table_list
        self.table_list.clear()

        # Загрузите список существующих таблиц и добавьте их в table_list
        for file in os.listdir("../gui"):
            if file.endswith(".db"):
                self.table_list.addItem(file[:-3])  # Убираем расширение .db

    def open_table(self, item):
        # Получаем имя выбранной таблицы
        table_name = item.text()

        #print(f"Opening table: {table_name}")  # Добавьте эту строку

        # Создаем и показываем MainWindow для выбранной таблицы
        self.main_window = MainWindow(table_name)  # Сохраняем ссылку на MainWindow
        self.main_window.show()

       #print("Table opened")  # Добавьте эту строку

        # Закрываем окно выбора таблицы
        self.close()

class NewTableDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("New table")

        self.table_name_input = QLineEdit()
        self.language_input = QComboBox()
        # Добавьте поддерживаемые языки в language_input
        # ...

        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.accept)

        layout = QFormLayout()
        layout.addRow("Table name:", self.table_name_input)
        layout.addRow("Language:", self.language_input)
        layout.addRow(self.create_button)

        self.setLayout(layout)

# app = QApplication(sys.argv)
# window = TableSelectionWindow()
# window.show()
# sys.exit(app.exec_())
