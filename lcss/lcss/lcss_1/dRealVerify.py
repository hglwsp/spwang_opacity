from dreal import *
import numpy as np


def dRealReLU(x):
    res = [[if_then_else(ele > 0, ele, 0) for ele in row] for row in x]
    return np.array(res)


def preprocess(x1, x2, B_diff_x1, B_diff_x2):
    w_i_1 = np.load("./network/W_i_1.npy")
    w_1_2 = np.load("./network/W_1_2.npy")
    w_2_o = np.load("./network/W_2_o.npy")

    b_i_1 = np.load("./network/b_i_1.npy").reshape(-1, 1)
    b_1_2 = np.load("./network/b_1_2.npy").reshape(-1, 1)
    b_2_o = np.load("./network/b_2_o.npy").reshape(-1, 1)

    hidden1 = dRealReLU(np.dot(np.transpose(w_i_1), np.array([x1, x2]).reshape(-1, 1)) + b_i_1)
    hidden2 = dRealReLU(np.dot(np.transpose(w_1_2), hidden1) + b_1_2)
    u = (np.dot(np.transpose(w_2_o), hidden2) + b_2_o)[0][0]

    ##################################################
    # x1_diff = x2
    # x2_diff = -x1 - x2 + x2^2 + x1^2*x2 + u
    ##################################################
    x1_diff = x2
    x2_diff = -x1 - x2 + x2 * x2 + x1 * x1 * x2 + u
    B_diff = B_diff_x1 * x1_diff + B_diff_x2 * x2_diff

    return B_diff


def drealTest(a):
    x1 = Variable("x1")
    x2 = Variable("x2")

    B = a[0] + a[1] * x1 + a[2] * x2 + a[3] * x1 * x1 + a[4] * x2 * x2 + a[5] * x1 * x2
    B_diff_x1 = a[1] + 2 * a[3] * x1 + a[5] * x2
    B_diff_x2 = a[2] + 2 * a[4] * x2 + a[5] * x1
    B_diff = preprocess(x1, x2, B_diff_x1, B_diff_x2)

    f_sat = And(-0.2 <= x1, x1 <= 0.2,
                -0.2 <= x2, x2 <= 0.2,
                B < 0)
    print(CheckSatisfiability(f_sat, 0.001))

    f_sat = And(1.2 <= x1, x1 <= 1.3,
                -0.1 <= x2, x2 <= 0.1,
                B > 0)
    print(CheckSatisfiability(f_sat, 0.001))

    f_sat = And(-2 <= x1, x1 <= 2,
                -2 <= x2, x2 <= 2,
                -0.00001 <= B, B <= 0.00001,
                B_diff < 0)
    print(CheckSatisfiability(f_sat, 0.001))


if __name__ == '__main__':
    a = [32718.4096307, 18648.2708041, -7629.1378154, -43632.2410643, -119036.454357, -54261.724772]
    drealTest(a)
