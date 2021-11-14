'''

https://prog-help.ru/python/pyqt5-rabota-s-qtableview-sortirovka-ne-po-str-poisk-po-vybrannym-stolbcam-avto-shirina/
https://webformyself.com/rukovodstvo-po-parsingu-xml-python/
'''


import xml.dom.minidom

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime as dt
import json
import os

from PyQt5.QtWidgets import QHeaderView

dir = 'd:/tmp'
file = 'list.xml'


class Ui_Dialog(object):
    resized = QtCore.pyqtSignal()

    # def __init__(self, parent=None):
    #     super(Ui_Dialog, self).__init__(parent=parent)
    #     ui = Ui_Dialog()
    #     ui.setupUi(self)
    #     self.resized.connect(self.someFunction)

    def __init__(self):
        super(Ui_Dialog, self).__init__()
        print(444444444444)

        #

    def someFunction(self):
        print(444444444444)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(756, 724)

        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout.addWidget(self.tableView)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        Dialog.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 21))
        self.menubar.setObjectName("menubar")
        Dialog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setObjectName("statusbar")
        Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # def setupUi(self, Dialog):
    #     Dialog.setObjectName("Dialog")
    #     Dialog.resize(800, 600)
    #
    #
    #
    #     # self.pushButton = QtWidgets.QPushButton(Dialog)
    #     # self.pushButton.setGeometry(QtCore.QRect(20, 270, 75, 23))
    #     # self.pushButton.setObjectName("pushButton")
    #     # self.pushButton.clicked.connect(self.loadData)
    #
    #
    #     self.tableView = QtWidgets.QTableView(Dialog)
    #     self.tableView.setGeometry(QtCore.QRect(10, 10, 780, 580))
    #     self.tableView.setSortingEnabled(True)
    #     self.tableView.setObjectName("tableView")
    #
    #
    #
    #     # self.lineEdit = QtWidgets.QLineEdit(Dialog)
    #     # self.lineEdit.setGeometry(QtCore.QRect(340, 270, 191, 20))
    #     # self.lineEdit.setObjectName("lineEdit")
    #
    #
    #
    #     self.retranslateUi(Dialog)
    #     QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        # Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        # self.pushButton.setText(_translate("Dialog", "Загрузить"))
        # self.lineEdit.setPlaceholderText(_translate("Dialog", "Поиск по имени или ID"))



    def loadData(self):
        headers = ['Файл ', 'Від ', 'Номер ', 'Статус ', 'Дата ']
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(headers)

        # Читаємо з файлу
        items = []
        if os.path.exists(dir + '/' + file):
            # f = open(dir + '/' + file, 'r')
            doc = xml.dom.minidom.parse(dir + '/' + file,)
            # print(doc.nodeName)
            # print(doc.firstChild.tagName)
            expertise = doc.getElementsByTagName("doc")
            # print("%d expertise:" % expertise.length)
            for i, skill in enumerate(expertise):
                print(skill.getAttribute("name"))
                item = [
                    skill.getAttribute("name"),
                    skill.getAttribute("date"),
                    skill.getAttribute("num"),
                    skill.getAttribute("status"),

                ]
                items.append(item)
        else:
            print('файлу немає')

        # items = [
        #     ['Oleg', 22.98, 1587900157, dt.date(1998, 9, 5)],
        #     ['Max', 223.05, 1587900543, dt.date(2000, 9, 5)],
        #     ['Vladimir324235576576294592', -99.12, 1587900003, dt.date(2001, 9, 5)],
        #     ['Anton', -11.32, 1587900322, dt.date(1998, 3, 5)],
        #     ['Глеб', 17.21, 1587900932, dt.date(1998, 4, 5)],
        #     ['Nataliya', 989.16, 1587900113, dt.date(1998, 5, 5)],
        #     ['Виталий', -233.04, 1587900199, dt.date(1998, 9, 6)]
        # ]

        self.fillTable(model, items)
        self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

        # print(path)

    def fillTable(self, model, items):
        for row_number, row_data in enumerate(items):
            tableitem = []
            model.insertRow(row_number)
            for value in row_data:
                item = QtGui.QStandardItem(str(value))
                tableitem.append(item)
            model.insertRow(row_number, tableitem)
        self.tableView.setModel(model)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.setWindowTitle("Реєстратор документів")

    ui.loadData()
    Dialog.show()

    sys.exit(app.exec_())
