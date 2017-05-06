# TODO: Проверить чтобы имена переменных в варс0 и коэф не содержали ключевых слов тригономтрии и dx
# from lexex import FINALNODETREE
import sys
import TOKENS as TKS
import ERRORS as ER

# print(FINALNODETREE)

# PLH_ERROR="Jib,"
class PostParserHandler:
    def __init__(self, nodetree):
        self.PLH_ERROR=""
        self.nt = nodetree
        self.lexems = [k for l in [TKS.WORDS.keys(), TKS.MATHFUNC.keys(), TKS.METHODS.keys()] for k in l]
        self.chek_vars_and_diffs()
        self.replace_coeff()

        # self.replace_sin()
        # self.replace_cos()
        # self.replace_tg()
        # self.replace_pi()
        self.replace_pow()

    def error(self, msg):
        print('Ошибка постобработчика: ' + msg)
        f=open('plh_err.txt','w')
        PLH_ERROR = 'Ошибка постобработчика: ' + str(msg)
        f.write(PLH_ERROR)
        f.close()
        # print(PLH_ERROR)
        sys.exit(1)

    def chek_vars_and_diffs(self):
        if len(set(self.nt['Expr'].keys())) != len(set(self.nt['Vars0'].keys())):
            self.error(
                ER.POST_PARS_ERRORS[0].format(len(set(self.nt['Expr'].keys())), len(set(self.nt['Vars0'].keys()))))
        for dif in [k[1] for k in set(self.nt['Expr'].keys())]:
            if dif not in set(self.nt['Vars0'].keys()):
                self.error(ER.POST_PARS_ERRORS[1].format(dif))
        for dif in [k[1] for k in set(self.nt['Expr'].keys())]:
            if dif in set(self.nt['Coeff'].keys()):
                self.error(ER.POST_PARS_ERRORS[2].format(dif, dif))

    def replace_coeff(self):
        """
        Замена коэффциентов их значениями, если всё успешно .pop('Coeff')
        :return: None
        """
        for k, v in self.nt['Expr'].items():
            for coef in self.nt['Coeff'].items():
                v = v.replace(coef[0], coef[1])
            chars_only = [char for char in v.replace('sin', "").replace('cos', '').replace('pi', "").replace('tg', '')
                          if char.isalpha()]
            for char in chars_only:
                if char not in self.nt['Vars0']:
                    self.error(ER.POST_PARS_ERRORS[3].format(k, char))
            self.nt['Expr'][k] = v

        self.nt.pop('Coeff')

    def replace_sin(self):
        result = self.nt
        for v in result['Expr'].items():
            if 'sin' in v[1]:
                newstr = v[1].replace('sin', 'math.sin')
                result['Expr'][v[0]] = newstr
        self.nt = result

    def replace_cos(self):
        result = self.nt
        for v in result['Expr'].items():
            if 'cos' in v[1]:
                newstr = v[1].replace('cos', 'math.cos')
                result['Expr'][v[0]] = newstr
        self.nt = result

    def replace_tg(self):
        result = self.nt
        for v in result['Expr'].items():
            if 'tg' in v[1]:
                newstr = v[1].replace('tg', 'tan')
                result['Expr'][v[0]] = newstr
        self.nt = result


    def replace_pi(self):
        result = self.nt
        for v in result['Expr'].items():
            if 'pi' in v[1]:
                newstr = v[1].replace('pi', 'math.pi')
                result['Expr'][v[0]] = newstr
        self.nt = result

    def replace_pow(self):
        result = self.nt
        for v in result['Expr'].items():
            if '^' in v[1]:
                newstr = v[1].replace('^', '**')
                result['Expr'][v[0]] = newstr
        self.nt = result


# p = PostParserHandler(FINALNODETREE)
#
# result = p.nt
# print(result)
