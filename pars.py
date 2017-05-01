from pyparsing import *

# {'Range': '2.0',
#  'Coeff': ([(['a', '5'], {}), (['b', '3'], {}), (['c', '5'], {})], {'a': ['5'], 'b': ['3'], 'c': ['5']}),
#  'Exp': ([(['dx', 'b*y-a*x*c'], {}), (['dy', 'x+y+z'], {}), (['dz', 'b*z-a*y'], {})], {}), 'Step': '0.05',
#  'Vars0': ([(['y', '1'], {}), (['x', '1'], {}), (['z', '0.5'], {})], {'z': ['0.5'], 'y': ['1'], 'x': ['1']})}
# {'Range': '2.0', 'Exp': {'dy': 'x+y+z', 'dx': '3*y-5*x*5', 'dz': '3*z-5*y'}, 'Step': '0.05',
#  'Vars0': {'z': '0.5', 'y': '1', 'x': '1'}}

END = Literal(';').suppress()
POINT = Literal('.')
COMMA = Literal(',').suppress()
COLON = Word(':', max=1).suppress()
EQUAL = Literal('=').suppress()
VARNAME = Word(alphas, max=10)
NATNUM = Word(nums)  # 1234567890
SIGN = oneOf('+ -')
OPER = oneOf('+ - * / ^ ')
REALNUM = Combine(Optional(SIGN) + NATNUM + Optional(POINT + NATNUM))  # Real Numbers 2.3, 4.5
STEP = Dict(Group('Step' + COLON + REALNUM + END))  # Step: 0.01 ;
RANGE = Dict(Group('Range' + COLON + REALNUM + END))  # Range: 2.0 ;
VARINIT = Dict(Group(VARNAME + EQUAL + REALNUM))  # x=32.31
ZEROVAR = Dict(Group('Vars0' + COLON + VARINIT + Optional(OneOrMore(COMMA + VARINIT)) + END))
COEFF = Dict(Group('Coeff' + COLON + VARINIT + Optional(OneOrMore(COMMA + VARINIT)) + END))
EXPESS = Forward()
EXPESS << Combine((REALNUM | VARNAME) + ZeroOrMore(OPER + EXPESS), adjacent=False)
IDENT = Combine('d'+VARNAME)
FUNC = Group(IDENT + EQUAL + EXPESS)
DIFUR = Dict(Group('Exp' + COLON + FUNC + ZeroOrMore(COMMA + FUNC) + END))
STATE = Suppress("Start") + DIFUR + ZEROVAR + COEFF + STEP + RANGE + Suppress("Stop")
#
# result = dict(DIFUR.parseString('Exp: dx = a*x-y, dy = b * x -y, dz=800-2*4*x+z ;'))
# fin={}
# for v in result.values():
#     for k in v:
#         fin.update({k[0]:k[1]})
#         print(fin)
# result['Exp']={k[0]:k[1] for v in result.values() for k in v}
# print(result)
# # ))
filename = 'plain.txt'
FIN = open(filename)

try:
    result = dict(STATE.parseFile(FIN))
    print(result)

    for v in result['Exp']:
        for coef in result['Coeff']:
            v[1] = v[1].replace(coef[0],coef[1])
    result.pop('Coeff')
    result['Exp'] = {k[0]: k[1] for k in result['Exp']}
    result['Vars0'] = {k[0]: k[1] for k in result['Vars0']}
    if len(result['Exp']) != len(result['Vars0']):
        raise ParseExpression("Количество начальных условий не соответсвует количеству уравнений")
    if len({k for v in list(result['Exp'].values()) for k in v if k.isalpha()}) != len(result['Vars0']):
        raise ParseExpression('Не соответсвует количество коэффициентов')
#     # for v in result['Vars0']:
#     #     result['Vars0'][v[0]]="".join(v[1])
#     #     result['Vars0'].pop()
#             # pr?int(v[1])
    print(result)
except ParseException as pe:
    print(str(pe).replace('Expected', 'Ожидался'))
    print('Строка: '+ str(pe.lineno))
    print('Символ: '+ str(pe.col))


#
# fin = {}
# print(result.keys())
# for v in result['Exp']:
#     # for k in v:
#     fin.update({v[0]:v[1]})
# print(fin)
# result['Exp']={k[0]:k[1] for k in result['Exp']}
# print(result)
# print(len(result['Vars0']))
# print({k for v in list(result['Exp'].values()) for k in v if k.isalpha()})