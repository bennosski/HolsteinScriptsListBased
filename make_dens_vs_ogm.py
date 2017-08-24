import sys, os
from numpy import *

#folder = sys.argv[1]

#dirpath = load('dirpath_output.npy')
#dirpath = 'outputfiles2/'

dirpath = sys.argv[1]
folders = os.listdir(dirpath)

omegas = load('../omegas.npy')
save('../results/omegas.npy', omegas)

betas = load('../betas.npy')
save('../results/betas.npy', betas)

mu_map = load('../mu_map.npy')
save('../results/mu_map.npy', mu_map)
print shape(mu_map)


dens_ogm = zeros(shape(mu_map))
dens_ogm_std = zeros(shape(mu_map))

for folder in folders:

  [i1,i2,i3] = [pos for pos,char in enumerate(folder) if char=='_']

  i = int(folder[i1+1:i2])
  j = int(folder[i2+1:i3])
  k = int(folder[i3+1:])

  files = os.listdir(dirpath+folder)

  dens = []
  #print i,j,k

  #if i=='0' and j=='7' and k=='7':
  #  print 'ahh'
  #  continue
  
  for myfile in files:

      if '.log' in myfile:
         with open(dirpath+folder+'/'+myfile,'r') as f:
            
            filestr = f.read()
            index = filestr.find('total density')
            index2 = filestr.find('\n',index+15)
            #dens.append(float(filestr[index+15:index+23]))
            
            try:
              d = float(filestr[index+15:index2])
              if not isnan(d):
                dens.append(d)
            except:
              pass
              #print 'error ',i,j,k
              #print filestr
              #print myfile


  dens = asarray(dens)
  if len(dens)<5:
    print i,j,k," warning len(dens) ",len(dens)

  dens_ogm[i,j,k]     = mean(dens)
  dens_ogm_std[i,j,k] = std(dens)


print 'saving files'
save('../results/dens_ogm', dens_ogm)
save('../results/dens_ogm_std', dens_ogm_std)
