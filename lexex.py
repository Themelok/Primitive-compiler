import sys
import TOKENS as TKS
import ERRORS as ERR


class Lexer:
    """
    Parsing Char by chr and returning tokens
    """

    raw_text_file = open('raw.txt', 'r')
    ch = ' '

    def error(self, msg):
        char_no = self.raw_text_file.tell()
        print('LEX ERR: ' + msg + str(char_no))
        self.raw_text_file.close()

        sys.exit(1)

    def lex_comma(self):
        """
        NOT USSING YET. LET IT BE HERE
        :return:
        """
        if self.ch != ',':
            self.error('Ожидался символ ",", а пришел {}. Cимвол номер '.format(self.ch))
        else:
            return ','

    def lex_num(self):
        num = ""
        while self.ch not in TKS.SYMBOLS and self.ch not in TKS.BRACKETS:
            if self.ch.isdigit() or self.ch in TKS.DELIMETORS:
                num += self.ch
                self.getc()
                if num.count('.') > 1:
                    self.error(ERR.LEX_ERRORS[2].format(num))
            elif self.ch =="\n":
                self.error(ERR.LEX_ERRORS[3].format(num))
            else:
                self.error(ERR.LEX_ERRORS[1].format(self.ch))
        if num[-1] == '.': num += '0'
        return num

    def getc(self):
        self.ch = self.raw_text_file.read(1)

    def next_token(self):
        self.value = None
        self.sym = None
        while self.sym == None:
            if len(self.ch) == 0:
                self.sym = TKS.EOF
                self.raw_text_file.close()
            # elif not self.ch in '\n\t':
            #     self.getc()
            elif self.ch.isspace():
                self.getc()
            elif self.ch in TKS.BRACKETS:
                self.sym = TKS.BRACKETS[self.ch]
                self.value = self.ch
                self.getc()
            elif self.ch in TKS.SYMBOLS:
                self.sym = TKS.SYMBOLS[self.ch]
                self.value = self.ch
                self.getc()
            elif self.ch.isdigit():
                self.value = self.lex_num()
                self.sym = TKS.NUM
            elif self.ch.isalpha():
                word = ""
                while self.ch.isalpha() or self.ch.isdigit():
                    word += self.ch
                    self.getc()
                if word in TKS.WORDS:
                    self.sym = TKS.WORDS[word]
                    self.value = word
                elif word in TKS.METHODS:
                    self.sym = TKS.METHODS[word]
                    self.value = word
                else:
                    self.sym = TKS.VAR
                    self.value = word
            else:
                self.error(ERR.LEX_ERRORS[0].format(self.ch))


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
        print('Parser error: ' + msg + "Символ номер " + str(char_no))
        sys.exit(1)

    def eol_chek(self):
        """
        Chek End Of Line symbol ';'
        :return:
        """
        self.lexer.next_token()
        token = self.lexer.sym
        if token != TKS.SEMICOLON:
            self.error('Пропущен символ конца строки ";", в позиции ')

    def check_equ(self):
        self.lexer.next_token()
        if self.lexer.sym == TKS.EQUAL:
            pass
        else:
            self.error('Пропущен символ равенства. ')

    def check_varname(self):
        self.lexer.next_token()
        if self.lexer.sym == TKS.VAR:
            return self.lexer.value
        else:
            self.error('Ошибка в определении имени переменной. ')

    def check_num(self):
        self.lexer.next_token()
        if self.lexer.sym == TKS.NUM:
            return self.lexer.value
        else:
            self.error('Ошибка в определении значения переменной. ')

    def colon_check(self, operator):
        """
        Chek COLON
        :return:
        """
        self.lexer.next_token()
        token = self.lexer.sym
        if token != TKS.COLON:
            self.error('Пропущен символ присваивания ":" оператора {}. '.format(operator))

    def parse_vars0(self):
        self.lexer.next_token()
        op = self.lexer.value
        if self.lexer.sym != TKS.VARS0:
            self.error(ERR.PARS_ERRORS['Vars0'][0])
        self.colon_check(op)
        vars_dict={}
        while self.lexer.ch != ';':
            k = self.check_varname()
            self.check_equ()
            v = self.check_num()
            vars_dict[k] = v
            if self.lexer.ch == ',':
                self.lexer.next_token()
            else: break

        self.eol_chek()
        self.node.add_too_tree('Vars0', vars_dict)

    def parse_coeff(self):
        self.lexer.next_token()
        op = self.lexer.value
        if self.lexer.sym != TKS.COEFF:
            self.error(ERR.PARS_ERRORS['COEFF'][0])
        self.colon_check(op)
        coeff_dict={}
        while self.lexer.ch != ';':
            k = self.check_varname()
            self.check_equ()
            v = self.check_num()
            coeff_dict[k] = v
            if self.lexer.ch == ',':
                self.lexer.next_token()
            else: break

        self.eol_chek()
        self.node.add_too_tree('Coeff', coeff_dict)

    def parse_step(self):
        self.lexer.next_token()
        op = self.lexer.value
        token = self.lexer.sym
        if token != TKS.STEP:
            self.error(ERR.PARS_ERRORS['STEP'][0])
        self.colon_check(op)
        self.lexer.next_token()
        step_value = self.lexer.value

        self.eol_chek()
        self.node.add_too_tree('Step', step_value)

    def pars_range(self):
        """
        Parsing Range statment, look like [ NUM , NUM]
         or <ИНТЕРВАЛ> ::= "Range:" "[" <ЧИСЛ> "," <ЧИСЛ> "]" ";" in EBNF form
        :return: Finally make add_too_tree method
        """
        self.lexer.next_token()
        op = self.lexer.value
        token = self.lexer.sym
        if token != TKS.RANGE:
            self.error(ERR.PARS_ERRORS['RANGE'][0])
        self.colon_check(op)
        self.lexer.next_token()
        if self.lexer.sym != TKS.LSB:
            self.error(ERR.PARS_ERRORS['RANGE'][1]
                       .format(self.lexer.value))
        else:
            range_value = self.lexer.value
            while self.lexer.sym != TKS.RSB:
                if self.lexer.sym == TKS.SEMICOLON:
                    self.error(ERR.PARS_ERRORS['RANGE'][2].format(self.lexer.value))
                elif self.lexer.sym == TKS.NUM or self.lexer.value in '[,]':
                    self.lexer.next_token()
                else:
                    self.error(ERR.PARS_ERRORS['RANGE'][3].format(self.lexer.value))

                range_value += self.lexer.value
                for l in '[,]':
                    if range_value.count(l) > 1: self.error(ERR.PARS_ERRORS['RANGE'][4].format(l))
        self.node.add_too_tree('Range', range_value)  # Add too tree
        self.eol_chek()

    def pars_method(self):
        """
        Parsing Method statement, look like Method: MEthodName
         or <МЕТОД> = "Method:" "Euler"|"RungeKutta2"!|"RungeKutta4" ";" in EBNF form
        :return: Finally make add_too_tree method
        """
        self.lexer.next_token()
        op = self.lexer.value
        if self.lexer.sym != TKS.METHOD:
            self.error(ERR.PARS_ERRORS['METHOD'][0])
        self.colon_check(op)
        self.lexer.next_token()
        token = self.lexer.value
        if self.lexer.value not in TKS.METHODS:
            self.error(ERR.PARS_ERRORS['METHOD'][1].format(self.lexer.value))
        method_value = self.lexer.value
        self.eol_chek()
        self.node.add_too_tree('Method', method_value)

    def statement(self):
        if self.lexer.sym != TKS.BEGIN:
            self.error('Программа должна начинаться с оператора Begin:, а пришло {}'
                       .format(self.lexer.value))
        self.eol_chek()

        self.parse_vars0()
        self.parse_coeff()
        self.parse_step()
        self.pars_range()
        self.pars_method()

        self.lexer.next_token()
        if self.lexer.sym != TKS.END:
            self.error('Программа должна заканчиваться оператором End, а пришло {}'
                       .format(self.lexer.value))

        # TODO: Bug HERE, when NO semicolon
        self.eol_chek()

    def parse(self):
        self.lexer.next_token()
        self.statement()

        self.lexer.next_token()
        if (self.lexer.sym != TKS.EOF):
            self.error('Неправильный синтаксис выражения')
        else:
            print('OK')
            # return self.node


p = Parser(Lexer, Node)
print(p.node.node_tree)
