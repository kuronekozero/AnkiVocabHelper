from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, \
    QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtCore import Qt
import sys

from db import add_word, create_connection, get_all_words, create_table, delete_word, add_column, column_exists, word_exists
from twinword import get_word_difficulty
from info_window import InfoWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.setStyleSheet("""
            QMainWindow {
                background-color: #282828;
                color: #ffffff;
            }
            QPushButton {
                background-color: #333333;
                color: #ffffff;
            }
            QPushButton:hover {
                background-color: #555555;
            }
            QLineEdit {
                background-color: #333333;
                color: #ffffff;
            }
            QTableWidget {
                background-color: #333333;
                color: #ffffff;
            }
            QHeaderView::section {
                background-color: #333333;
                color: #ffffff;
            }
            QTableCornerButton::section {
                background-color: #333333;
                border: none;
            }
            QTableView {
                gridline-color: #333333;
            }
        """)

        self.word_sort_order = 0
        self.difficulty_sort_order = 0
        self.date_sort_order = 0

        # Устанавливаем размер окна
        self.setGeometry(100, 100, 800, 600)  # параметры: x, y, width, height

        # Создаем подключение к базе данных
        self.conn = create_connection()

        # Создаем таблицу, если она еще не существует
        create_table(self.conn)

        # Добавляем новый столбец, если он еще не существует
        if not column_exists(self.conn, "date_added"):
            add_column(self.conn)

        # Создаем виджеты
        self.word_input = QLineEdit()
        self.add_button = QPushButton("Add")

        # Подключаем обработчик события нажатия кнопки
        self.add_button.clicked.connect(self.add_word)

        # Подключаем обработчик события нажатия клавиши Enter
        self.word_input.returnPressed.connect(self.add_word)

        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(["Words", "Difficulty", "Controls"])

        # Получаем горизонтальный заголовок таблицы
        header = self.table.horizontalHeader()

        # Устанавливаем растяжение последнего столбца
        header.setStretchLastSection(True)

        self.table.horizontalHeader().sectionClicked.connect(
            self.sort_table)  # подключаем обработчик события нажатия на заголовок столбца

        # Устанавливаем начальный размер таблицы
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 100)

        # Подключаем обработчик события клика по элементу таблицы
        self.table.itemClicked.connect(self.handle_item_clicked)

        # Создаем компоновку и добавляем в нее виджеты
        layout = QVBoxLayout()
        layout.addWidget(self.word_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.table)

        self.info_button = QPushButton("i")
        self.info_button.clicked.connect(self.show_info)
        layout.addWidget(self.info_button)
        self.info_button.setFixedSize(30, 30)  # параметры: ширина, высота

        # Создаем центральный виджет и устанавливаем его в окне
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_word(self):
        words = self.word_input.text().split()
        for word in words:
            if word_exists(self.conn, word):
                # Создаем и показываем QMessageBox
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f'Word "{word}" already exists in the table.')
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                difficulty = get_word_difficulty(word)
                add_word(self.conn, word, difficulty)
        self.update_table()
        self.word_input.clear()

    def update_table(self):
        words = get_all_words(self.conn)

        self.table.setRowCount(len(words))
        self.table.setColumnCount(4)  # Устанавливаем количество столбцов в таблице
        self.table.setHorizontalHeaderLabels(
            ["Words", "Difficulty", "Date", "Controls"])  # Устанавливаем заголовки столбцов

        for i, (id, word, frequency, date_added) in enumerate(words):
            self.table.setItem(i, 0, QTableWidgetItem(word))
            self.table.setItem(i, 1, NumericTableWidgetItem(str(frequency)))  # Используем NumericTableWidgetItem здесь
            self.table.setItem(i, 2, QTableWidgetItem(date_added))

            # Создаем кнопку "Удалить"
            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda checked, word=word: self.delete_word(word))

            # Добавляем кнопку в таблицу
            self.table.setCellWidget(i, 3, delete_button)

        # Устанавливаем ширину столбцов
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 200)

    def handle_item_clicked(self, item):
        # Проверяем, является ли элемент кнопкой "Удалить"
        if item.column() == 2 and item.text() == "Delete":
            # Получаем слово из таблицы
            word = self.table.item(item.row(), 0).text()

            # Удаляем слово из базы данных
            delete_word(self.conn, word)

            # Обновляем таблицу
            self.update_table()

    def delete_word(self, word):
        # Удаляем слово из базы данных
        delete_word(self.conn, word)

        # Обновляем таблицу
        self.update_table()

    def sort_table(self, column):
        if column == 0:
            if self.word_sort_order == 0:
                # Сортируем слова в алфавитном порядке
                self.word_sort_order = 1
            elif self.word_sort_order == 1:
                # Сортируем слова в обратном алфавитном порядке
                self.word_sort_order = -1
            else:
                # Возвращаемся к исходному порядку
                self.word_sort_order = 0

            self.sort_words(self.word_sort_order)

        elif column == 1:
            if self.difficulty_sort_order == 0:
                # Сортируем по сложности от легких к сложным
                self.difficulty_sort_order = 1
            elif self.difficulty_sort_order == 1:
                # Сортируем по сложности от сложных к легким
                self.difficulty_sort_order = -1
            else:
                # Возвращаемся к исходному порядку
                self.difficulty_sort_order = 0

            self.sort_difficulty(self.difficulty_sort_order)

        elif column == 2:
            if self.date_sort_order == 0:
                # Сортируем по дате от ранних к поздним
                self.date_sort_order = 1
            elif self.date_sort_order == 1:
                # Сортируем по дате от поздних к ранним
                self.date_sort_order = -1
            else:
                # Возвращаемся к исходному порядку
                self.date_sort_order = 0

            self.sort_date(self.date_sort_order)

        # Store the current sort column and order
        self.current_sort_column = column
        if column == 0:
            self.current_sort_order = Qt.AscendingOrder if self.word_sort_order == 1 else Qt.DescendingOrder
        elif column == 1:
            self.current_sort_order = Qt.AscendingOrder if self.difficulty_sort_order == 1 else Qt.DescendingOrder
        elif column == 2:
            self.current_sort_order = Qt.AscendingOrder if self.date_sort_order == 1 else Qt.DescendingOrder

    def sort_date(self, order):
        if order == 0:
            # Сортируем по дате от ранних к поздним
            self.table.sortItems(2, Qt.AscendingOrder)
        elif order == 1:
            # Сортируем по дате от поздних к ранним
            self.table.sortItems(2, Qt.DescendingOrder)

    def sort_words(self, order):
        if order == 0:
            # Сортируем слова в алфавитном порядке
            self.table.sortItems(0, Qt.AscendingOrder)
        elif order == 1:
            # Сортируем слова в обратном алфавитном порядке
            self.table.sortItems(0, Qt.DescendingOrder)

    def sort_difficulty(self, order):
        if order == 0:
            # Сортируем по сложности от легких к сложным
            self.table.sortItems(1, Qt.AscendingOrder)
        elif order == 1:
            # Сортируем по сложности от сложных к легким
            self.table.sortItems(1, Qt.DescendingOrder)

    def show_info(self):
        self.info_window = InfoWindow()
        self.info_window.show()


class NumericTableWidgetItem(QTableWidgetItem):
    def __lt__(self, other):
        return float(self.text()) < float(other.text())

# Создаем приложение и главное окно
app = QApplication(sys.argv)
window = MainWindow()
window.update_table()
window.show()

# Запускаем цикл обработки событий приложения
sys.exit(app.exec_())
