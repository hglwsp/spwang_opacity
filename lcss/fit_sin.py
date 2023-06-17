import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq


# 我们要拟合的目标函数
def real_func(x):
    return np.sin(2*np.pi*x)


# 我们自己定义的多项式函数
def fit_func(p, x):
    f = np.poly1d(p)  # np.poly1d([2,3,5,7])返回的是函数，2x3 + 3x2 + 5x + 7
    ret = f(x)
    return ret


# 计算残差
def residuals_func(p, x, y):
    ret = fit_func(p, x) - y
    return ret


# 返回残差和正则项
def residuals_func_regularization(p, x, y):
    ret = fit_func(p, x) - y
    ret = np.append(ret,
                    np.sqrt(0.5 * regularization * np.square(p)))  # L2范数作为正则化项
    return ret


def fitting(M=0):
    """
        M    为 多项式的次数
    """
    # 随机初始化多项式参数
    p_init = np.random.rand(M + 1)  # 返回M+1个随机数作为多项式的参数
    # 最小二乘法:具体函数的用法参见我的博客：残差函数，残差函数中参数一，其他的参数
    p_lsq = leastsq(residuals_func, p_init, args=(x, y))
    # 求解出来的是多项式当中的参数，就是最小二乘法中拟合曲线的系数
    # print('Fitting Parameters:', p_lsq[0])
    return p_lsq[0]


# 书中10个点,对y加上了正态分布的残差
x = np.linspace(0, 1, 10)
y_old = real_func(x)
y = [np.random.normal(0, 0.1) + yi for yi in y_old]


x_real = np.linspace(0, 1, 1000)
y_real = real_func(x_real)


# # 画出10个散点，sin图像，和拟合的曲线
# plt.plot(x_real, y_real, label="real")
# plt.plot(x, y, 'bo', label='point')
# plt.plot(x_real, fit_func(fitting(9), x_real), label="fitted curve")
# plt.legend()
# plt.show()


# 画出添加正则项的曲线
regularization = 0.0001
p_init = np.random.rand(9 + 1)
p_lsq_regularization = leastsq(
    residuals_func_regularization, p_init, args=(x, y))


# 画出原sin图像，不加正则项的图像，加上正则项的图像，10个点的散点图
# 不加正则项和加上正则项都是9次方，10个系数
plt.plot(x_real, real_func(x_real), label='real')
plt.plot(x_real, fit_func(fitting(9), x_real), label='fitted curve')
plt.plot(
    x_real,
    fit_func(p_lsq_regularization[0], x_real),
    label='regularization')
plt.plot(x, y, 'bo', label='noise')
plt.legend()
plt.show()
