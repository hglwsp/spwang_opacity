import torch
import superp

############################################
# set the super-rectangle range
############################################
# set the initial in super-rectangle
pi = 3.14
DIM_S = 4    # barrier need 4-dims,it only connection with x1,x2,x3,x4,without input u
INIT = [[0,6*pi/18] ,\
          [0,6*pi/18],\
            [0,0],\
                [0,0],\
        ]
INIT_SHAPE = 3  # 4 for top-triangle, 3 for down-triangle, 2 for circle, 1 for rectangle

# the the unsafe in super-rectangle
UNSAFE_1 = [[-9*pi/18,pi/2] ,\
          [-9*pi/18,pi/2],\
            [-pi/2,pi/2],\
                [-pi/2,pi/2],\
        ]

UNSAFE_2 = [[-pi/3,pi/3] ,\
          [-pi/3,pi/3],\
            [-pi/2,pi/2],\
                [-pi/2,pi/2],\
        ]
UNSAFE_SHAPE = 3  # 2 for circle, 1 for rectangle


# the the domain in super-rectangle
DOMAIN =  [[-pi/2,pi/2] ,\
          [-pi/2,pi/2],\
            [-pi/2,pi/2],\
                [-pi/2,pi/2],\
        ]
DOMAIN_SHAPE = 1  # 1 for rectangle

############################################
# set the range constraints
############################################
# accept a two-dimensional tensor and return a
# tensor of bool with the same number of columns
def cons_init(x):
    # return x[:, 0] == x[:, 0]
    inner_box = ((x[:,1] - x[:,0]) * (x[:,1] - x[:,0]) <= pi/12 * pi/12)\
                & (0*pi/18 <= x[:, 0]) & (x[:, 0] <= 3*pi/18 ) \
                & (0*pi/18<= x[:, 1]) & (x[:, 1] <= 3*pi/18) \
                & (0 <= x[:, 2]) & (x[:, 2] <= 0) \
                & (0 <= x[:, 3]) & (x[:, 3] <= 0)
    return inner_box



def cons_unsafe(x):
    inner_box = ((x[:,1] - x[:,0]) * (x[:,1] - x[:,0]) > pi/3 * pi/3) \
              & (-pi/2  <= x[:,0]) &  (x[:,0]<=pi/2) \
              & (-pi/2 <= x[:,1] ) & (x[:,1]<= pi/2)\
              & (-pi/2 <= x[:,2]) & (x[:,2] <= pi/2)\
               & (-pi/2 <= x[:,3]) & (x[:,3] <= pi/2)
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
        l = len(a)
        # init_seed = 0
        # torch.manual_seed(init_seed)
        # u = (torch.rand(l) * 10 - 5)/100.0
        u = torch.linspace(-0.02,0.02,l)
        e = u.view(-1,1)
        controller_input_1 = torch.cat((a,c),dim = 1)
        controller_input_2 = torch.cat((-b,-d), dim=1)
        ######################################################
        # field
        ######################################################
        g = 9.8
        if i == 3:
            # torch.manual_seed(init_seed)
            x_ = g * (x[:,0] - x[:,0]*x[:,0]*x[:,0]/6) + 1/u + x[:,2]
            return x_ , u # x[:, 1] stands for x2
        elif i == 1:
            # torch.manual_seed(init_seed)
            x_ = x[:, 0] + x[:, 2]
            return x_, u
            # x[:, 0] stands for x1
        elif i == 4:
            # torch.manual_seed(init_seed)
            # x_ = x[:, 3] +  (ctrl_nn(controller_input))[:, 0]
            # x_ = x[:,3] + 0.8*x[:,0] - 0.8*x[:,1] + 1.5*x[:,2] - 1.5*x[:,3] + u
            x_ = g * (x[:,1] - x[:,1]*x[:,1]*x[:,1]/6) + 1/( (ctrl_nn(controller_input_1))[:, 0] + u + (ctrl_nn(controller_input_2))[:, 0]) +  x[:,3]
            return x_,u# x[:, 1] stands for x4
        elif i == 2:
            # torch.manual_seed(init_seed)
            # x_ = x[:, 1] + x[:, 3]+  0.5*(ctrl_nn(controller_input))[:, 0]
            # x_ = x[:,1] + x[:,3] + 0.5*(0.8*x[:,0] - 0.8*x[:,1] + 1.5*x[:,2] - 1.5*x[:,3] + u)
            x_ = x[:,1] + x[:,3]
            return x_,u
            # x[:, 0] stands for x3
        else:
            print("Vector function error!")
            exit()
    vf = torch.stack([f(i + 1, x)[0] for i in range(superp.DIM_S)], dim=1)
    vu = torch.stack([f(i + 1, x)[1] for i in range(superp.DIM_S)], dim=1)
    return vf,vu