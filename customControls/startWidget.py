from PySide2.QtWidgets import QWidget, QPushButton


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

        self.e = QPushButton('简单(E)', self)
        self.e.resize(350, 60)
        self.e.move(175, 120)
        self.m = QPushButton('中等(M)', self)
        self.m.resize(350, 60)
        self.m.move(175, 180)
        self.h = QPushButton('困难(H)', self)
        self.h.resize(350, 60)
        self.h.move(175, 240)
        self.v = QPushButton('魔鬼(V)', self)
        self.v.resize(350, 60)
        self.v.move(175, 300)
        self.d = QPushButton('设计(D)', self)
        self.d.resize(350, 60)
        self.d.move(175, 400)
