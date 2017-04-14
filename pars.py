from pyparsing import *

END = Literal(';').suppress()
POINT = Literal('.')
COMMA = Literal(',').suppress()
COLON = Word(':', max=1).suppress()
EQUAL = Literal('=').suppress()
VARNAME = Word(alphas, max=1)
NATNUM = Word(nums)  # 1234567890
SIGN = oneOf('+ -')
OPER = oneOf('+ - * / ^ ')
REALNUM = Combine(Optional(SIGN) + NATNUM + Optional(POINT + NATNUM))  # Real Numbers 2.3, 4.5
STEP = Dict(Group('Step' + COLON + REALNUM + END))  # Step: 0.01 ;
RANGE = Dict(Group('Range' + COLON + REALNUM + END))  # Range: 2.0 ;
VARINIT = Dict(Group(VARNAME + Suppress('=') + REALNUM))  # x=32.31
ZEROVAR = Dict(Group('Vars0' + COLON + VARINIT + Optional(COMMA + VARINIT) + END))
EXPESS = Forward()
EXPESS << Combine((REALNUM | VARNAME) + ZeroOrMore(OPER + EXPESS), adjacent=False)
IDENT = Combine(VARNAME + "'")
FUNC = Dict(Group(IDENT + EQUAL + EXPESS))
DIFUR = Dict(Group('Exp' + COLON + FUNC + ZeroOrMore(COMMA + FUNC) + END))
STATE = Suppress("Start") + DIFUR + ZEROVAR + STEP + RANGE + Suppress("Stop")

# result = dict(STATE.parseString(
#                                 """
#                                 Start
#                                 Exp: x' = 12 + y  + 15, y' = 2*x + 7 ;
#                                 Vars0: y = 0.2, x = 20 ;
#                                 Step: 0.05;
#                                 Range: 2.0;
#                                 Stop
#                                 """
# ))
filename = 'plain.txt'
FIN = open(filename)

result = dict(STATE.parseFile(FIN))
result = dict(result)
print(result)
