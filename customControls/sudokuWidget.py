from random import choice

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow

from customControls.mainWidget import MainWidget
from customControls.startWidget import StartWidget


class SudokuWidget(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(SudokuWidget, self).__init__(*args, **kwargs)
        self.setStyleSheet("""
                QWidget{
                    font-size:26px;
                    font-family:Microsoft YaHei;
                    color:#000000;
                    background-color:#ffffff;
                }""")

        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.resize(880, 600)
        self.setFixedSize(self.width(), self.height())
        icon = QIcon('resource/ico/title.ico')
        self.setWindowIcon(icon)
        self.setWindowTitle('数独')

        self.start = StartWidget()
        self.home = MainWidget()

        self.setCentralWidget(self.start)
        self.home.new.clicked.connect(lambda: self.play(self.start))
        self.start.easy.clicked.connect(lambda: self.play(self.home, n=choice(range(40, 46))))
        self.start.normal.clicked.connect(lambda: self.play(self.home, n=choice(range(46, 51))))
        self.start.hard.clicked.connect(lambda: self.play(self.home, n=51))
        self.start.very_hard.clicked.connect(lambda: self.play(self.home, n=52))
        pass

    def play(self, widget, n=0):
        self.centralWidget().setParent(None)
        self.setCentralWidget(widget)
        if widget == self.home:
            widget.write_all_button(n)
