import torch
import ann
import data
import train
import time
import redlog
import plot # comment this line if matplotlib, mayavi, or PyQt5 was not successfully installed
import superp

barr_nn = ann.gen_nn(superp.N_H_B, superp.D_H_B, superp.DIM_S, 1, superp.BARR_ACT, superp.BARR_OUT_BOUND)
barr_nn.load_state_dict(torch.load('pre_trained_barr.pt'), strict=True)
output_init = barr_nn([[0,1,0,0]])
print(output_init)