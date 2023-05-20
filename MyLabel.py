from PyQt6.QtGui import QColor, QPixmap, QMouseEvent, QPaintEvent, QPainter, QFont
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt

from qrcode import QRCode


class MyLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__pos = None
        self.__product_name = None
        self.__qr_code = None
        self.__save_file_name = None
        self.__pixmap = QPixmap("./instruction.png")

    def size_hint(self):
        return self.__pixmap.size()

    def save_image(self, file_name):
        self.__save_file_name = file_name

        self.update()

    def load_image(self, file_name):
        self.__pixmap = QPixmap(file_name)

        self.update()

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(MyLabel, self).mousePressEvent(ev)

        if ev.type() == Qt.MouseButton.LeftButton:
            self.__pos = ev.pos()

            self.update()

    def print_product_name(self, text):
        self.__product_name = text

        self.update()

    def generate_qr(self, input_data):
        qr = QRCode(version=1, box_size=5, border=1)
        qr.add_data(input_data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save('tmp.png')

        self.__qr_code = QPixmap('tmp.png')

        self.update()

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter()

        if self.__save_file_name:
            my_pixmap = QPixmap(self.__pixmap)
            painter.begin(my_pixmap)
        else:
            super(MyLabel, self).paintEvent(a0)

            painter.begin(self)

        if self.__pixmap:
            painter.drawPixmap(0, 0, self.__pixmap)

        if self.__pos:
            if self.__product_name:
                painter.setPen(QColor("black"))
                painter.setFont(QFont("Courier", 25))
                painter.drawText(self.__pos, self.__product_name)
            else:
                painter.setPen(QColor("red"))
                painter.drawEllipse(self.__pos, 20, 20)

        if self.__qr_code:
            width = self.__pixmap.size().width() - self.__qr_code.size().width()
            height = self.__pixmap.size().height() - self.__qr_code.size().height()

            painter.drawPixmap(width, height, self.__qr_code)

        painter.end()

        if self.__save_file_name:
            my_pixmap.save(self.__save_file_name)

            self.__save_file_name = None
