import torch
import superp
import annc

############################################
"""
This code is written by spwang, which is for printing net parameters!
"""
############################################
def print_nn_matlab(model):
    layer = 0
    for p in model.parameters():
        layer = layer + 1
        arr = p.detach().numpy()
        if arr.ndim == 2:
            print("w" + str((layer + 1) // 2) + " = [", end="")
            print('],[ '.join([', '.join(str(curr_int) for curr_int in curr_arr) for curr_arr in arr]), end="];\n")
        elif arr.ndim == 1:
            print("b" + str(layer // 2) + " = [", end="")
            if layer == 2:
                print(', '.join(str(i) for i in arr), end="]';\n")
            else:
                print(', '.join(str(i) for i in arr), end="];\n")
        else:
            print("Transform error!")

ctrl_nn = annc.gen_nn(superp.N_H_C, superp.D_H_C, superp.DIM_C, 1, superp.CTRL_ACT, superp.CTRL_OUT_BOUND) # generate the nn model for the controller
ctrl_nn2 = annc.gen_nn(superp.N_H_C, superp.D_H_C, superp.DIM_C, 1, superp.CTRL_ACT, superp.CTRL_OUT_BOUND)
ctrl_nn.load_state_dict(torch.load('pre_trained_ctrl.pt'), strict=True)
ctrl_nn2.load_state_dict(torch.load('pre_trained_ctrl2.pt'), strict=True)

print_nn_matlab(ctrl_nn)
print_nn_matlab(ctrl_nn2)