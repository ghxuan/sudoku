import sys
import time
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QLCDNumber, QApplication


class LcdNumber(QLCDNumber):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.setAttribute(Qt.WA_StyledBackground)
        self.resize(130, 40)
        self.move(680, 150)
        self.setDigitCount(8)
        self.setMode(QLCDNumber.Dec)
        self.setSegmentStyle(QLCDNumber.Flat)
        self.display(time.strftime("%X", time.localtime()))
        self.setStyleSheet("""
                QLCDNumber{
                    border:none;
                }
        """)
        print(time.localtime())
        print(type(time.localtime()))

    def re_init(self):
        pass


def main():
    app = QApplication(sys.argv)
    label = LcdNumber()
    label.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
