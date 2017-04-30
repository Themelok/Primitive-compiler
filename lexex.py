import string
import sys


# <ШАГ> = "Step:" <ЧИСЛ> ";"
# <МЕТОД> = "Method:" "Euler"|"RungeKutta2"!|"RungeKutta4" ";"
# <ИНИЦПЕРЕМ> = <ПЕРЕМ> "=" <ЧИСЛ>
# <ЧИСЛ> = [<ЗНАК>] {/<НАТЧИС>/}["."{/<НАТЧИС>/}]
# <ПЕРЕМ> ::= <БУК> {<ЦИФ>|<БУК>}
# <НАТЧИС> ::= <ЦИФ>{ЦИФ}
# <ЗНАК> ::= "-" | "+"
# <БУК> ::= "a"|"b"|..|"z"
# <ЦИФ> ::= '0'|'1'|...|'9'


class Lexer:
    """
    Parsing Char by chr and returning tokens
    """
    COMMA, RSB, LSB, NUM, STEP, METHOD, COLON, SEMICOLON, PLUS, MINUS, EOF, DOT, VAR, BEGIN, END = range(15)
    WORDS = {'Step': STEP, 'Method:': METHOD, 'Begin': BEGIN, 'End': END}
    SYMBOLS = {';': SEMICOLON, '+': PLUS, '-': MINUS, '.': DOT, ':': COLON, '[':LSB, ']':RSB, ',': COMMA}

    raw_text_file = open('raw.txt', 'r')
    ch = ' '

    # def __init__(self, str):
    #     self.str = str
    # exit_char =
    # def __init__(self):
    #     self.next_token()

    def error(self, msg):
        char_no = self.raw_text_file.tell()
        print('LEX ERR: ' + msg + str(char_no))
        self.raw_text_file.close()

        sys.exit(1)

    def getc(self):
        self.ch = self.raw_text_file.read(1)

    def next_token(self):
        self.value = None
        self.sym = None
        while self.sym == None:
            if len(self.ch) == 0:
                self.sym = Lexer.EOF
                self.raw_text_file.close()
            elif self.ch.isspace():
                self.getc()
            elif self.ch in Lexer.SYMBOLS:
                self.sym = Lexer.SYMBOLS[self.ch]
                self.getc()
            elif self.ch.isdigit():
                num = ""
                while self.ch.isdigit() or self.ch == '.':
                    num += self.ch
                    self.getc()
                    if num.count('.') > 1:
                        self.error('Очень много точек в вещественном числе {} символ номер '.format(num))
                self.value = num
                self.sym = Lexer.NUM
            elif self.ch.isalpha():
                word = ""
                while self.ch.isalpha() or self.ch.isdigit():
                    word += self.ch
                    self.getc()
                if word in Lexer.WORDS:
                    self.sym = Lexer.WORDS[word]
                else:
                    self.sym = Lexer.VAR
                    self.value = word
            else:
                self.error('ХЗ че за символ {} номер'.format(self.ch))


# #
# lex =Lexer()
# print(lex.next_token())
# print(lex.sym)
class Node:
    """
    Builing Tree o nodes by Parser object
    """
    def __init__(self):
        self.node_tree = {}

    def add_too_tree(self, key, value):
        self.node_tree[key] = value


class Parser:
    """
    Parsing token by token and building node tree
    """
    BEGIN = range(1)

    def __init__(self, lexer, node):
        self.lexer = lexer()
        self.node = node()
        self.parse()

    def error(self, msg):

        char_no = self.lexer.raw_text_file.tell()
        print('Parser error: ' + msg + str(char_no))
        sys.exit(1)

    def eol_chek(self):
        self.lexer.next_token()
        token = self.lexer.sym
        if token != Lexer.SEMICOLON:
            self.error('Пропущен символ конца строки ";", в позиции ')

    def colon_check(self):
        self.lexer.next_token()
        token = self.lexer.sym
        if token != Lexer.COLON:
            self.error('Пропущен символ присваивания оператора, в позиции ')

    def parse_step(self):
        self.lexer.next_token()
        token = self.lexer.sym
        if token != Lexer.STEP:
            self.error('Пропущен оператор определения шага "Step", в позиции ')
        self.colon_check()
        self.lexer.next_token()
        self.node.add_too_tree('Step', self.lexer.value)
        self.eol_chek()

    def statement(self):
        # token = self.lexer.sym
        if self.lexer.sym != Lexer.BEGIN:
            self.error('Программа должна начинаться с оператора Begin:, а пришло {}'
                       .format(self.lexer.value))
        self.eol_chek()

        self.parse_step()

        self.lexer.next_token()
        if self.lexer.sym != Lexer.END:
            self.error('Программа должна заканчиваться оператором End, а пришло {}'
                       .format(self.lexer.value))
        self.eol_chek()

    def parse(self):
        self.lexer.next_token()
        self.statement()

        self.lexer.next_token()
        if (self.lexer.sym != Lexer.EOF):
            self.error('Неправильный синтаксис выражения')
        else:
            print('OK')
            # return self.node


p = Parser(Lexer, Node)
print(p.node.node_tree)
