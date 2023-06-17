import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
def calc_e(x):
    # y = 0.049602643328127936 * x*x*x*x+ 0.2072056986248578 * x*x*x + 0.48947384885936057 * x*x + 0.964249926959191 * x + 1.0019684997084841  exp

    # y = 1.0100097652819067 *x+ 0.9999669016648912    #[0,0.02]  yita = 3.424305622634627e-05    yita(最大误差)
    # y = 1.0304133159807205 *x+ 0.9995593067413109    #[0.02,0.04] yita = 3.3766965830572815e-05
    # y = 1.0512290457449436 *x+ 0.9987271632588013      #[0.04,0.06] yita = 3.4449103789135904e-05
    # y = 1.072519013268418 *x+ 0.9974499043043142            #[0.06,0.08] yita = 3.550144494024465e-05
    y = 6.073576959321154 *x+ -4.842380159475544       #[0.08,0.1] yita = 3.621862170044565e-05
    return y
if __name__ == "__main__":
    t = np.linspace(1.6, 2, 20, endpoint=False)
    # t2 = np.linspace(0.0, 0.02, 10)
    # t = np.concatenate((t1, t2))
    print(t)  # 横轴数据
    y = np.empty_like(t)
    for i, x in enumerate(t):
        y[i] = calc_e(x)
        print('e^', x, ' = ', y[i], '(近似值)\t', math.exp(x), '(真实值)',math.exp(x)-y[i],'（误差）')
        # print '误差：', y[i] - math.exp(x)
    plt.figure(facecolor='w')
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.plot(t, y, 'r-', t, y, 'go', linewidth=2)
    plt.title(u'Taylor展式的应用 - 指数函数', fontsize=18)
    plt.xlabel('X', fontsize=15)
    plt.ylabel('exp(X)', fontsize=15)
    plt.grid(True)
    plt.show()