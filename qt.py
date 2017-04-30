# import sys
# from PyQt5.QtWidgets import QLabel, QApplication, QVBoxLayout, QWidget, \
#     QMainWindow, QAction,qApp, QPushButton,QPlainTextEdit, QTextBrowser, QTextEdit
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import QCoreApplication
#
# # app = QApplication(sys.argv)
# # window = QWidget()
# # window.setWindowTitle('WTF GUI APP')
# # window.resize(300,70)
# # lable = QLabel("<center>HELLO WONDERFUL GUI</center>")
# # btnQuit = QPushButton('Dont give a FUCK')
# # btnQuit.clicked.connect(app.quit)
# # vbox = QVBoxLayout()
# # vbox.addWidget(lable)
# # vbox.addWidget(btnQuit)
# # window.setLayout(vbox)
# #
# # window.show()
# # sys.exit(app.exec_())
#
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.title='WTF GUI APP'
#
#         self.initUI()
#
#     def initUI(self):
#         # exitAction = QAction(QIcon('web.png'), '&Exit', self)
#         # exitAction.setStatusTip('Exit Application')
#         # exitAction.triggered.connect(qApp.quit)
#         # # self.statusBar()
#         #
#         # menubar = self.menuBar()
#         # fileMenu = menubar.addMenu('&File')
#         # fileMenu.addAction(exitAction)
#         qbtn = QPushButton('Close', self)  # Закрыть окно
#         qbtn.clicked.connect(qApp.quit)  # Закрыть окно
#         qbtn.setToolTip('Close This fuckking')  # Закрыть окно
#         # btn.resize(btn.sizeHint())
#         qbtn.move(50,50)  # Закрыть окно
#         qbtn.resize(qbtn.sizeHint())  # Закрыть окно
#         qbtn.setStatusTip('ExitToo')
#         self.lable = QLabel('hello Fuckers')
#         self.textedit = QTextEdit('TTTT')
#         self.plaintextedit = QPlainTextEdit('PPP')
#         self.setWindowTitle(self.title)
#         self.setGeometry(300,300,300,300)
#         self.lable = QLabel("<center>HELLO WONDERFUL GUI</center>")
#         self.setWindowIcon(QIcon('web.png'))
#
#
#         self.vbox = QVBoxLayout()
#         self.vbox.addWidget(self.lable)
#         self.vbox.addWidget(self.textedit)
#         self.vbox.addWidget(self.plaintextedit)
#         self.setLayout(self.vbox)
#         self.show()
#
#
#
#
# if __name__== '__main__':
#     app = QApplication(sys.argv)
#     window=MyWindow()
#     sys.exit(app.exec_())
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget
from euler2 import EulerMethod

def on_clicked():
    print("Кнопка нажата. Функция on_clicked()")

class MyUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.set_layout()
        self.show()


    def initUI(self):
        self.setWindowTitle('Анализатор')
        self.setGeometry(300, 300, 1000, 500)
        self.btn = QtWidgets.QPushButton('Нажми меня плизз', self)
        self.btn.clicked.connect(self.get_text)
        self.lable = QtWidgets.QLabel('You text be here', self)
        self.text_area = QtWidgets.QTextEdit()


    def set_layout(self):
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.text_area)
        vbox.addWidget(self.btn)
        vbox.addWidget(self.lable)
        self.setLayout(vbox)

    def get_text(self):
        area_text = self.text_area.toPlainText()
        self.lable.setText("{}".format(area_text))

        self.lable.setSelection(2,4)
        print(self.lable.hasSelectedText())
        self.text_area.selectAll()
        self.text_area.repaint()
        self.lable.repaint()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyUI()
    sys.exit(app.exec_())