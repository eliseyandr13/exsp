from PyQt5 import QtWidgets as qtw
from PyQt5 import uic
import sys
import sqlite3


class Widget(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute(""" SELECT * FROM coffee """).fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название сорта', 'Степень обжарки',
                                                            'Молотый/в зернах', 'Описание вкуса',
                                                            'Цена', 'Объем упаковки'])
        for i in range(len(result)):
            for j in range(7):
                self.tableWidget.setItem(i, j, qtw.QTableWidgetItem(str(result[i][j])))
            
        
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    copy = Widget()
    copy.show()
    sys.exit(app.exec())
