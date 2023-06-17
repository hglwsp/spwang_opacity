import torch
import superp
import prob

############################################
"""
This code is written by spwang!
"""
############################################

############################################
# constraints for barrier certificate B:
# eps = 0.001
# (1) init ==> B <= 0 <==> B <= -eps <==> eps + B <= 0
# (2) unsafe ==> B > 0 <==> B >= eps <==> eps - B <= 0 (positive eps)
# (3) domain ==> B(f(x)) - B(x) <= 0
############################################
# '_1' represent we deal with domain

############################################
# given the training data, compute the loss
############################################
def calc_loss(barr_nn, ctrl_nn,input_init, input_unsafe, input_domain,epoch):
    # compute loss of init
    output_init = barr_nn(input_init)
    loss_init = torch.relu(( output_init)  + 0.01)  # tolerance

    # compute loss of unsafe
    output_unsafe = barr_nn(input_unsafe)
    loss_unsafe1 = torch.relu((- output_unsafe)  + 0.01)
    # output_unsafe_1 = barr_nn(input_unsafe_1)
    # loss_unsafe2 =  torch.relu((- output_unsafe_1)  + 0.001)# tolerance


    # compute loss of B(f(x))-B(x)<=0
    output_x = barr_nn(input_domain)
    f_domain = prob.vector_field(input_domain, ctrl_nn)
    output_fx = barr_nn(f_domain)
    loss_diff1 = torch.relu(output_fx + 0.01)
    # output_x_1 = barr_nn(input_domain_1)
    # f_1_domain = prob.vector_field(input_domain_1, ctrl_nn, ctrl_nn2)
    # output_fx_1 = barr_nn(f_1_domain)
    # loss_diff2 =  torch.relu(output_fx_1 - output_x_1 )




    # compute loss of u   [0,1]
    # a = input_domain[:, 0].view(-1, 1)
    # b = input_domain[:, 1].view(-1, 1)
    # c = input_domain[:, 2].view(-1, 1)
    # d = input_domain[:, 3].view(-1, 1)
    # input_u1 = torch.cat((a), dim=1)
    # input_u2 = torch.cat((b), dim=1)
    # input_u3 = torch.cat((c), dim=1)
    # input_u4 = torch.cat((d), dim=1)
    a = input_domain[:, 0].view(-1, 1)
    b = input_domain[:, 1].view(-1, 1)
    input_u1 = a
    input_u2 = b
    output_u1 = ctrl_nn(input_u1)
    output_u2 = ctrl_nn(input_u2)
    loss_u =0* torch.relu(-(output_u1)) + torch.relu((output_u1) - 1000000000) \
             + 0*torch.relu(-(output_u2)) + torch.relu((output_u2) - 100000000)\




    ##--------------------------------------------------------------------------------------------------------------
    # select boundary points
    # with torch.no_grad():
    #     output_domain = barr_nn(input_domain)
    #     boundary_index = ((output_domain[:, 0] >= -superp.TOL_BOUNDARY) & (
    #                 output_domain[:, 0] <= superp.TOL_BOUNDARY)).nonzero()
    #
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
    unsafe = torch.sum(loss_unsafe1)
    diff = torch.sum(loss_diff1)
    loss_u = 0*torch.sum(loss_u)
    total_loss =         superp.DECAY_INIT * torch.sum(loss_init) \
                         + superp.DECAY_UNSAFE * torch.sum(loss_unsafe1) \
                         + superp.DECAY_DIFF * torch.sum(loss_diff1) \


    #######################################################
    # only for controller
    # loss_u = torch.sum(loss_u)
    # total_loss = torch.sum(loss_u)
    #######################################################

    #######################################################
    # only for controller
    # return loss_u,total_loss
    #######################################################

    #######################################################
    # For barrier
    #######################################################
    # torch.mean() for average
    # return total_loss is a tensor, max_gradient is a scalar
    return init,unsafe,diff,loss_u,total_loss
