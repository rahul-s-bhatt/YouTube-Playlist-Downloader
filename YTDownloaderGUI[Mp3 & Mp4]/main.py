import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6 import uic

class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('form.ui', self)
        self.setWindowTitle('MyApp')

def main():
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    try:
        sys.exit(app.exec())
    except:
        print('no')

if __name__ == '__main__':
    main()
