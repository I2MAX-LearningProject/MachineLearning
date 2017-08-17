# Day_05_08_PyQt.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, \
    QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog

def getContents(filename):
    f = open(filename, 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()

    return ''.join(lines)

def showDialog():
    filename, ok = QFileDialog.getOpenFileName(w, '파일 선택', '', '텍스트파일(*.txt)')
    if ok:
        edit.appendPlainText(getContents(filename))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    button = QPushButton('파일 선택')
    button.clicked.connect(showDialog)

    edit = QPlainTextEdit()
    edit.setReadOnly(True)

    hbox = QHBoxLayout()
    hbox.addStretch(1)
    hbox.addWidget(button)
    hbox.addStretch(1)

    vbox = QVBoxLayout()
    vbox.addLayout(hbox)
    vbox.addWidget(edit)

    w = QWidget()
    w.setLayout(vbox)
    w.show()

    sys.exit(app.exec_())






