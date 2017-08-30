import sys, os
from numpy import *

#folder = sys.argv[1]
#dirpath = load('dirpath_output.npy')
#dirpath = 'outputfiles2/'
      
dirpath = sys.argv[1]
folders = os.listdir(dirpath)

if not os.path.exists('../results'):
  os.makedirs('../results')

omegas = load('../omegas.npy')
save('../results/omegas.npy', omegas)

betas = load('../betas.npy')
save('../results/betas.npy', betas)

mu_map = load('../mu_map.npy')
save('../results/mu_map.npy', mu_map)
print shape(mu_map)

dens_ogm = []
dens_ogm_std = []

for i,blist in enumerate(mu_map):
  dens_ogm.append([])
  dens_ogm_std.append([])
  for j,mulist in enumerate(blist):
    dens_ogm[i].append([])
    dens_ogm_std[i].append([])
    for k,mu in enumerate(mulist):

      folder = 'output_%d'%i+'_%d'%j+'_%d'%k

      files = os.listdir(dirpath+folder)

      dens = []
 
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
              
      if len(dens)<5:
        print i,j,k," warning len(dens) ",len(dens)

      if len(dens)==0: 
        dens = [0]

      #print mean(dens), std(dens)
  
      dens_ogm[i][j].append(mean(dens))
      dens_ogm_std[i][j].append(std(dens))

#print 'saving files'
#save('../results/dens_ogm', dens_ogm)
#save('../results/dens_ogm_std', dens_ogm_std)

print 'saving files'

save('../results/dens_ogm', dens_ogm)
save('../results/dens_ogm_std', dens_ogm_std)


