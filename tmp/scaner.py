# raw_stroka = """25.62;"""
# stroka=raw_stroka.replace(' ','').replace('\n', '').replace('\t', '')
# NUM = ""
#
#
# for k,v in enumerate(stroka):
#     if v.isdigit():
#         NUM += v
#         if stroka[k+1]=='.':
#             if not stroka[k+2].isdigit():
#                 raise Exception('Ожидался числовой символ, а пришел {}'.format(stroka[k+2]))
#                 #return
#             else:
#                 continue
#     if v == '.':
#         if stroka[k-1].isdigit() and stroka[k+1].isdigit() and v not in NUM:
#             NUM += '.'
#         else:
#             raise Exception('Неожиданный символ {}'.format(v, k))
#             #return
#
# print(NUM)


def sysstdin(str):
