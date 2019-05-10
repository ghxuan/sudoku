import sys
from PySide2.QtWidgets import QApplication
from customControls.sudokuWidget import SudokuWidget


def main():
    app = QApplication(sys.argv)
    label = SudokuWidget()
    label.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
