# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(460, 654)
        Form.setMinimumSize(QtCore.QSize(460, 654))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.open_developers_file_button = QtWidgets.QPushButton(Form)
        self.open_developers_file_button.setObjectName("open_developers_file_button")
        self.horizontalLayout_2.addWidget(self.open_developers_file_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.open_constructors_file_button = QtWidgets.QPushButton(Form)
        self.open_constructors_file_button.setObjectName("open_constructors_file_button")
        self.horizontalLayout_2.addWidget(self.open_constructors_file_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.delevelopers_file_name_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setItalic(True)
        self.delevelopers_file_name_label.setFont(font)
        self.delevelopers_file_name_label.setObjectName("delevelopers_file_name_label")
        self.horizontalLayout_5.addWidget(self.delevelopers_file_name_label)
        self.constructors_file_name_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setItalic(True)
        self.constructors_file_name_label.setFont(font)
        self.constructors_file_name_label.setObjectName("constructors_file_name_label")
        self.horizontalLayout_5.addWidget(self.constructors_file_name_label)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.developers_list_widget = QtWidgets.QListWidget(Form)
        self.developers_list_widget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.developers_list_widget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.developers_list_widget.setLineWidth(1)
        self.developers_list_widget.setProperty("showDropIndicator", False)
        self.developers_list_widget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.developers_list_widget.setObjectName("developers_list_widget")
        self.horizontalLayout_3.addWidget(self.developers_list_widget)
        self.constructors_list_widget = QtWidgets.QListWidget(Form)
        self.constructors_list_widget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.constructors_list_widget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.constructors_list_widget.setLineWidth(1)
        self.constructors_list_widget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.constructors_list_widget.setObjectName("constructors_list_widget")
        self.horizontalLayout_3.addWidget(self.constructors_list_widget)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comparison_button = QtWidgets.QPushButton(Form)
        self.comparison_button.setEnabled(False)
        self.comparison_button.setFlat(False)
        self.comparison_button.setObjectName("comparison_button")
        self.horizontalLayout_4.addWidget(self.comparison_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.result_label = QtWidgets.QLabel(Form)
        self.result_label.setEnabled(True)
        self.result_label.setObjectName("result_label")
        self.horizontalLayout_4.addWidget(self.result_label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 4, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Анализ таблиц цепей"))
        self.label.setText(_translate("Form", "Файл разработчиков"))
        self.label_2.setText(_translate("Form", "Файл конструкторов"))
        self.open_developers_file_button.setText(_translate("Form", "Обзор"))
        self.open_constructors_file_button.setText(_translate("Form", "Обзор"))
        self.delevelopers_file_name_label.setText(_translate("Form", "Файл не выбран"))
        self.constructors_file_name_label.setText(_translate("Form", "Файл не выбран"))
        self.comparison_button.setText(_translate("Form", "Найти несовпадения"))
        self.result_label.setText(_translate("Form", "Найдено несовпадений: "))
