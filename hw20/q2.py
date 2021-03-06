import torch
import torch.nn as nn
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import torch.optim as optim
from torch.autograd import Variable
import matplotlib.pyplot as plt
import numpy as np
print(torch.cuda.is_available())
use_cuda = True
input_size = 28*28
classes = 10
epochs = 10
batch_size = 100
lr = 1e-2
train_dataset = dsets.MNIST(root='./data',train=True,transform=transforms.ToTensor(),download=True)
test_dataset = dsets.MNIST(root='./data',train=False,transform=transforms.ToTensor())
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,batch_size=batch_size,shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset,batch_size=batch_size,shuffle=False)
class Autoencoder(nn.Module):
  def __init__(self,no_of_weights):
    super(Autoencoder,self).__init__()

    self.encoder = nn.Sequential(
        nn.Linear(28*28, 256),
        nn.ReLU(True),
        nn.Linear(256, no_of_weights),
        nn.ReLU(True)
    )
    self.decoder = nn.Sequential(
        nn.Linear(no_of_weights, 256),
        nn.ReLU(True),
        nn.Linear(256, 28*28),
        nn.ReLU(True)
    )

  def forward(self, x):
    out = self.encoder(x)
    out = self.decoder(out)
    return out
def training_AE(epochs, no_of_weights, train_loader, optimisation = 'adam', lr = 0.01):
  ae = Autoencoder(no_of_weights)
  if use_cuda and torch.cuda.is_available():
    ae.cuda()
  
  criterion = nn.MSELoss()
  
  if optimisation == 'adam':
    optimizer = optim.Adam(ae.parameters(), lr)
  elif optimisation == 'SGDmom':
    optimizer = optim.SGD(ae.parameters(), lr, nesterov = True, dampening = 0, momentum=0.01)
  elif optimisation == 'SGD':
    optimizer = optim.SGD(ae.parameters(), lr)
  elif optimisation == 'RMS':
    optimizer = optim.RMSprop(ae.parameters(), lr)
  
  losses = []
  for epoch in range(epochs):
    running_loss,cnt = 0.0,0
    for i, (images, labels) in enumerate(train_loader):
      images = Variable(images.view(images.size(0),-1))
      labels = Variable(labels)
      
      if use_cuda and torch.cuda.is_available():
        images = images.cuda()
        labels = labels.cuda()

      optimizer.zero_grad()
      outputs = ae(images)
      loss = criterion(outputs, images)
      loss.backward()
      optimizer.step()
      running_loss += loss.item()
      cnt+=1
    epoch_loss = running_loss/cnt
    print('Epoch [%d/%d], Loss = %.5f'%(epoch+1,epochs,epoch_loss))
    losses.append(epoch_loss)
  
  return losses[-1]
weights = range(4,60,4)
optimizers = ['adam', 'SGDmom', 'SGD', 'RMS']
losses_ae = np.zeros((4,len(weights)))
i = 0
for optimizer in optimizers:
  error = []
  for weight in weights:
    err = training_AE(epochs, weight, train_loader, optimizer)
    error.append(err)
  losses_ae[i,:] = error
  i+=1
tmp = 141
fig = plt.figure(figsize = [16,8], dpi = 80)
for k in range(len(optimizers)):
  plt.subplot(tmp)
  plt.title("Optimizer :" + str(optimizers[k]))
  plt.plot(weights,losses_ae[k,:])
  tmp+=1
fig.tight_layout()
plt.show()
