import torch
import torch.nn as nn
import acti
import numpy as np
from functools import reduce
from operator import mul

############################################
# set default data type to double; for GPU
# training use float
############################################
torch.set_default_dtype(torch.float64)
torch.set_default_tensor_type(torch.DoubleTensor)
# torch.set_default_dtype(torch.float32)
# torch.set_default_tensor_type(torch.FloatTensor)


VERBOSE = 1 # set to 1 to display epoch and batch losses in the training process
VISUAL = 1 # plot figure or not

FINE_TUNE = 0   # set to 1 for fine-tuning a pre-trained model
FIX_CTRL = 0
FIX_BARR = 0



############################################
# set the system dimension
############################################
DIM_S = 4 # dimension of system
DIM_C = 2 # dimension of controller input

############################################
# set the network architecture
############################################
N_H_B = 1 # the number of hidden layers for the barrier
D_H_B = 16
#D_H_B = 10 # the number of neurons of each hidden layer for the barrier

N_H_C = 1 # the number of hidden layers for the controller
D_H_C = 5
#D_H_C = 5 # the number of neurons of each hidden layer for the controller

############################################
# for activation function definition
############################################
BENT_DEG = 0.0001

BARR_ACT = nn.ReLU()
# BARR_ACT = nn.LeakyReLU(negative_slope=0.0001, inplace=False)
CTRL_ACT = acti.my_act()
# CTRL_ACT = nn.LeakyReLU(negative_slope=0.0001, inplace=False)
# CTRL_ACT = nn.ReLU()
# CTRL_ACT = nn.Sigmoid()

BARR_OUT_BOUND = 1e16 # set the output bound of the barrier NN
CTRL_OUT_BOUND = 1e16 # set the output bound of the controller NN: for bounded controller


############################################
# set loss function definition
############################################
TOL_INIT = 0 #0.01
TOL_SAFE = 0
#TOL_ACC = 0.05

TOL_LIE = 0.0 #0.02
TOL_NORM_LIE = 0.0
TOL_BOUNDARY = 0.01 #0.01 # initial boundary 0.01

WEIGHT_LIE = 1.0
WEIGHT_NORM_LIE = 1.0#0



DECAY_LIE = 1 # decay of lie weight 0.1 works, 1 does not work
DECAY_INIT = 1
DECAY_UNSAFE = 1
DECAY_DIFF = 1
DECAY_U = 1





############################################
# number of training epochs
############################################
EPOCHS = 500

############################################
# my own scheduling policy: 
# rate = alpha / (1 + beta * epoch^gamma)
############################################
#ALPHA = 0.01
ALPHA = 0.01
BETA = 0.2
GAMMA = 5


############################################
# training termination flags
############################################
#LOSS_OPT_FLAG = 1e-16
LOSS_OPT_FLAG = 1e-16
TOL_MAX_GRAD = 5
GRAD_CTRL_FACTOR = 1.4


############################################
# for training set generation
############################################
TOL_DATA_GEN = 1e-16

DATA_EXP_I = np.array([6,6,4,4])
    # for sampling from initial; length = prob.DIM
DATA_LEN_I = np.power(2, DATA_EXP_I) 
    # the number of samp,les for each dimension of domain
BLOCK_EXP_I = np.array([4,4,2,2])
    # 0 <= BATCH_EXP <= DATA_EXP
BLOCK_LEN_I = np.power(2, BLOCK_EXP_I) 
    # number of batches for each dimension

DATA_EXP_U1 = np.array([6,6,4,4]) # for sampling from initial; length = prob.DIM
DATA_LEN_U1 = np.power(2, DATA_EXP_U1) # the number of samples for each dimension of domain
BLOCK_EXP_U1 = np.array([4,4,2,2]) # 0 <= BATCH_EXP <= DATA_EXP
BLOCK_LEN_U1 = np.power(2, BLOCK_EXP_U1) # number of batches for each dimension

DATA_EXP_U2 = np.array([6,6,4,4]) # for sampling from initial; length = prob.DIM
DATA_LEN_U2 = np.power(2, DATA_EXP_U2) # the number of samples for each dimension of domain
BLOCK_EXP_U2 = np.array([4,4,2,2]) # 0 <= BATCH_EXP <= DATA_EXP
BLOCK_LEN_U2 = np.power(2, BLOCK_EXP_U2) # number of batches for each dimension

DATA_EXP_D = np.array([6,6,4,4]) # for sampling from initial; length = prob.DIM
DATA_LEN_D = np.power(2, DATA_EXP_D) # the number of samples for each dimension of domain
BLOCK_EXP_D = np.array([4,4,2,2]) # 0 <= BATCH_EXP <= DATA_EXP
BLOCK_LEN_D = np.power(2, BLOCK_EXP_D) # number of batches for each dimension


############################################
# for plotting
############################################
PLOT_EXP_B = np.array([10,10]) # sampling from domain for plotting the boundary of barrier using contour plot
PLOT_LEN_B = PLOT_EXP_B # the number of samples for each dimension of domain, usually larger than superp.DATA_LEN_D

PLOT_EXP_V = np.array([3,3]) # sampling from domain for plotting the vector field
PLOT_LEN_V = np.power(2, PLOT_EXP_V) # the number of samples for each dimension of domain, usually equal to PLOT_LEN_P

PLOT_EXP_P = np.array([3,3]) # sampling from domain for plotting the scattering sampling points, could be equal to PLOT_EXP_V
PLOT_LEN_P = np.power(2, PLOT_EXP_P) # the number of samples for each dimension of domain

PLOT_VEC_SCALE = 150