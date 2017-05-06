import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget
from euler import EulerMethod as EulerMethod
from lexex import Lexer as Lexer
from lexex import Node as Node
from lexex import Parser as Parser
from post_lex_handler import PostParserHandler as PostParserHandler
import os

# from  euler import output as OUTPUT
# from post_lex_handler import PLH_ERROR as PLH_ERROR
# from euler import EulerMethod

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
        self.btn2 = QtWidgets.QPushButton('Нажми ', self)
        self.btn.clicked.connect(self.get_text)
        self.btn2.clicked.connect(on_clicked)
        self.lable = QtWidgets.QLabel('You text be here', self)
        self.text_area = QtWidgets.QTextEdit()
        self.text_area.setGeometry(0,0, 50, 50)
        self.text_area.sizePolicy()
        self.values = QtWidgets.QScrollArea()
        self.values.setWidget(self.lable)



    def set_layout(self):
        hbox = QtWidgets.QHBoxLayout()
        vbox = QtWidgets.QVBoxLayout()
        hbox.addWidget(self.text_area)
        hbox.addWidget(self.values)
        vbox.addLayout(hbox)
        vbox.addWidget(self.btn)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.lable)
        self.setLayout(vbox)

    def magic(self):
        file = open('input.txt', 'r')
        lexer = Lexer(file)
        node = Node()
        p = Parser(lexer, node)
        FINALNODETREE = p.node.node_tree
        p = PostParserHandler(FINALNODETREE)
        result = p.nt
        METHOD = result.pop('Method')
        d = EulerMethod(**result)
        OUTPUT = str(d.printval())
        d.gen_plot()
        return OUTPUT
    def get_text(self):
        area_text = self.text_area.toPlainText()
        file = open('input.txt', 'w')
        file.write(area_text)
        file.close()
        try:

            self.out = self.magic()
            self.text_area.setText(self.out)

        except:
            if os.path.isfile('plh_err.txt'):
                err = open('plh_err.txt').readline()
                self.lable.setText(str(err))
                os.remove('plh_err.txt')
            elif os.path.isfile('pars_err.txt'):
                err = open('pars_err.txt').readline()
                self.lable.setText(str(err))
                os.remove('pars_err.txt')
            elif os.path.isfile('lex_err.txt'):
                err = open('lex_err.txt').readline()
                self.lable.setText(str(err))
                os.remove('lex_err.txt')
        # finally:
        #     if PLH_ERROR:
        #         self.lable.setText(str(PLH_ERROR))

        # self.lable.setSelection(2, 4)
        # print(self.lable.hasSelectedText())
        # self.text_area.selectAll()
        self.text_area.repaint()
        self.text_area.repaint()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyUI()
    sys.exit(app.exec_())
