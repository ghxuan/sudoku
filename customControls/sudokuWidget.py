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
        icon = QIcon('t.ico')
        self.setWindowIcon(icon)
        self.setWindowTitle('数独')

        self.home = StartWidget()
        self.start = MainWidget()

        self.setCentralWidget(self.start)
        self.start.n.clicked.connect(lambda: self.play(self.home))
        self.home.e.clicked.connect(lambda: self.play(self.start))
        pass

    def exchange(self):
        pass

    def play(self, widget):
        self.setCentralWidget(widget)
        pass
