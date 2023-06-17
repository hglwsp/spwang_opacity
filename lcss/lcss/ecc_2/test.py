import numpy as np
import torch
import math
import numpy
import torch

i=0
while i < 5:
    torch.manual_seed(i)
    u=torch.rand(1,2)
    print(u)
    torch.manual_seed(i)
    b=torch.rand(1,2)
    print(b)
    i+=1
    seed = np.random.randint(1, 10000000)
    print(seed)

