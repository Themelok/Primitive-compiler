COMMA, RSB, LSB, NUM, STEP, METHOD, COLON, SEMICOLON, \
PLUS, MINUS, EOF, DOT, VAR, BEGIN, END, RANGE, LPAR, RPAR, \
RANGEVAL, EULER, RUNGKUT2, RUNGKUT4, COEFF, EQUAL, VARS0, POW, \
MULT, DIVIS, SIN, COS, TANG, EXPR = range(32)

WORDS = {'Step': STEP,
         'Method': METHOD,
         'Begin': BEGIN,
         'Range': RANGE,
         'End': END,
         'Coeff': COEFF,
         'Vars0': VARS0,
         'Expr': EXPR,
         }

SYMBOLS = {';': SEMICOLON,
           '=': EQUAL,
           ':': COLON,
           ',': COMMA
           }

BRACKETS = {'[': LSB,
            ']': RSB,
            }

MATHOP = {'/': DIVIS,
          '+': PLUS,
          '*': MULT,
          '-': MINUS,
          '^': POW,
          }
MATHFUNC = {'sin': SIN,
          'cos': COS,
          'tg': TANG,
          }

PARANTH = {'(': LPAR,
           ')': RPAR,
           }

DELIMETORS = {'.': DOT}

METHODS = {'Euler': EULER,
           'RungeKutta2': RUNGKUT2,
           'RungeKutta4': RUNGKUT4
           }
