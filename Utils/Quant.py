def sign(x):
  if x == 0: return 0 
  return 1 if x>0 else -1

def Quant(weight, levels = 4):
  dev = weight.device
  D = weight.max().item()/(levels - 1)
  W = weight.clone().detach().cpu() 
  for k in range(levels):
    W.apply_(lambda x: k*D*sign(x) if k < sign(x)*x/D < k+1 else x)

  return W.to(dev)
