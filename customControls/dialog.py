import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QDialog, QLabel, QWidget

from customControls.pushButton import QPushButton


class StopDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.widget = QWidget(self)
        self.widget.setGeometry(0, 0, 300, 300)
        self.widget.setStyleSheet('border-radius:10px;background-color:#FFFFFF;')
        self.label = QLabel("数独已暂停", self)
        self.label.resize(300, 200)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.continueButton = QPushButton("继续游戏", self)
        self.continueButton.resize(100, 50)
        self.continueButton.move(100, 200)
        self.continueButton.clicked.connect(lambda: self.close())
        self.label.setStyleSheet('border-radius:10px;background-color:#FFFFFF;')


class WinDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.widget = QWidget(self)
        self.widget.setGeometry(0, 0, 300, 300)
        self.widget.setStyleSheet('border-radius:10px;background-color:#FFFFFF;')
        self.label = QLabel("恭喜你，数独已经被你成功解答", self)
        self.label.move(25, 0)
        self.label.resize(250, 200)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.continueButton = QPushButton("新游戏", self)
        self.continueButton.resize(100, 50)
        self.continueButton.move(33.3, 200)
        self.continueButton.clicked.connect(lambda: self.close())
        self.label.setStyleSheet('border-radius:10px;background-color:#FFFFFF;')
        self.continueButton = QPushButton("退出", self)
        self.continueButton.resize(100, 50)
        self.continueButton.move(166.6, 200)
        self.continueButton.clicked.connect(lambda: self.parent().parent().close())
        self.label.setStyleSheet('border-radius:10px;background-color:#FFFFFF;')


def main():
    app = QApplication(sys.argv)
    label = StopDialog()
    label.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
