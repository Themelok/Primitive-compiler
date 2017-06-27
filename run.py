import os
import sys
from tkinter import *
import matplotlib.pyplot as plt
from lexex import Node as Node
from lexex import Lexer as Lexer
from lexex import Parser as Parser
from lexex import PreLexer as PreLexer
from euler import EulerMethod as EulerMethod
from post_lex_handler import PostParserHandler as PostParserHandler


class MyUI(Tk):
    def __init__(self):
        super().__init__()

        self.res_arr = {}
        self.time_arr = []
        self.initUI()
        self.Pack()

    def initUI(self):
        self.f = Frame(self)
        self.title('Анализатор')
        self.text_area = Text(self.f, height=15, width=140, font='Monospace 12', undo=True)
        self.xscroll = Scrollbar(self.f, orient=HORIZONTAL)
        self.result = Text(self.f, width=140, font='Monospace 12', height=3, background='#ccc', wrap=NONE,
                           xscrollcommand=self.xscroll.set)
        st = ''
        self.result.insert(INSERT, st)
        self.result.configure(xscrollcommand=self.xscroll.set)
        self.xscroll.config(command=self.result.xview)
        self.result.configure(state=DISABLED)


        self.btn_doit = Button(self.f, text='DO IT!', command=self.do_it)
        self.show_plot = Button(self.f, text='Show Plot', command=self.gen_plot, state=DISABLED)

    def Pack(self):
        self.f.pack()
        self.text_area.pack()
        self.btn_doit.pack(fill=X)
        self.show_plot.pack()
        self.result.pack(fill=X)
        self.xscroll.pack(fill=X)

    def gen_plot(self):
        color = ['red', 'green', 'blue', 'yellow']
        i = 0

        plt.figure()
        for k in self.res_arr:
            plt.plot(self.time_arr, self.res_arr[k], color=color[i], label='d'+k)
            i += 1
        plt.xlabel('t')
        plt.grid(True)
        plt.legend(loc='lower right')
        plt.show()
        print(self.time_arr)
    def magic(self):
        file = 'input.txt'
        # prelexer=PreLexer(file)   ### PreLexer ON/OFF
        lexer = Lexer(file)
        node = Node()
        p = Parser(lexer, node)
        FINALNODETREE = p.node.node_tree
        p = PostParserHandler(FINALNODETREE)
        result = p.nt
        METHOD = result.pop('Method')
        d = EulerMethod(**result)
        OUTPUT = d.gen_arr()
        self.res_arr = d.printval()
        self.time_arr = self.res_arr.pop('t')
        print(self.res_arr)
        return OUTPUT

    def do_it(self):
        file = open('input.txt', 'w')
        file.write(self.text_area.get('1.0', END))
        file.close()
        try:
            try:
                self.text_area.tag_delete('ER')
            except:
                pass
            out = self.magic()
            self.result.configure(state=NORMAL)
            self.result.delete('1.0', END)
            self.result.insert(END, out)
            self.result.configure(state=DISABLED,  background='#a8ffcd')
            self.show_plot.configure(state=NORMAL)
        except:
            self.result.configure(state=NORMAL)
            self.result.delete('1.0', END)
            if os.path.isfile('pre_lex_err.txt'):
                err = open('pre_lex_err.txt').readline()
                l_n = int(err.split()[-1])
                self.text_area.tag_configure('ER', background='#ffa8a8')
                self.text_area.tag_add('ER', '{}.0'.format(l_n), '{}.0 lineend'.format(l_n))
                os.remove('pre_lex_err.txt')
            elif os.path.isfile('plh_err.txt'):
                err = open('plh_err.txt').readline()
                os.remove('plh_err.txt')
                self.text_area.tag_configure('ER', background='#ffa8a8')
                self.text_area.tag_add('ER', '2.0', '2.0 lineend')
            elif os.path.isfile('pars_err.txt'):
                err = open('pars_err.txt').readline()
                char_no= int(err.split()[-1])
                self.text_area.tag_configure('ER', background='#ff0000', foreground="#fff", underline=True)
                self.text_area.tag_add('ER', "1.0+{}c".format(char_no-2))
                os.remove('pars_err.txt')
            elif os.path.isfile('lex_err.txt'):
                err = open('lex_err.txt').readline()
                char_no= int(err.split()[-1])
                self.text_area.tag_configure('ER', background='#ff0000', foreground="#fff", underline=True)
                self.text_area.tag_add('ER', "1.0+{}c".format(char_no-2))
                os.remove('lex_err.txt')
            self.result.insert(END, err)
            self.result.configure(state=DISABLED,  background='#ffa8a8')
if __name__ == '__main__':
    ui = MyUI()
    ui.mainloop()
