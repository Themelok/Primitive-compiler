COMMA, RSB, LSB, NUM, STEP, METHOD, COLON, SEMICOLON, \
PLUS, MINUS, EOF, DOT, VAR, BEGIN, END, RANGE, LPAR, RPAR,\
RANGEVAL, EULER, RUNGKUT2, RUNGKUT4, COEFF, EQUAL, VARS0 = range(25)

WORDS = {'Step': STEP,
         'Method': METHOD,
         'Begin': BEGIN,
         'Range': RANGE,
         'End': END,
         'Coeff': COEFF,
         'Vars0': VARS0,
         }

SYMBOLS = {';': SEMICOLON,
           '+': PLUS,
           '=': EQUAL,
           '-': MINUS,
           ':': COLON,
           ',': COMMA
           }

BRACKETS = {'[': LSB,
            ']': RSB,
            '(': LPAR,
            ')': RPAR,
            }

DELIMETORS = {'.':DOT}

METHODS = {'Euler': EULER,
           'RungeKutta2': RUNGKUT2,
           'RungeKutta4': RUNGKUT4
           }