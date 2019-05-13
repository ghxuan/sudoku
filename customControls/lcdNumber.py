import sys
from datetime import datetime, timedelta
from PySide2.QtCore import Qt, QTimer
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
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.time = datetime.strptime('00:00:00', '%H:%M:%S')
        self.one_seconds = timedelta(seconds=1)
        self.timer.start(1000)
        self.display(self.time.strftime('%H:%M:%S'))
        self.setStyleSheet("""
                QLCDNumber{
                    border:none;
                }
        """)
        self.timer.interval()

    def re_init(self):
        self.timer.start()
        self.time = datetime.strptime('00:00:00', '%H:%M:%S')
        self.display(self.time.strftime('%H:%M:%S'))
        self.timer.interval()
        pass

    def update_time(self):
        self.time += self.one_seconds
        self.display(self.time.strftime('%H:%M:%S'))

    def stop(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start()


def main():
    app = QApplication(sys.argv)
    label = LcdNumber()
    label.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
