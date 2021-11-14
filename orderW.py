'''

https://prog-help.ru/python/pyqt5-rabota-s-qtableview-sortirovka-ne-po-str-poisk-po-vybrannym-stolbcam-avto-shirina/
https://webformyself.com/rukovodstvo-po-parsingu-xml-python/
'''
import codecs
import xml.dom.minidom

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime as dt
import json
import os

from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem

dir = 'd:\\tmp'
file = 'list.xml'


class Ui_Dialog(object):
    resized = QtCore.pyqtSignal()


    def __init__(self):
        super(Ui_Dialog, self).__init__()



    def someFunction(self):
        pass

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(756, 724)

        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.horizontalLayout.addWidget(self.tableWidget)
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

        self.tableWidget.doubleClicked.connect(self.openDocument)
        self.model = []


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate


    def openDocument(self, table):
        if self.tableWidget.currentColumn() == 0:
            item = self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn())
            print()
            s = item.text()
            param ='"' + dir + '\\' + s + '"'
            os.startfile(param)



    def loadData(self):
        headers = ['Файл ', 'Від ', 'Номер ', '', 'Статус ', 'Дата ']
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(headers)
        # Читаємо з файлу
        items = []
        if os.path.exists(dir + '/' + file):
            doc = xml.dom.minidom.parse(dir + '/' + file)
            expertise = doc.getElementsByTagName("doc")
            self.tableWidget.setRowCount(len(expertise))
            self.tableWidget.setColumnCount(len(headers))
            for i, skill in enumerate(expertise):
                # print(skill.getAttribute("name"))
                # item = [
                #     skill.getAttribute("name"),
                #     skill.getAttribute("date"),
                #     skill.getAttribute("num"),
                #     skill.getAttribute("status"),
                #
                # ]
                # items.append(item)
                item_0 = QTableWidgetItem(skill.getAttribute("name"))
                item_1 = QTableWidgetItem(skill.getAttribute("date"))
                item_2_3 = skill.getAttribute("num")

                if item_2_3.find('-') > -1:
                    n = item_2_3.find('-')
                    x2 = item_2_3[:n]
                    x3 = item_2_3[n+1:]
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(x2))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(x3))
                item_4 = QTableWidgetItem(skill.getAttribute("status"))
                self.tableWidget.setItem(i, 0, item_0)
                self.tableWidget.setItem(i, 1, item_1)
                self.tableWidget.setItem(i, 4, item_4)
        else:
            print('файлу немає')

        # self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().resizeSection(2, 50)
        self.tableWidget.horizontalHeader().resizeSection(3, 50)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(headers)

        # print(path)

    # def fillTable(self, model, items):
    #     for row_number, row_data in enumerate(items):
    #         tableitem = []
    #         model.insertRow(row_number)
    #         for value in row_data:
    #             item = QtGui.QStandardItem(str(value))
    #             tableitem.append(item)
    #         model.insertRow(row_number, tableitem)
    #     # self.tableWidget.setModel(model)

# class MyWindow(QtWidgets.QMainWindow()):

class Window(QtWidgets.QMainWindow):
    windowClose = QtCore.pyqtSignal()

    def closeEvent(self, event):
        self.windowClose.emit()
        print('close')
        saveData()
        return super(Window, self).closeEvent(event)

def saveData():
    print ('save...')
    print(ui.tableWidget)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = Window()
    # Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.setWindowTitle("Реєстратор документів")

    ui.loadData()
    Dialog.show()

    sys.exit(app.exec_())
