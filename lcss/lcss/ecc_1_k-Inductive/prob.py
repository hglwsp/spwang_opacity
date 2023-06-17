import torch
import superp

############################################
# set the super-rectangle range
############################################
# set the initial in super-rectangle

DIM_S = 4    # barrier need 4-dims,it only connection with x1,x2,x3,x4,without input u
INIT = [[21.5,22],\
         [21,21.5],\
            [21,22],\
              [21,22],\
        ]
INIT_SHAPE = 3  # 4 for top-triangle, 3 for down-triangle, 2 for circle, 1 for rectangle

# because of the domain, we need deal
# the the unsafe in super-rectangle
UNSAFE =  [[10,30] ,\
          [10,30],\
            [10,30],\
                [10,30],\
        ]
UNSAFE_SHAPE = 3  # 2 for circle, 1 for rectangle

# UNSAFE_1 =  [[20,30] ,\
#           [20,30],\
#             [20,30],\
#                 [20,30],\
#         ]
UNSAFE_1_SHAPE = 3  # 2 for circle, 1 for rectangle

# the the domain in super-rectangle
DOMAIN = [[10,30] ,\
          [10,30],\
            [10,30],\
                [10,30],\
        ]

# DOMAIN_1 =  [[20,30] ,\
#           [20,30],\
#             [20,30],\
#                 [20,30],\
#         ]

DOMAIN_SHAPE = 1  # 1 for rectangle

#para
alpha = 0.05
Te=15
ah=0.0036
Th=55
ae=0.008

############################################
# set the range constraints
############################################
# accept a two-dimensional tensor and return a
# tensor of bool with the same number of columns
def cons_init(x):
    # return x[:, 0] == x[:, 0]
    inner_box = ((x[:, 3] - x[:, 2]) * (x[:, 3] - x[:, 2]) <= 0.9*0.9) \
                & (21.5 <= x[:, 0]) & (x[:, 0] <= 22) \
                & (21 <= x[:, 1]) & (x[:, 1] <= 21.5) \
                & (21 <= x[:, 2]) & (x[:, 2] <= 22) \
                & (21 <= x[:, 3]) & (x[:, 3] <= 22)
    return inner_box



def cons_unsafe(x):
    inner_box = ((x[:, 3] - x[:, 2]) * (x[:, 3] - x[:, 2]) > 0.95*0.95) \
                & (10 <= x[:, 0]) & (x[:, 0] <= 30) \
                & (10 <= x[:, 1]) & (x[:, 1] <= 30) \
                & (10 <= x[:, 2]) & (x[:, 2] <= 30) \
                & (10 <= x[:, 3]) & (x[:, 3] <= 30)
    return inner_box



def cons_domain(x):
    return x[:, 0] == x[:, 0]  # equivalent to True



############################################
# set the vector field
############################################
# this function accepts a tensor input and returns the vector field of the same size
def vector_field(x, ctrl_nn,ctrl_nn2):
    # the vector of functions
    def f(i, x):
        #######################################################
        # controller is connected with u and x
        #######################################################
        a = x[:,0].view(-1, 1)
        b = x[:,1].view(-1, 1)
        c = x[:,2].view(-1, 1)
        d = x[:,3].view(-1, 1)
        # controller with two inputs
        # controller_input1 = torch.cat((a), dim=1)
        # controller_input2 = torch.cat((b), dim=1)
        # controller_input3 = torch.cat((c), dim=1)
        # controller_input4 = torch.cat((d), dim=1)
        controller_input1 = a
        controller_input2 = b
        controller_input3 = c
        controller_input4 = d
        ######################################################
        # field
        ######################################################
        #  x => i = 1,3, x with hat => i = 2,4
        # fix controller in [0,100], need *0.01
        ######################################################
        if i == 1:
            x_ = (1-2*alpha-ae-ah*0.001*(ctrl_nn(controller_input1))[:, 0])*x[:,0]+ alpha*x[:,2]+ ae*Te + ah*Th*0.001*(ctrl_nn(controller_input1))[:, 0]
            return x_
        elif i == 2:
            x_ = (1-2*alpha-ae-ah*0.001*(ctrl_nn(controller_input2))[:, 0])*x[:,1]+ alpha*x[:,3]+ ae*Te + ah*Th*0.001*(ctrl_nn(controller_input2))[:, 0]
            return x_
        elif i == 3:
            x_ = (1-2*alpha-ae-ah*0.001*(ctrl_nn2(controller_input3))[:, 0])*x[:,2]+ alpha*x[:,0]+ ae*Te + ah*Th*0.001*(ctrl_nn2(controller_input3))[:, 0]
            return x_
        elif i == 4:
            x_ = (1-2*alpha-ae-ah*0.001*(ctrl_nn2(controller_input4))[:, 0])*x[:,3]+ alpha*x[:,1]+ ae*Te + ah*Th*0.001*(ctrl_nn2(controller_input4))[:, 0]
            return x_
        else:
            print("Vector function error!")
            exit()

    vf = torch.stack([f(i + 1, x) for i in range(superp.DIM_S)], dim=1)
    return vf