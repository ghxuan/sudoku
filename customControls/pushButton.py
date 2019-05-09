from PySide2.QtCore import Qt, QRect, QPoint
from PySide2.QtWidgets import QWidget, QPushButton
from PySide2.QtGui import QPaintEvent, QPainter, QBrush, QColor, QPen


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.resize(60, 60)

    def __hash__(self):
        return hash(self.text())


class Push(QPushButton):
    def __init__(self, *args, **kwargs):
        super(Push, self).__init__(*args, **kwargs)

        self.setStyleSheet("""
                        QPushButton{
                            font-weight: 500;
                            font-size:16px;
                            font-family:Microsoft YaHei;
                        }

                        Push{
                            border-radius:5px;
                            border:1px solid lightgrey;
                            background-color:#ffffff;
                            color:#000000;
                            font-weight: 500;
                            font-size:18px;
                            font-family:Microsoft YaHei;
                        }

                        Push:hover{
                            border-radius:5px;
                            border:1px solid lightgrey;
                            background-color:#ffffff;
                            color:#000000;
                            font-weight: 500;
                            font-size:18px;
                            font-family:Microsoft YaHei;
                        }

                        Push:pressed{
                            border-radius:5px;
                            border:1px solid lightgrey;
                            background-color:#ffffff;
                            color:#000000;
                            font-weight: 500;
                            font-size:18px;
                            font-family:Microsoft YaHei;lightgrey;
                        }

                        Push:disabled{
                            border-radius:5px;
                            border:1px solid lightgrey;
                            background-color:#ffffff;
                            color:#000000;
                            font-weight: 500;
                            font-size:18px;
                            font-family:Microsoft YaHei;
                        }
                """)

        for i in range(3):
            for j in range(3):
                exec(
                    f'self.but{j}{i} = QPushButton("{i + j * 3 + 1}", self)\n'
                    f'self.but{j}{i}.resize(40, 40)\n'
                    f'self.but{j}{i}.resize(40, 40)\n'
                    f'self.but{j}{i}.move({5 + 40 * i + i * 5}, {15 + 40 * j + j * 5})\n'
                    f'self.but{j}{i}.clicked.connect(lambda: self.press(self.but{j}{i}))', locals(), globals()
                )

    def press(self, but, point=QPoint(-150, -150)):
        self.but.setText(but.text())
        self.move(point)
        self.check()

    def paintEvent(self, arg__1: QPaintEvent):
        # super(Push, self).paintEvent(arg__1)
        # lightgrey
        painter = QPainter()
        painter.begin(self)
        pen = QPen(QColor(162, 181, 205), 2, Qt.SolidLine)
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.setPen(pen)
        painter.setRenderHint(QPainter.Antialiasing, True)
        rect = QRect()
        rect.moveTo(1, 10)
        rect.setWidth(140)
        rect.setHeight(140)
        painter.drawRoundedRect(rect, 5, 5)
        painter.drawConvexPolygon([QPoint(60, 10), QPoint(80, 10), QPoint(70, 1)])

        pen.setColor(QColor(255, 255, 255))
        painter.setPen(pen)
        painter.drawLine(63, 10, 77, 10)
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawPoints([QPoint(61, 10), QPoint(78, 10)])
        painter.end()


class RotatePush(QPushButton):
    def __init__(self, *args, **kwargs):
        super(RotatePush, self).__init__(*args, **kwargs)

        self.setStyleSheet("""
                QPushButton{
                    font-weight: 500;
                    font-size:16px;
                    font-family:Microsoft YaHei;
                }

                Push{
                    border-radius:5px;
                    border:1px solid lightgrey;
                    background-color:#ffffff;
                    color:#000000;
                    font-weight: 500;
                    font-size:18px;
                    font-family:Microsoft YaHei;
                }

                Push:hover{
                    border-radius:5px;
                    border:1px solid lightgrey;
                    background-color:#ffffff;
                    color:#000000;
                    font-weight: 500;
                    font-size:18px;
                    font-family:Microsoft YaHei;
                }

                Push:pressed{
                    border-radius:5px;
                    border:1px solid lightgrey;
                    background-color:#ffffff;
                    color:#000000;
                    font-weight: 500;
                    font-size:18px;
                    font-family:Microsoft YaHei;lightgrey;
                }

                Push:disabled{
                    border-radius:5px;
                    border:1px solid lightgrey;
                    background-color:#ffffff;
                    color:#000000;
                    font-weight: 500;
                    font-size:18px;
                    font-family:Microsoft YaHei;
                }
        """)

        for i in range(3):
            for j in range(3):
                exec(
                    f'self.but{j}{i} = QPushButton("{i + j * 3 + 1}", self)\n'
                    f'self.but{j}{i}.resize(40, 40)\n'
                    f'self.but{j}{i}.resize(40, 40)\n'
                    f'self.but{j}{i}.move({5 + 40 * i + i * 5}, {5 + 40 * j + j * 5})\n'
                    f'self.but{j}{i}.clicked.connect(lambda: self.press(self.but{j}{i}))', locals(), globals()
                )

    def press(self, but, point=QPoint(-150, -150)):
        self.but.setText(but.text())
        self.move(point)
        self.check()

    def paintEvent(self, arg__1: QPaintEvent):
        # super(Push, self).paintEvent(arg__1)
        # lightgrey
        painter = QPainter()
        painter.begin(self)
        pen = QPen(QColor(162, 181, 205), 2, Qt.SolidLine)
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.setPen(pen)
        painter.setRenderHint(QPainter.Antialiasing, True)
        rect = QRect()
        rect.moveTo(1, 1)
        rect.setWidth(140)
        rect.setHeight(140)
        painter.drawRoundedRect(rect, 5, 5)
        painter.drawConvexPolygon([QPoint(60, 141), QPoint(80, 141), QPoint(70, 150)])

        pen.setColor(QColor(255, 255, 255))
        painter.setPen(pen)
        painter.drawLine(63, 141, 77, 141)
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawPoints([QPoint(61, 140), QPoint(78, 140)])
        painter.end()
