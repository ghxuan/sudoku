import sys
from PySide2.QtWidgets import QWidget, QPushButton, QApplication


class StartWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(StartWidget, self).__init__(*args, **kwargs)

        self.setStyleSheet('''
                QPushButton{
                    border-radius:5px;
                    border-bottom:1px solid lightgrey;
                    border-right:1px solid lightgrey;
                    border:1px solid lightgrey;
                    background-color:#F8F8F8;
                    color:#555555;
                    font-size:19px;
                    font-family:Microsoft YaHei;
                }

                QPushButton:hover{
                    border-bottom:1px solid lightgrey;;
                    border-right:1px solid lightgrey;;
                    background-color:#416ba5;
                    color:#ffffff;
                }

                QPushButton:pressed{
                    border-bottom:none;
                    border-right:none;
                    background-color:#416ba5;
                    color:#ffffff;
                    border-top:1px solid lightgrey;
                    border-left:1px solid lightgrey;
                }

                QPushButton:disabled{
                    border:1px solid lightgrey;
                    background-color:#c9c9c9;
                    color:#555555;
                }
        ''')

        self.easy = QPushButton('简单(E)', self)
        self.easy.resize(380, 60)
        self.easy.move(250, 120)
        self.normal = QPushButton('中等(N)', self)
        self.normal.resize(380, 60)
        self.normal.move(250, 200)
        self.hard = QPushButton('困难(H)', self)
        self.hard.resize(380, 60)
        self.hard.move(250, 280)
        self.very_hard = QPushButton('魔鬼(V)', self)
        self.very_hard.resize(380, 60)
        self.very_hard.move(250, 360)


def main():
    app = QApplication(sys.argv)
    label = StartWidget()
    label.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
