from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QMenuBar, QFileDialog, QInputDialog

from MyLabel import MyLabel


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__my_label = MyLabel(self)
        self.setCentralWidget(self.__my_label)

        self.menu_bar = QMenuBar(None)

        product_menu = self.menu_bar.addMenu("Produkt")

        product_menu.addAction("1. Produktbild öffnen", self.load_file)
        product_menu.addAction("2. Produktname eingeben", self.set_product_name)
        product_menu.addAction("3. QR-Code erstellen", self.set_qr_value)
        product_menu.addAction("4. Flyer speichern", self.save_file)

        self.setMenuBar(self.menu_bar)

        self.setWindowTitle("Flyer-Generator")

        self.resize(self.__my_label.size_hint())

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Bild auswählen")

        if file_name:
            self.__my_label.load_image(file_name)

            self.resize(self.__my_label.size_hint())

    def set_product_name(self):
        text, valid = QInputDialog.getText(self, "Produktname eingeben", "Produktname:")

        if valid:
            self.__my_label.print_product_name(text)

    def set_qr_value(self):
        url, ok = QInputDialog.getText(self, "Link", "Link zum QR-Code: ")

        if ok and url:
            self.__my_label.generate_qr(url)

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(caption="Speicherort und -name auswählen")

        if file_name:
            self.__my_label.save_image(file_name)
