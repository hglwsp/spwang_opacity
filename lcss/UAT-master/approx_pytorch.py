# Downloading dependencies:
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
import os
import acti


#torch.set_default_tensor_type(torch.DoubleTensor)
#from pygments.console import x

os.environ['KMP_DUPLICATE_LIB_OK']='True'

### Setting function to approximate: *******************   #

# Actual Function here, Relationship: y = x^2

x_data= np.arange(-10,10,0.1)
y_data= np.arange(-10,10,0.1)
s1=np.array(np.meshgrid(x_data,y_data))
b=s1.reshape(-1,order='F')
s1=b.reshape(-1,2)
print(s1)

print(s1[:,0])

x1=s1[:,0]
x2=s1[:,1]
# y= 0.01203*x1**2 + 0.1662*x1*x2 + 0.08012*x1 + 0.1032*x2**2 - 1.47*x2 #+ 0.2*torch.rand(x1.size())
# y =  x1**2 + x2**2 + x1 * x2
y = x1 ** 2 + x2 **2

y=y.reshape(-1,1)
print(y)

# Feel free to change Actual Function whatever u want to try: Ex: y=sin(x)
#x = np.linspace(0,180,200)
#y = np.sin(np.deg2rad(x))


#   ****************************************************   #

### Setting up the feedfoward neural network  **********   #net = nn.double()
# Hyperparamters to tune: Number of Neurons and Hidden Layers, Learning Rate and Epochs.
n_neurons = 10  # number of neurons/nodes
learning_rate = 0.0005 # learning rate

act_fun = acti.my_act()
   
model = nn.Sequential(     
          nn.Linear(2, n_neurons,bias=True),
          act_fun,
          #nn.Linear(n_neurons,n_neurons),
          #nn.ReLU(),        
          nn.Linear(n_neurons,1,bias=True),
          #nn.ReLU()
          )


# Set up  : Input (1 Node) -> Hidden (10 nodes) -> Output (1 Node) 
# Set up 2: Input (1 Node) -> Hidden (10 nodes) -> Hidden (10 nodes) -> Output (1 Node)

# Important Note: If you increase the number of neurons or use a harder function to approximate, try tuning the learning rate.
#                 Tuning the learning rate is vital to properly train the network.

optimizer = optim.RMSprop(model.parameters(), lr=learning_rate) # define optimizer
#optimizer = optim.SGD(model.parameters(), lr=learning_rate)

criterion = nn.MSELoss() # define loss function 5e-3

# ******************************************************  #

### Training: ******************************************  #

# Convert to tensor form with batch for PyTorch model.
inputs = torch.tensor(s1).view(-1,2)

labels = torch.tensor(y).view(-1,1)

# Important Note 2: Change epochs
epochs = 200000

for p in model.parameters():
    nn.init.normal_(p)  # standard Gaussian distribution

for epoch in range(epochs):  # loop over the data multiple times
   
    # zero the parameter gradients
    optimizer.zero_grad()
   
    # forward + backward + optimize
    outputs = model(inputs.double())
    loss = criterion(outputs, labels.double())
    print("peoch:",epoch, "loss:", loss.data)
    loss.backward()
    optimizer.step()
    if loss< 1e-16:
        print("Approximate the polymial successfully!")
        break
    
# ******************************************************  #

### Running Inference over the trained model ***********  #
with torch.no_grad():
    #test_inputs = torch.tensor(s1).view(-1,2).float()
    test_inputs = torch.tensor(s1).view(len(s1), -1).double()
    y_hat = model(test_inputs)
    #y_hat = y_hat.detach().numpy()
    
# ******************************************************  #
torch.save(model.state_dict(), 'pre_trained_ctrl.pt')

def print_nn():
    for p in model.parameters():
        print(p.data)
### Plot results: Actual vs Model Prediction ***********  #


print_nn()
# ******************************************************  #

