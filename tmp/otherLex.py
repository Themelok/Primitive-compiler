# Num = NatNum ! RealNum
# RealNum = NatNum'.'NatNum
# NatNum = Digit...Digit
# Letter = 'a'!'b'!...'z'
# Digit = '0'!'1'!..'9
import sys
import string as st
from pyparsing import ParseExpression

rs = """
Begin
Exp:
dx = b*y - a * x*c,
dy = x + y+z,
dz=b*z-a*y;
Vars0 y = 1, x = 1, z=0.5;
Coeff: a = 5,b=3,c=5;
Step: 0.05;
Range: 2.0;
Method: euler;
End

"""


class Lexer:
    SYMBOLS = {'DOT': '.', 'LPAR': '(', 'RPAR': ')', 'EOL': ';'}
    DIGITS = st.digits
    KEYWORDS = ('Begin\n', 'Exp:', 'Vars0:', 'Coeff:', 'Step:', 'Range:', 'Method:', '\nEnd')

    def __init__(self, raw_stroka=''):
        self.result = {}
        self.stroka = raw_stroka.strip()

        self.raw_dict=[]  # Changin in key_words_validate method
        self.key_words_validate()


    def key_words_validate(self):
        a= self.stroka[:6]
        b= self.KEYWORDS[0]
        if self.stroka[:6] != self.KEYWORDS[0]:
            raise Exception('Программа должна начинаться с оператора Begin')
        elif self.KEYWORDS[1] not in self.stroka:
            raise Exception('Отсутсвует оператор определения дифференциальных уравнений Exp:')
        elif self.KEYWORDS[2] not in self.stroka:
            print('Отсутсвует оператор определения начальных значений Vars0:')
            sys.exit(1)
        elif self.KEYWORDS[3] not in self.stroka:
            raise Exception('Отсутсвует оператор определения коэффициентов Coeff:')
        elif self.KEYWORDS[4] not in self.stroka:
            raise Exception('Отсутсвует оператор определения шага Step:')
        elif self.KEYWORDS[5] not in self.stroka:
            raise Exception('Отсутсвует оператор определения интервала Range:')
        elif self.KEYWORDS[6] not in self.stroka:
            raise Exception('Отсутсвует оператор определения метода Method:')
        elif self.stroka[-4:] != self.KEYWORDS[7]:
            raise Exception('Программа должна заканчиваться оператором End')
        else:
            self.raw_dict = self.stroka.replace('Begin', '').replace('End', '').split(';')



a = Lexer(rs)
# a.key_words_validate()
print(a.stroka)
print(a.raw_dict)
