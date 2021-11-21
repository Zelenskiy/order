'''

https://prog-help.ru/python/pyqt5-rabota-s-qtableview-sortirovka-ne-po-str-poisk-po-vybrannym-stolbcam-avto-shirina/
https://webformyself.com/rukovodstvo-po-parsingu-xml-python/
'''
import codecs
import xml.dom.minidom

from PyQt5 import QtCore, QtGui, QtWidgets
import time

import json
from datetime import datetime

import os
import sys

from PyQt5.QtCore import QDate
from lxml import etree as ET
from pathlib import Path


from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem

dir = ''
dir = 'd:\\tmp\\'
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


        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(90, 40, -271, -201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.clicked.connect(self.setDate)


        Dialog.setCentralWidget(self.centralwidget)



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
        self.tableWidget.clicked.connect(self.clickCell)
        self.model = []


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

    def clickCell(self):
        r = self.tableWidget.currentRow()
        c = self.tableWidget.currentColumn()
        text = self.tableWidget.item(r, c).text()
        # if c == 1:
        #     cursor = QtGui.QCursor()
        #     xCur = cursor.pos().x()
        #     yCur = cursor.pos().y()
        #     xWindow = Dialog.geometry().x()
        #     yWindow = Dialog.geometry().y()
        #     print()
        #     print(text)
        #     date_time_obj = time.strptime(text, "%Y-%m-%d")
        #     date = QDate(date_time_obj.tm_year, date_time_obj.tm_mon, date_time_obj.tm_mday)
        #     self.calendarWidget.setSelectedDate(date)
        #     self.calendarWidget.setGeometry(QtCore.QRect(xCur-xWindow, yCur-yWindow, 271, 201))
        #     # self.calendarWidget.setGeometry(QtCore.QRect(90, 40, xCur+xWindow, yCur+yWindow))
        # else:
        #     self.calendarWidget.setGeometry(QtCore.QRect(90, 40, -271, -201))


    def setDate(self):
        print('999999')
        self.calendarWidget.setGeometry(QtCore.QRect(90, 40, -271, -201))

    def openDocument(self, table):
        if self.tableWidget.currentColumn() == 0:
            item = self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn())
            item6 = self.tableWidget.item(self.tableWidget.currentRow(), 6).text()
            s = item.text()
            param ='"' + dir + s + '"'
            if item6 == "Є":
                os.startfile(param)



    def loadData(self):
        # Читаємо файли документів
        colorNoFile = QtGui.QColor(155, 155, 155)
        source_dir = Path(dir)
        files = source_dir.glob('*.doc*')
        ff = []
        for file_ in files:
            s = file_.name
            ff.append(s)

        headers = ['Файл ', 'Від ', 'Номер ', '', 'Статус ', 'Дата ', '']
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(headers)
        # Читаємо з файлу
        items = []
        if os.path.exists(dir + file):
            doc = xml.dom.minidom.parse(dir + file)
            expertise = doc.getElementsByTagName("doc")
            self.tableWidget.setRowCount(len(expertise))
            self.tableWidget.setColumnCount(len(headers))
            for i, skill in enumerate(expertise):
                nameFile = skill.getAttribute("name")
                items.append(nameFile)

                item_0 = QTableWidgetItem(skill.getAttribute("name"))
                x = skill.getAttribute("date")
                ss = x.split('.')
                try:
                    if len(ss[2]) == 4:
                        x = ss[2]+'-'+ss[1]+'-'+ss[0]
                except:
                    pass
                item_1 = QTableWidgetItem(x)
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
                if nameFile in ff:
                    item_6 = QTableWidgetItem("Є")
                    self.tableWidget.setItem(i, 6, item_6)
                else:
                    item_6 = QTableWidgetItem("Немає")
                    self.tableWidget.setItem(i, 6, item_6)
                    for j in range(self.tableWidget.columnCount()):
                        try:
                            self.tableWidget.item(i, j).setForeground(colorNoFile)
                        except:
                            pass
            for f in ff:
                if f in items:
                    pass
                else:
                    self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
                    n = self.tableWidget.rowCount()-1
                    self.tableWidget.setItem(n, 0, QTableWidgetItem(f))
                    self.tableWidget.setItem(n, 1, QTableWidgetItem(''))
                    self.tableWidget.setItem(n, 2, QTableWidgetItem(''))
                    self.tableWidget.setItem(n, 3, QTableWidgetItem(''))
                    self.tableWidget.setItem(n, 4, QTableWidgetItem(''))
                    self.tableWidget.setItem(n, 6, QTableWidgetItem(''))


        else:
            print('файлу немає')

        # self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().resizeSection(2, 50)
        self.tableWidget.horizontalHeader().resizeSection(3, 50)
        self.tableWidget.horizontalHeader().resizeSection(6, 20)
        self.tableWidget.setHorizontalHeaderLabels(headers)




class Window(QtWidgets.QMainWindow):
    windowClose = QtCore.pyqtSignal()

    def closeEvent(self, event):
        self.windowClose.emit()
        print('close')
        saveData()
        return super(Window, self).closeEvent(event)

def saveData():
    print('save...')
    root = ET.Element('docs')
    rowCount = ui.tableWidget.rowCount()
    for i in range(rowCount):
        second1 = ET.SubElement(root, 'doc')
        second1.attrib['name'] = ui.tableWidget.item(i, 0).text()
        second1.attrib['date'] = ui.tableWidget.item(i, 1).text()
        try:
            n = ui.tableWidget.item(i, 2).text()
        except:
            n = ''
        try:
            d = ui.tableWidget.item(i, 3).text()
        except:
            d = ''
        second1.attrib['num'] = n+'-'+d
        second1.attrib['status'] = ui.tableWidget.item(i, 4).text()
    tree = ET.ElementTree(root)
    tree.write(dir + file, pretty_print=True, xml_declaration=True, encoding="utf-8")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = Window()
    # Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.setWindowTitle("Реєстратор документів")
    ui.loadData()
    Dialog.show()
    sys.exit(app.exec_())
