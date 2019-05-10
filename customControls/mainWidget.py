from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt, QPoint
from PySide2.QtGui import QPaintEvent, QPainter, QMouseEvent, QPen

from customControls.pushButton import QPushButton, RotatePush, Push, Button
from customControls.maskWidget import MaskWidget
from customControls.dialog import StopDialog, WinDialog
from customControls.sudoKu import SudoKu, deepcopy


class MainWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)

        self.setStyleSheet('''
                QPushButton{
                    border-radius:5px;
                    border:1px solid lightgrey;
                    background-color:#F8F8F8;
                    color:#555555;
                    font-size:13px;
                    font-family:DFKai-SB;
                }

                QPushButton:hover{
                    border-bottom:1px solid lightgrey;
                    border-right:1px solid lightgrey;
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
                    background-color:#fff;
                    color:#a9a9a9;
                }

                Button{
                    border-radius:0px;
                    border:none;
                    border-left:1px solid #999999;
                    border-top:1px solid #999999;
                    background-color:none;
                    color:#000000;
                    font-weight: 500;
                    font-size:18px;
                    font-family:Microsoft YaHei;
                }

                Button:hover{
                    border:none;
                    border-left:1px solid #999999;
                    border-top:1px solid #999999;
                    background-color:#ffffff;
                    color:#000000;
                }

                Button:pressed{
                    border:none;
                    border-left:1px solid #999999;
                    border-top:1px solid #999999;
                    background-color:#eeeeee;
                    color:#000000;
                }

                Button:disabled{
                    border:none;
                    border-left:1px solid #999999;
                    border-top:1px solid #999999;
                    background-color:#cccccc;
                    color:#000000;
                }

                Button[dis="False"]{
                    padding:none;
                    border:none;
                    border-left:1px solid #999999;
                    border-top:1px solid #999999;
                    background-color:#cccccc;
                    color:#000000;
                }

                Button[dis="False"]:active{
                    border:none;
                    border-left:1px solid #999999;
                    border-top:1px solid #999999;
                    background-color:#cccccc;
                    color:#000000;
                }

                Button[dis="False"]:focus{
                    border:none;
                    border-left:1px solid #999999;
                    border-top:1px solid #999999;
                    background-color:#cccccc;
                    color:#000000;
                }

                Button[dis="False"]:pressed{
                    border:none;
                    border-left:1px solid #999999;
                    border-top:1px solid #999999;
                    background-color:#cccccc;
                    color:#000000;
                }

                Button[dis="False"]:hover{
                    border:none;
                    border-left:1px solid #999999;
                    border-top:1px solid #999999;
                    background-color:#cccccc;
                    color:#000000;
                }
        ''')
        self.sudoKu = SudoKu()
        self.stop = QPushButton('暂停(S)', self)
        self.stop.resize(130, 60)
        self.stop.move(680, 350)
        self.stop.clicked.connect(lambda: self.stop_it())
        self.clear = QPushButton('清除盘面(C)', self)
        self.clear.resize(130, 60)
        self.clear.move(680, 420)
        self.clear.clicked.connect(lambda: self.re_write_all_button())
        self.new = QPushButton('新谜题(N)', self)
        self.new.resize(130, 60)
        self.new.move(680, 490)
        self.end_board, self.board, self.rows, self.cols, self.blocks = [[]], [[]], [set()], [set()], [set()]
        self._buttons, self.buttons, self.res = [dict() for _ in range(9)], [], []

        for i in range(3):
            # 从左到右，从上到下
            self.init_board(71, 31 + i * 179, i * 3)
            self.init_board(71 + 179, 31 + i * 179, 1 + i * 3)
            self.init_board(71 + 358, 31 + i * 179, 2 + i * 3)

        self.write_all_button()
        self.out = QPoint(-150, -150)

        self.push = Push(self)
        self.push.resize(142, 151)
        self.push.move(self.out)
        self.push.check = self.check
        self.rotate_push = RotatePush(self)
        self.rotate_push.resize(142, 151)
        self.rotate_push.move(self.out)
        self.rotate_push.check = self.check

    def init_board(self, x, y, t=0):
        for i in range(3):
            for j in range(3):
                # 从左到右，从上到下
                # t 为大正方形，第几个；j 为从左到右第几个；i 为从上到下第几个
                m, n = divmod(t, 3)
                # pos_i, pos_j = m * 3 + j, n * 3 + i
                exec(
                    f'self.but{t}{j}{i} = Button("", self)\n'
                    f'self.but{t}{j}{i}.resize(59, 59)\n'
                    f'self.but{t}{j}{i}.move({x + 59 * i}, {y + 59 * j})\n'
                    f'self.but{t}{j}{i}.clicked.connect(lambda: self.press(self.but{t}{j}{i}))',
                    locals(), globals())
                self.buttons.append([eval(f'self.but{t}{j}{i}'), m * 3 + j, n * 3 + i, t])
                if i == 0 and j == 0:
                    exec(f'self.but{t}{j}{i}.setStyleSheet("border-left:none;border-top:none;")')
                elif j == 0:
                    exec(f'self.but{t}{j}{i}.setStyleSheet("border-top:none;")')
                elif i == 0:
                    exec(f'self.but{t}{j}{i}.setStyleSheet("border-left:none;")')
        pass

    def write_all_button(self):
        self.res = self.sudoKu.board(50)
        self.re_write_all_button()

    def re_write_all_button(self):
        self.end_board, self.board, self.rows, self.cols, self.blocks = deepcopy(self.res)
        from pprint import pprint
        pprint(self.end_board)
        for i in range(3):
            # 从左到右，从上到下
            self.write_one_button(i * 3)
            self.write_one_button(1 + i * 3)
            self.write_one_button(2 + i * 3)
        pass

    def write_one_button(self, t=0):
        for i in range(3):
            for j in range(3):
                # 从左到右，从上到下
                # t 为大正方形，第几个；j 为从左到右第几个；i 为从上到下第几个
                m, n = divmod(t, 3)
                val = self.board[m * 3 + j][n * 3 + i] if self.board[m * 3 + j][n * 3 + i] else ""
                exec(f'self.but{t}{j}{i}.setText("{val}")')
                if val:
                    # exec(f'self.but{t}{j}{i}.setEnabled(False)')
                    exec(f'self.but{t}{j}{i}.dis = False')
                    exec(f'self.but{t}{j}{i}.setProperty("dis", "False")')
                else:
                    exec(f'self.but{t}{j}{i}.dis = True')
                    exec(f'self.but{t}{j}{i}.setProperty("dis", "True")')

    def check(self):
        cols, rows, blocks, reds = deepcopy(self._buttons), deepcopy(self._buttons), deepcopy(self._buttons), set()
        win = []
        for but, i, j, t in self.buttons:
            val = but.text()
            if val == f'{self.end_board[i][j]}':
                win.append(True)
            else:
                win.append(False)
            if val in cols[i]:
                reds.add(but)
                reds.add(cols[i][val])
            else:
                cols[i][val] = but
            if val in rows[j]:
                reds.add(but)
                reds.add(rows[j][val])
            else:
                rows[j][val] = but
            if val in blocks[t]:
                reds.add(but)
                reds.add(blocks[t][val])
            else:
                blocks[t][val] = but
        if all(win):
            self.win()
        for but, _, _, _ in self.buttons:
            if but in reds:
                but.setStyleSheet('color:red;')
            else:
                but.setStyleSheet('color:black;')

    def stop_it(self):
        dialog = StopDialog(self)
        mask = MaskWidget(self)
        mask.show()
        dialog.exec()
        mask.close()

    def win(self):
        dialog = WinDialog(self)
        mask = MaskWidget(self)
        mask.show()
        dialog.exec()
        mask.close()

    def press(self, but, out=QPoint(-42, 39), rotate_out=QPoint(-42, -130)):
        self.push.move(self.out)
        self.rotate_push.move(self.out)
        if but.dis:
            pos = but.pos()
            if pos.y() > 400:
                self.rotate_push.move(pos + rotate_out)
                self.rotate_push.but = but
            else:
                self.push.move(pos + out)
                self.push.but = but

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)

        for i in range(4):
            painter.drawLine(70, 30 + i * 179, 607, 30 + i * 179)
            painter.drawLine(70 + i * 179, 30, 70 + i * 179, 567)
        painter.end()

    def mousePressEvent(self, event: QMouseEvent):
        self.push.move(self.out)
        self.rotate_push.move(self.out)
        super(MainWidget, self).mousePressEvent(event)
        pass
