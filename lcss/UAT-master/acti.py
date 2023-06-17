import torch
import torch.nn as nn


############################################
# set default data type to double
############################################
torch.set_default_dtype(torch.float64)
torch.set_default_tensor_type(torch.DoubleTensor)
# torch.set_default_dtype(torch.float32)
# torch.set_default_tensor_type(torch.FloatTensor)


############################################
# self-defined activation function
############################################
class my_act(nn.Module):
    def __init__(self):
        super(my_act, self).__init__()
        
    def forward(self, x):
        #x = 0.5 * x + torch.sqrt(0.25 * x * x + superp.BENT_DEG) #bent relu, approximate relu as close as possible for post-verfication
        #x = x + 0.5 * (torch.sqrt(x * x + 1) - 1) #bent identity
        #x = 0.51 * x + torch.sqrt(0.2401 * x * x + superp.BENT_DEG) #bent leakly relu
        #x = 0.5 * x + torch.sqrt(0.16 * x * x + superp.BENT_DEG) #bent leakly relu
        #x = -0.004735975767152627 *pow(x,4)+ -0.10661026206281723 *pow(x,3)+ 0.012550335782954333 *pow(x,2)+ 0.8679167801126567 *x+ -0.003563348167205441
        x = torch.tanh(x)
        #x = 0.002484511740280433 *pow(x,2)+ 0.35602035671435817 *x+ -0.007945468545416763#二次替代
        #x = -0.02549178590895252 * pow(x, 3) + -0.0013392561460622572 * pow(x, 2) + 0.6004610917953047 * x + 0.004282941155107011
        #x = -0.0001711589065517019 *pow(x,4)+ -0.01447711943585072 *pow(x,3)+ 0.002849795794085815 *pow(x,2)+ 0.5071116596907747 *x+ -0.00508383030596129
        #x = 0.0011037890192654714 *pow(x,5)+ 0.00010478834826477135 *pow(x,4) + -0.04508886823681293 * pow(x, 3) + -0.0017447259986083934 * pow(x,2) + 0.6708844053970195 * x + 0.003112465435499514
        #x = 2.0051831663135838e-05 *pow(x,6)+ 0.0011098045687644195 *pow(x,5)+ -0.0005773385070393623 *pow(x,4)+ -0.045225393867032275 *pow(x,3)+ 0.003929047138919935 *pow(x,2)+ 0.6714524654391838 *x+ -0.003631209674748929

        return x