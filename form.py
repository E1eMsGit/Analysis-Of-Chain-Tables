import os

from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtWidgets import QMessageBox, QWidget, QFileDialog, QLabel, \
    QListWidget, QAbstractItemView

import form_deisgn
import functions
from icons import *


class MainWindow(QWidget):
    """
    Главное окно.
    """

    def __init__(self):
        """
        Инициализация графического интерфейса и сигнал-слотов
        """
        QWidget.__init__(self)

        self.developers_file_content = dict()
        self.constructors_file_content = dict()

        self.ui = form_deisgn.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/images/chip_icon.png"))

        self.ui.result_label.setVisible(False)

        self.ui.open_developers_file_button.clicked.connect(
            self.open_developers_file_dialog)
        self.ui.open_constructors_file_button.clicked.connect(
            self.open_constructors_file_dialog)
        self.ui.comparison_button.clicked.connect(self.file_comparison)

        self.ui.developers_list_widget.itemClicked.connect(
            self.on_developers_list_widget_item_clicked)
        self.ui.constructors_list_widget.itemClicked.connect(
            self.on_constructors_list_widget_item_clicked)

    def closeEvent(self, event):
        """
        Обработка закрытия окна.
        :param event:
        :return:
        """
        result = QMessageBox.question(
            self,
            self.windowTitle(),
            "Закрыть программу?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if result == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def open_file(self, dictionary: dict, list_widget: QListWidget,
                  label_widget: QLabel):
        """
        Диалоговое окно открытия файла.
        Получает имя файла, заменяет в тексте символ "," на "-",
        преобразует содержимое файла в словарь, заполняет list widget,
        проверяет открыты ли оба файла.
        :return:
        """
        file_path = QFileDialog.getOpenFileName(self, 'Открыть файл')[0]
        dictionary.clear()

        if file_path != "":
            file_content = ""
            list_widget.clear()
            label_widget.setText(os.path.basename(file_path))

            with open(file_path, 'r', encoding='cp1251') as f:
                for line in f.readlines():
                    file_content += line.replace(',', '-')

            dictionary.update(functions.make_dict(file_content))

            self.fill_list_widget(dictionary, list_widget)

            self.check_list_widgets_count()

    def check_list_widgets_count(self):
        """
        Проверяет открыты ли оба файла.
        :return:
        """
        if self.ui.developers_list_widget.count() > 0 and \
                self.ui.constructors_list_widget.count() > 0:
            self.ui.comparison_button.setEnabled(True)

    def fill_list_widget(self, dictionary: dict,
                         list_widget: QListWidget, counter=None):
        """
        Заполняет list widget словарем.
        :param dictionary: Словарь.
        :param list_widget: Объект list widget
        :param counter: Счетчик (только для поиска несовпадений).
        :return:
        """
        for key in sorted(dictionary):
            list_widget.addItem(key)
            items = list_widget.findItems(key, QtCore.Qt.MatchExactly)

            if len(items) > 0:
                for item in items:
                    item.setFont(QFont("Serif", 10, QFont.Bold))

            for i in sorted(dictionary[key]):
                list_widget.addItem(i)
                if counter is not None:
                    counter[0] += 1

            list_widget.addItem('')

    def find_list_widget_item(self, list_widget: QListWidget):
        """
        Находит и окрашивает выбраный в списке несовпадений элемент
        в заданном списке.
        :param list_widget: Виджет списка.
        :return:
        """
        if self.sender().currentItem().text() != '':
            for index in range(list_widget.count()):
                list_widget.item(index).setBackground(QColor(255, 255, 255))

            items = list_widget.findItems(
                self.sender().currentItem().text(),
                QtCore.Qt.MatchExactly)

            if len(items) > 0:
                for item in items:
                    item.setBackground(QColor("red"))
                    list_widget.scrollToItem(item,
                                             QAbstractItemView.PositionAtCenter)

    @QtCore.pyqtSlot(name="open_developers_file_dialog")
    def open_developers_file_dialog(self):
        """
        Открытие файла разработчиков.
        :return:
        """
        self.open_file(self.developers_file_content,
                       self.ui.developers_list_widget,
                       self.ui.delevelopers_file_name_label)

    @QtCore.pyqtSlot(name="open_constructors_file_dialog")
    def open_constructors_file_dialog(self):
        """
        Открытие файла конструкторов.
        :return:
        """
        self.open_file(self.constructors_file_content,
                       self.ui.constructors_list_widget,
                       self.ui.constructors_file_name_label)

    @QtCore.pyqtSlot(name="file_comparison")
    def file_comparison(self):
        """
        Получает два словаря с уникальными значениями каждого списка блоков,
        объединяет эти словари, удаляет ключи с пустыми значениями,
        подсчитывает количество несовпадений, выводит в list widget.
        :return:
        """
        counter = [0]

        self.ui.result_label.setVisible(True)

        developers_differences_dict = functions.make_dict_of_differences(
            self.developers_file_content,
            self.constructors_file_content
        )
        constructors_differences_dict = functions.make_dict_of_differences(
            self.constructors_file_content,
            self.developers_file_content
        )

        self.ui.developers_list_widget.clear()
        self.ui.constructors_list_widget.clear()

        self.fill_list_widget(developers_differences_dict,
                              self.ui.developers_list_widget, counter)
        self.fill_list_widget(constructors_differences_dict,
                              self.ui.constructors_list_widget, counter)

        self.ui.result_label.setText("Найдено несовпадений: " + str(counter[0]))

    @QtCore.pyqtSlot(name="on_developers_list_widget_item_clicked")
    def on_developers_list_widget_item_clicked(self):
        """
        Обработки нажатий на элементы списка разработчиков.
        Поиск выбранного элемента в списке конструкторов.
        :return:
        """
        self.find_list_widget_item(self.ui.constructors_list_widget)

    @QtCore.pyqtSlot(name="on_constructors_list_widget_item_clicked")
    def on_constructors_list_widget_item_clicked(self):
        """
        Обработки нажатий на элементы списка конструкторов.
        Поиск выбранного элемента в списке разработчиков.
        :return:
        """
        self.find_list_widget_item(self.ui.developers_list_widget)


if __name__ == "__main__":
    print("Это модуль формы")
