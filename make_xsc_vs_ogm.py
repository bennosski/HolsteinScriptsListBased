import sys, os
from numpy import *


#raw_input('Did you run make_dens_ogm.py first???')
#dirpath = 'outputfiles_w4p0_l0p2/'

dirpath  = sys.argv[1]

folders = os.listdir(dirpath)

dens = load('../results/dens_ogm.npy')
betas = load('../betas.npy')

x_ogm     = zeros(shape(dens))
x_ogm_std = zeros(shape(dens))

N = load('../N.npy')

def get_xsc(folder, myfiles, beta, N, density):
     files = []
     for myfile in myfiles:
         if "uneqlt_sc_c_sw" in myfile:
             files.append(myfile)

     ct = 0
     xtaus  = []
     
     # no need to divide by N because it is already in signfac in the DQMC code!!!
     for myfile in files:
          x = fromfile(dirpath+folder+'/'+myfile)
          L = len(x)/N          
                               
          xtau = zeros(L)
          for l in range(L):
               xtau[l] = sum(x[l*N:l*N+N]) * beta/L
          
          xtaus.append(xtau)

     if xtaus == []:
          print 'missing data'
          return 0,0          
          
     xtaus = asarray(xtaus)
     xtau_avg = mean(xtaus, axis=0)

     
     assert len(xtau_avg) == L
     
     xbeta = xtau_avg[0] - (1.0-density)*beta/L
     xtau_avg = concatenate((xtau_avg, [xbeta]))
 
     #regular integration
     '''
     weights = ones(len(xtau_avg))
     xsc = sum(weights[:-1] * xtau_avg[:-1])
     '''

     #now do simpson's rule:
     weights = zeros(len(xtau_avg))
     for i in range(len(xtau_avg)):
         weights[i] = 2.* (i%2 + 1) /3.
     weights[0]  = 1./3
     weights[-1] = 1./3
     xsc = sum(weights * xtau_avg)
     
     xsc_std = std(sum(xtaus, axis=1), ddof=1)/sqrt(shape(xtaus)[0])  #std error
    
     return xsc, xsc_std

def get_xsc_phil(folder, myfiles, beta, N, density):
     files = []
     for myfile in myfiles:
         if "uneqlt_sc_c_sw" in myfile:
             files.append(myfile)

     ct = 0
     xtaus  = []
     
     # no need to divide by N because it is already in signfac in the DQMC code!!!
     for myfile in files:
          x = fromfile(dirpath+folder+'/'+myfile)
          L = len(x)/N          
                               
          xtau = zeros(L)
          for l in range(L):
               xtau[l] = sum(x[l*N:l*N+N]) * beta/L
          
          xtaus.append(xtau)

     xtaus = asarray(xtaus)
     xtau_avg = mean(xtaus, axis=0)


     return xtau_avg

     '''
     xbeta = xtau_avg[0] - (1.0-density)*beta/L
     xtau_avg = concatenate((xtau_avg, [xbeta]))
 
     #regular integration
     '''
     #weights = ones(len(xtau_avg))
     #xsc = sum(weights[:-1] * xtau_avg[:-1])
     '''

     #now do simpson's rule:
     weights = zeros(len(xtau_avg))
     for i in range(len(xtau_avg)):
         weights[i] = 2.* (i%2 + 1) /3.
     weights[0]  = 1./3
     weights[-1] = 1./3
     xsc = sum(weights * xtau_avg)
     
     xsc_std = std(sum(xtaus, axis=1), ddof=1)/sqrt(shape(xtaus)[0])  #std error
    
     return xsc, xsc_std
     '''



for folder in folders:

  [i1,i2,i3] = [pos for pos,char in enumerate(folder) if char=='_']

  i = int(folder[i1+1:i2])
  j = int(folder[i2+1:i3])
  k = int(folder[i3+1:])

  #print i,j,k


  #if i=='0' and j=='7' and k=='7':
  #  print 'ahh'
  #  continue

  print folder
  files = os.listdir(dirpath+folder)

  '''
  for myfile in files:
    if ".log" in myfile:
      with open(folders[0]+myfile, 'r') as f:
        for line in f:
          if "lattice dimension:" in line:
            index1 = line.index(":")+1
            index2 = line.index("x")
            Nk = int(float(line[index1:index2]))
            N = Nk**2
          if "beta:" in line:
            index1 = line.index(":")+1
            beta = float(line[index1:])
            break
      break
  '''



  #print shape(betas)
  #print shape(dens)
  

  x, xstd = get_xsc(folder,files, betas[j], N, dens[i,j,k])
  
  x_ogm[i,j,k]     = x
  x_ogm_std[i,j,k] = xstd


print 'saving files'
save('../results/x_ogm', x_ogm)
save('../results/x_ogm_std', x_ogm_std)

#vertex_ogm = load('vertex_ogm.npy')
#print 'rel difference',(x_ogm - vertex_ogm[:,:,:,0])/(x_ogm + vertex_ogm[:,:,:,0])
