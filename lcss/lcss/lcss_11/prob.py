import torch
import superp

############################################
# set the super-rectangle range
############################################
# set the initial in super-rectangle

DIM_S = 4    # barrier need 4-dims,it only connection with x1,x2,x3,x4,without input u
INIT = [[0,0.15] ,\
          [0.15,1],\
            [0,2],\
                [0,2],\
[0,2],
[0,2]
        ]
INIT_SHAPE = 3  # 4 for top-triangle, 3 for down-triangle, 2 for circle, 1 for rectangle

# the the unsafe in super-rectangle
UNSAFE = [[0,2] ,\
          [0,2],\
            [0,2],\
                [0,2],\
[0,2],
[0,2]
        ]
UNSAFE_SHAPE = 3  # 2 for circle, 1 for rectangle


# the the domain in super-rectangle
DOMAIN = [[0,2] ,\
          [0,2],\
            [0,2],\
                [0,2],\
                  [0,2],
                   [0,2]
        ]
DOMAIN_SHAPE = 1  # 1 for rectangle

############################################
# set the range constraints
############################################
# accept a two-dimensional tensor and return a
# tensor of bool with the same number of columns
def cons_init(x):
    # return x[:, 0] == x[:, 0]
    inner_box = (x[:,1] - x[:,0] <= 0.8*0.8 ) \
                &( 0 <= x[:,0] )& (x[:,0] <= 0.15)\
                & (0.15 <= x[:,1]) & (x[:,1] <= 1 ) \
                & (0 <= x[:, 2]) & (x[:, 2] <= 2) \
                & (0 <= x[:, 3]) & (x[:, 3] <= 2) \
                & (0 <= x[:, 4]) & (x[:, 4] <= 2) \
                & (0 <= x[:, 5]) & (x[:, 5] <= 2)
    return inner_box



def cons_unsafe(x):
    inner_box = ((x[:,1] - x[:,0]) * (x[:,1] - x[:,0]) > 0.9*0.9) \
                & (0 <= x[:, 0]) & (x[:, 0] <= 2) \
                & (0 <= x[:, 1]) & (x[:, 1] <= 2) \
                & (0 <= x[:, 2]) & (x[:, 2] <= 2) \
                & (0 <= x[:, 3]) & (x[:, 3] <= 2) \
                & (0 <= x[:, 4]) & (x[:, 4] <= 2) \
                & (0 <= x[:, 5]) & (x[:, 5] <= 2)
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
        p = x[:, 4].view(-1, 1)
        q = x[:, 5].view(-1, 1)
        l = len(a)
        # init_seed = 0
        # torch.manual_seed(init_seed)
        # u = (torch.rand(l) * 10 - 5)/100.0
        u = torch.linspace(-0.5,0.5,l)
        e = u.view(-1,1)
        controller_input = torch.cat((a,b,c,d,p,q,e),dim = 1)
        ######################################################
        # field
        ######################################################
        if i == 3:
            # torch.manual_seed(init_seed)
            x_ = x[:, 2] - x[:,4]
            return x_ , u # x[:, 1] stands for x11
        elif i == 1:
            # torch.manual_seed(init_seed)
            x_ = x[:, 0] - x[:, 2]+  0.005*u
            return x_, u
            # x[:, 0] stands for x1
        elif i == 5:
            # torch.manual_seed(init_seed)
            x_ = -x[:, 0] - 2*x[:, 2]+  0.01*u + 0.005*x[:,0]*x[:,0]*x[:,0]
            return x_, u
            # x[:, 0] stands for x111
        elif i == 4:
            # torch.manual_seed(init_seed)
            x_ = x[:, 3] - x[:,5]
            return x_,u# x[:, 1] stands for x22
        elif i == 2:
            # torch.manual_seed(init_seed)
            x_ = x[:, 1] - x[:, 3]+  0.005*(ctrl_nn(controller_input))[:, 0]
            return x_,u
            # x[:, 0] stands for x2
        elif i == 6:
            # torch.manual_seed(init_seed)
            x_ = -x[:, 1] - 2*x[:, 3]+  0.01*(ctrl_nn(controller_input))[:, 0] + 0.005*x[:,1]*x[:,1]*x[:,1]
            return x_, u
            # x[:, 0] stands for x222
        else:
            print("Vector function error!")
            exit()
    vf = torch.stack([f(i + 1, x)[0] for i in range(superp.DIM_S)], dim=1)
    vu = torch.stack([f(i + 1, x)[1] for i in range(superp.DIM_S)], dim=1)
    return vf,vu