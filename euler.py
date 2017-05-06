import matplotlib.pyplot as plt
import numpy as np
from math import sin as sin
from math import cos as cos
from math import tan as tan
from math import pi as pi


# from post_lex_handler import result
# print(result)
# METHOD = result.pop('Method')


# result = {'Range': '2.0',
#           'Exp': {'dx': '5555*x-2*y', 'dz': '800-2*4*x+z', 'dy': '2*x-y'},
#           'Vars0': {'y': '0.55', 'x': '0.02', 'z': '12'},
#           'Step': '0.05'}


class EulerMethod:
    def __init__(self, **kwargs):
        rang0 = eval(kwargs['Range'])[0]
        rang1 = eval(kwargs['Range'])[1]
        self.rang0 = rang0
        self.rang1 = float(rang1)
        self.step = float(kwargs['Step'])
        self.express = kwargs['Expr']
        self.time_arr = np.linspace(self.rang0,
                                    self.rang1,
                                    int(self.rang1 / self.step) + 1)
        self.vars0 = {k: eval(v) for k, v in kwargs['Vars0'].items()}
        self.res = {}
        self.gen_zeros()
        self.gen_res()
        # self.gen_plot()

    def gen_zeros(self):
        for k, v in self.vars0.items():
            self.res[k] = np.zeros(len(self.time_arr))
            self.res[k][0] = v

    def gen_res(self):
        for i in range(1, len(self.time_arr)):
            for k, v in self.res.items():
                dic = {k: v[i - 1] for k, v in self.res.items()}
                dic['sin'] = sin
                dic['cos'] = cos
                dic['tg'] = tan
                dic['pi'] = pi
                # print(dic)
                self.res[k][i] = round(self.res[k][i - 1] + \
                                       eval(self.express['d' + k],
                                            dic) \
                                       * self.step, 3)

    def gen_plot(self):
        color = ['red', 'green', 'blue', 'yellow']
        i = 0
        plt.figure()
        for k in self.res:
            plt.plot(self.time_arr, self.res[k], color=color[i])
            i += 1
        plt.xlabel('t')
        plt.show()

    def printval(self):

        self.res['t'] = self.time_arr
        return self.res

    def gen_arr(self):
        sting_arr = ""
        sting_arr += "t"
        for char in self.time_arr:
            sting_arr += "|{:^10}".format(round(float(char), 2))
        sting_arr += '\n'
        for k, v in self.res.items():
            sting_arr += k
            for l in v:
                sting_arr += "|{:^10}".format(round(float(l), 2))
            sting_arr += '\n'
        print(sting_arr)
        return sting_arr
# d = EulerMethod(**result)
# output = str(d.printval())
# # pretty_vals = {k:[v] for d.}
