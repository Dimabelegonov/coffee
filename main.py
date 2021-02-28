from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QGridLayout
from win32api import GetSystemMetrics
import sys
import sqlite3
from PyQt5 import uic


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.grid_layout.addWidget(self.table, 0, 0)
        self.set_info()

    def set_info(self):
        conn = sqlite3.connect("coffee.db3")
        cur = conn.cursor()
        result = cur.execute("""SELECT * FROM "table" """).fetchall()
        self.table.setRowCount(len(result))
        for i, elem in enumerate(result):
            self.table.setItem(i, 0, QTableWidgetItem(elem[1]))
            self.table.setItem(i, 1, QTableWidgetItem(elem[2]))
            self.table.setItem(i, 2, QTableWidgetItem(elem[3]))
            self.table.setItem(i, 3, QTableWidgetItem(elem[4]))
            self.table.setItem(i, 4, QTableWidgetItem(elem[5]))
            self.table.setItem(i, 5, QTableWidgetItem(elem[6]))
        self.table.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
