import torch
import superp

############################################
# set the super-rectangle range
############################################
# set the initial in super-rectangle

DIM_S = 4    # barrier need 4-dims,it only connection with x1,x2,x3,x4,without input u
INIT = [[21,22],\
         [21,22],\
            [21.5,22],\
              [21,21.5],\
        ]
INIT_SHAPE = 3  # 4 for top-triangle, 3 for down-triangle, 2 for circle, 1 for rectangle

# the the unsafe in super-rectangle
UNSAFE =  [[0,50] ,\
          [0,50],\
            [0,50],\
                [0,50],\
        ]
UNSAFE_SHAPE = 3  # 2 for circle, 1 for rectangle


# the the domain in super-rectangle
DOMAIN = [[0,50] ,\
          [0,50],\
            [0,50],\
                [0,50],\
        ]
DOMAIN_SHAPE = 1  # 1 for rectangle

#para
alpha = 0.05
Te=-1
ah=0.0036
Th=50
ae=0.008

############################################
# set the range constraints
############################################
# accept a two-dimensional tensor and return a
# tensor of bool with the same number of columns
def cons_init(x):
    # return x[:, 0] == x[:, 0]
    inner_box = ((x[:, 3] - x[:, 2]) * (x[:, 3] - x[:, 2]) <= 1) \
                & (21 <= x[:, 0]) & (x[:, 0] <= 22) \
                & (21 <= x[:, 1]) & (x[:, 1] <= 22) \
                & (21.5 <= x[:, 2]) & (x[:, 2] <= 22) \
                & (21 <= x[:, 3]) & (x[:, 3] <= 21.5)
    return inner_box



def cons_unsafe(x):
    inner_box = ((x[:, 3] - x[:, 2]) * (x[:, 3] - x[:, 2]) > 1*1) \
                & (0 <= x[:, 0]) & (x[:, 0] <= 50) \
                & (0 <= x[:, 1]) & (x[:, 1] <= 50) \
                & (0 <= x[:, 2]) & (x[:, 2] <= 50) \
                & (0 <= x[:, 3]) & (x[:, 3] <= 50)
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
        # x1,x2,x3,x4,u
        #######################################################
        # need generate random u
        #######################################################
        # need a seed
        #######################################################
        a = x[:, 0].view(-1, 1)
        b = x[:, 1].view(-1, 1)
        c = x[:, 2].view(-1, 1)
        d = x[:, 3].view(-1, 1)
        # controller with two inputs
        controller_input1 = torch.cat((a,c),dim = 1)
        controller_input2 = torch.cat((b,d), dim=1)
        ######################################################
        # field
        ######################################################
        #  x => i = 1,3, x with hat => i = 2,4
        ######################################################
        if i == 1:
            # torch.manual_seed(init_seed)
            x_ = (1-2*alpha-ae-ah*(ctrl_nn(controller_input1))[:, 0])*x[:,0]+ alpha*x[:,2]+ ae*Te + ah*Th*(ctrl_nn(controller_input1))[:, 0]
            return x_
        elif i == 2:
            # torch.manual_seed(init_seed)
            x_ = (1-2*alpha-ae-ah*(ctrl_nn(controller_input2))[:, 0])*x[:,1]+ alpha*x[:,3]+ ae*Te + ah*Th*(ctrl_nn(controller_input2))[:, 0]
            return x_
        elif i == 3:
            # torch.manual_seed(init_seed)
            x_ = (1-2*alpha-ae-ah*(ctrl_nn(controller_input1))[:, 0])*x[:,2]+ alpha*x[:,0]+ ae*Te + ah*Th*(ctrl_nn(controller_input1))[:, 0]
            return x_
        elif i == 4:
            # torch.manual_seed(init_seed)
            x_ = (1-2*alpha-ae-ah*(ctrl_nn(controller_input2))[:, 0])*x[:,3]+ alpha*x[:,1]+ ae*Te + ah*Th*(ctrl_nn(controller_input2))[:, 0]
            return x_
        else:
            print("Vector function error!")
            exit()
    vf = torch.stack([f(i + 1, x)[0] for i in range(superp.DIM_S)], dim=1)
    vu = torch.stack([f(i + 1, x)[1] for i in range(superp.DIM_S)], dim=1)
    return vf,vu