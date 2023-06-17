import torch
import superp

############################################
# set the super-rectangle range
############################################
# set the initial in super-rectangle

DIM_S = 4    # barrier need 4-dims,it only connection with x1,x2,x3,x4,without input u
INIT = [[0,1],\
         [1,3],\
        ]
INIT_SHAPE = 3  # 4 for top-triangle, 3 for down-triangle, 2 for circle, 1 for rectangle

# because of the domain, we need deal
# the the unsafe in super-rectangle
UNSAFE =  [[0,15] ,\
          [0,15],\
        ]
UNSAFE_SHAPE = 3  # 2 for circle, 1 for rectangle

# UNSAFE_1 =  [[20,30] ,\
#           [20,30],\
#             [20,30],\
#                 [20,30],\
#         ]
UNSAFE_1_SHAPE = 3  # 2 for circle, 1 for rectangle

# the the domain in super-rectangle
DOMAIN = [[0,15] ,\
          [0,15],\
        ]

# DOMAIN_1 =  [[20,30] ,\
#           [20,30],\
#             [20,30],\
#                 [20,30],\
#         ]

DOMAIN_SHAPE = 1  # 1 for rectangle

#para


############################################
# set the range constraints
############################################
# accept a two-dimensional tensor and return a
# tensor of bool with the same number of columns
def cons_init(x):
    # return x[:, 0] == x[:, 0]
    inner_box = ((x[:, 1] - x[:, 0]) * (x[:, 1] - x[:, 0]) <= 1.2*1.2) \
                & (0 <= x[:, 0]) & (x[:, 0] <= 1) \
                & (1 <= x[:, 1]) & (x[:, 1] <= 3)
    return inner_box



def cons_unsafe(x):
    inner_box = ((x[:, 1] - x[:, 0]) * (x[:, 1] - x[:, 0]) > 4) \
                & (0 <= x[:, 0]) & (x[:, 0] <= 15) \
                & (0 <= x[:, 1]) & (x[:, 1] <= 15)
    return inner_box



def cons_domain(x):
    return x[:, 0] == x[:, 0]  # equivalent to True



############################################
# set the vector field
############################################
# this function accepts a tensor input and returns the vector field of the same size
def vector_field(x, ctrl_nn):
    # the vector of functions
    def f(i, x):
        #######################################################
        # controller is connected with u and x
        #######################################################
        # controller with two inputs
        ######################################################
        # field
        ######################################################
        #  x => i = 1,3, x with hat => i = 2,4
        # fix controller in [0,100], need *0.01
        ######################################################
        if i == 1:
            x_ = x[:,0]+ 1-x[:,0]/15
            return x_
        elif i == 2:
            x_ = x[:,1]+ 1-x[:,1]/15
            return x_
        else:
            print("Vector function error!")
            exit()

    vf = torch.stack([f(i + 1, x) for i in range(superp.DIM_S)], dim=1)
    return vf