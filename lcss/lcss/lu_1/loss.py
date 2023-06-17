import torch
import torch.nn as nn
import superp
import sympy
import prob
import numpy as np
############################################
# constraints for barrier certificate B:
# eps = 0.001
# (1) init ==> B <= 1 <==> B <= -eps <==> eps + B <= 0
# (2) unsafe ==> B > 0 <==> B >= eps <==> eps - B <= 0 (positive eps)
# (3) domain ==> lie <= 0  (lie + lambda * barrier <= 0, where lambda >= 0)
# (4) domain /\ B = 0 ==> lie < 0 (alternatively)
# (5) goal  0 < B < 1
############################################


############################################
# given the training data, compute the loss
############################################
def calc_loss(barr_nn, ctrl_nn, input_init, input_unsafe,input_domain, input_goal,epoch):
    # compute loss of init
    output_init = barr_nn(input_init)
    loss_init = torch.relu(( output_init) - 1 + 0.001) +  torch.relu(( -output_init)  + 0.001) # tolerance

    # compute loss of unsafe1
    output_unsafe = barr_nn(input_unsafe)
    loss_unsafe = torch.relu((- output_unsafe) + 1.001 + 0.001)  # tolerance

    output_goal = barr_nn(input_goal)
    loss_goal = torch.relu(( output_goal) + 0.001)  # tolerance
    # compute loss of unsafe1
    # output_unsafe2 = barr_nn(input_unsafe2)
    # loss_unsafe_2 = torch.relu((- output_unsafe2) + 1.001  + 0.01)  # tolerance

    # compute loss of B(f(x))-B(x)<=0
    output_x = barr_nn(input_domain)
    f_domain = prob.vector_field(input_domain, ctrl_nn)
    # f_00 = f_domain[:,0]
    # f_01 = f_domain[:,1]
    # f_02 = f_domain[:,2]
    # f_03 = f_domain[:,3]
    # # above are f
    # f11 = torch.where(f_00 > 10.0, 10.0, f_00)
    # f1 = torch.where(-f11 > 0.0, 0.0, f11)
    # f22 = torch.where(f_01 > 10.0, 10.0, f_01)
    # f2 = torch.where(-f22 > 0.0, 0.0, f22)
    # f33 = torch.where(f_02 > 0.1, 0.1, f_02)
    # f3 = torch.where(-f33 > 0.0, 0.0, f33)
    # f44 = torch.where(f_03 > 0.1, 0.1, f_03)
    # f4 = torch.where(-f44 > 0.0, 0.0, f44)
    # f_1 = f1.view(-1, 1)
    # f_2 = f2.view(-1, 1)
    # f_3 = f3.view(-1, 1)
    # f_4 = f4.view(-1, 1)
    # input_f = torch.cat((f_1, f_2, f_3, f_4), dim=1)

    output_fx = barr_nn(f_domain)
    loss_diff = torch.relu(output_fx - output_x - 0.01)



    # compute loss of u   [-0.05,0.05]
    a = input_domain[:, 0].view(-1, 1)
    b = input_domain[:, 1].view(-1, 1)
    c = input_domain[:, 2].view(-1, 1)
    # d = input_domain[:, 3].view(-1, 1)
    # e1 = e[:,0].view(-1, 1)
    input_u = torch.cat((a,b,c), dim=1)
    output_u = ctrl_nn(input_u)
    loss_u = torch.relu(-(output_u) - 1000000000) + torch.relu((output_u) - 10000000)


    ##--------------------------------------------------------------------------------------------------------------
    # select boundary points
    # with torch.no_grad():
    #     output_domain = barr_nn(input_domain)
    #     boundary_index = ((output_domain[:, 0] >= -superp.TOL_BOUNDARY) & (
    #                 output_domain[:, 0] <= superp.TOL_BOUNDARY)).nonzero()
    #     input_boundary = torch.index_select(input_domain, 0, boundary_index[:, 0])
    #
    # if len(input_boundary) > 0 and superp.DECAY_LIE > 0:
    #     # compute the gradient of nn on boundary
    #     input_boundary.requires_grad = True  # temporarily enable gradient
    #     output_boundary = barr_nn(input_boundary)
    #     gradient_boundary = torch.autograd.grad(
    #         torch.sum(output_boundary),
    #         input_boundary,
    #         grad_outputs=None,
    #         create_graph=True,
    #         only_inputs=True,
    #         allow_unused=True)[0]
    #     input_boundary.requires_grad = False  # temporarily disable gradient
    #
    #     # compute the maximum gradient norm on boundary
    #     with torch.no_grad():
    #         norm_gradient_boundary = torch.norm(gradient_boundary, dim=1)
    #         max_gradient = (torch.max(
    #             norm_gradient_boundary)).item()  # computing max norm of gradient for controlling boundary sampling
    #
    # else:
    #     max_gradient = 0.0



    ##-----------------------------------------------------------------------------------------------------
    # compute total loss
    init = torch.sum(loss_init)
    unsafe = torch.sum(loss_unsafe)
    diff = torch.sum(loss_diff)
    goal = torch.sum(loss_goal)
    u = torch.sum(loss_u)

    total_loss = superp.DECAY_INIT * init \
                 + superp.DECAY_UNSAFE * unsafe \
                 + superp.DECAY_DIFF * diff\
    +goal
    + superp.DECAY_U * u\


    # torch.mean() for average
    # return total_loss is a tensor, max_gradient is a scalar
    return init,unsafe,diff,u,goal,total_loss
        # , max_gradient
