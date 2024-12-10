import sys

import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6 import uic


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        res = cur.execute('''SELECT * FROM coffee''').fetchall()

        for i in range(1, int(self.tableWidget.rowCount()) + 1):
            self.tableWidget.removeRow(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
