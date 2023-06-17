import torch
from verify.opacityy import superp

############################################
# set the super-rectangle range
############################################
# set the initial in super-rectangle
INIT = [[0, 1],\
         [0,0],\
            [1, 10],
              [0,0],\
        ]
INIT_SHAPE = 1  # 2 for circle, 1 for rectangle

SUB_INIT = []
SUB_INIT_SHAPE = []

# the the unsafe in super-rectangle
UNSAFE = [[0 , 10] ,
          [0,1],\
            [0, 10],
                [0,1],\
        ]
UNSAFE_SHAPE = 1  # 2 for circle, 1 for rectangle

SUB_UNSAFE = []
SUB_UNSAFE_SHAPE = []

# the the domain in super-rectangle
DOMAIN = [[0 , 10] ,
          [0,1],\
            [0, 10],
                [0,1],\
        ]
DOMAIN_SHAPE = 1  # 1 for rectangle




############################################
# set the range constraints
############################################
# accept a two-dimensional tensor and return a
# tensor of bool with the same number of columns
def cons_init(x):
    return torch.pow(x[:, 0], 2) + \
           torch.pow(x[:, 2], 2) <= 1 + \
           superp.TOL_DATA_GEN # equivalent to True


def cons_unsafe(x):
    inner_box = torch.pow(x[:, 0], 2) + \
                torch.pow(x[:, 2], 2) <= 1 + \
                superp.TOL_DATA_GEN
    return ~inner_box  # x[:, 0] stands for x1 and x[:, 1] stands for x2
    # x[:, 0] stands for x1 and x[:, 1] stands for x2


def cons_domain(x):
    return x[:, 0] == x[:, 0]  # equivalent to True





############################################
# set the vector field
############################################
# this function accepts a tensor input and returns the vector field of the same size
def vector_field(x, ctrl_nn):
    # the vector of functions
    def f(i, x):
        if i == 1:
            return x[:, 1]  # x[:, 1] stands for x2
        elif i == 2:
            return x[:, 0] + x[:, 1]
            # x[:, 0] stands for x1
        elif i == 3:
            return x[:, 3]  # x[:, 1] stands for x4
        elif i == 4:
            return x[:, 2] + x[:, 3]
            # x[:, 0] stands for x3
        else:
            print("Vector function error!")
            exit()

    vf = torch.stack([f(i + 1, x) for i in range(superp.DIM_S)], dim=1)
    return vf