import sys
from PyQt6 import QtWidgets
from MyMainWindow import MyMainWindow


app = QtWidgets.QApplication(sys.argv)

mainWindow = MyMainWindow()
mainWindow.show()

sys.exit(app.exec())
