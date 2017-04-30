import numpy as np
from pars import result
import matplotlib.pyplot as plt
# result = {'Range': '2.0',
#           'Exp': {'dx': '5555*x-2*y', 'dz': '800-2*4*x+z', 'dy': '2*x-y'},
#           'Vars0': {'y': '0.55', 'x': '0.02', 'z': '12'},
#           'Step': '0.05'}


class EulerMethod:
    def __init__(self, **kwargs):
        self.rang = float(kwargs['Range'])
        self.step = float(kwargs['Step'])
        self.express = kwargs['Exp']
        self.time_arr = np.linspace(0,
                                    self.rang,
                                    int(self.rang/self.step)+1)
        self.vars0 = {k:eval(v) for k,v in kwargs['Vars0'].items()}
        self.res={}
        self.gen_zeros()
        self.gen_res()
        self.gen_plot()

    def gen_zeros(self):
        for k,v in self.vars0.items():
            self.res[k]=np.zeros(len(self.time_arr))
            self.res[k][0] = v

    def gen_res(self):
        for i in range(1, len(self.time_arr)):
            for k,v in self.res.items():
                self.res[k][i] = round(self.res[k][i-1]+\
                                 eval(self.express['d'+k],
                                      {k:v[i-1] for k, v in self.res.items()})\
                                 *self.step, 3)
    def gen_plot(self):
        color=['red', 'green', 'blue', 'yellow']
        i=0
        plt.figure()
        for k in self.res:
            plt.plot(self.time_arr, self.res[k], color=color[i])
            i+=1
        plt.xlabel('t')
        plt.show()








    def printval(self):
        print(self.rang)
        print(self.step)
        print(self.time_arr)
        print(self.vars0)
        print(self.res)

d=EulerMethod(**result)
d.printval()