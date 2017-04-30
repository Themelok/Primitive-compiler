import numpy as np
import matplotlib.pyplot as plt
from pars import result

a = 0.0
b = eval(result['Range'])
h = eval(result['Step'])
N = (b - a) / h
# y0 = 0.5
# x0 = 0.2
list(map(exec, ("{0}={1}".format(x[0],x[1]) for x in dict(result['Vars0']).items())))

# ordinary differential equation
def fy(x, y):
    return eval(result['Exp']['dy'])


def fx(x, y):
    return eval(result['Exp']['dx'])


def euler(f1x, f2y, ran, step, x0, y0):
    ts = np.linspace(0, ran, int(ran / step) + 1)
    xs = np.zeros(len(ts))
    ys = np.zeros(len(ts))
    xs[0] = x0
    ys[0] = y0
    for i in range(1, len(ts)):
        xs[i] = float(round(xs[i - 1] + f1x(xs[i - 1], ys[i - 1]) * step, 3))
        ys[i] = round(ys[i - 1] + f2y(xs[i - 1], ys[i - 1]) * step, 2)
    res = {'x': xs, 'y': ys, 't': ts}
    print(res)

    plt.figure()
    plt.plot(res['t'], res['y'], color='red')
    plt.plot(res['t'], res['x'], color='blue')
    plt.xlabel('t')
    plt.ylabel('y(t), x(t)')
    plt.show()

    plt.plot(res['x'], res['y'], color='green')
    plt.xlabel('x(t)')
    plt.ylabel('y(t)')
    plt.show()





if __name__ == "__main__":
    print(euler(fx, fy, b, h, x, y))
