import sys, os
from numpy import *
import numpy as np

#input('Did you run make_dens_ogm.py first???')
#dirpath = 'outputfiles2/'
dirpath = sys.argv[1]

N = load('../N.npy')
Nm = sqrt(N)/2+1

folders = os.listdir(dirpath)

dens = load('../results/dens_ogm.npy')
[d1,d2,d3] = shape(dens)

x_ogm     = zeros([Nm,Nm,d1,d2,d3])
x_ogm_std = zeros([Nm,Nm,d1,d2,d3])

betas = load('../betas.npy')


def get_xcdw2(folder, myfiles, beta, N):
     Nk = int(sqrt(N))

     files = []
     for myfile in myfiles:
         if "uneqlt_nn_corr" in myfile:
             files.append(myfile)

     print('len files', len(files))


     xs = []
     for i, myfile in enumerate(files):
          xs.append(fromfile(dirpath+folder+'/'+myfile))
     
     L = len(xs[0])//N

     xs = asarray(xs)
     print(shape(xs))
     print(len(files),L,Nk,Nk)
     xs.shape = (len(files), L, Nk, Nk) 
     
     xq = conj(fft.fft2(xs))
     x   = real(sum(xq[:,:,Nk//2,Nk//2], axis=1)*beta/L)

     return average(x), std(x)
     


def get_xcdw(folder, myfiles, beta, N):
     Nk = int(sqrt(N))

     files = []
     for myfile in myfiles:
         if "uneqlt_nn_corr" in myfile:
             files.append(myfile)

     print('len files', len(files))

     xs = []
     xs = zeros((len(files), Nk, Nk))



     ct = 0
     for myfile in files:

          x = fromfile(dirpath+folder+'/'+myfile)
          L = len(x)//N
          #x = reshape(x, (Nk,Nk,L))
          #print shape(x)

          ct2 = 0
          x_mat = zeros([Nk,Nk,L+1])
          for il in range(L):
              for ik2 in range(Nk):
                  for ik1 in range(Nk):
                      x_mat[ik1,ik2,il] = x[ct2]
                      ct2 += 1

          #x = sum(x_mat, axis=2)*beta/L     

          # add symmetric end point at tau=beta
          x_mat[:,:,L] = x_mat[:,:,0]
                      
          #now do simpson's rule:
          weights = zeros(L+1)
          for i in range(L+1):
               weights[i] = 2.* (i%2 + 1) /3.
          weights[0]  = 1./3
          weights[-1] = 1./3

          x = np.einsum('ijk,k->ij', x_mat, weights) * beta/L
          
          xs[ct,:,:] = x
          ct += 1

     # now do Fourier transform

     cs = xs.copy()
     xs  = average(cs, axis=0)
     mystd = std(cs, axis=0)
     pipi_std = 0.
     
     pipi_x = 0.

     for i1 in range(Nk):
          for i2 in range(Nk):
               k_dot_R = i1*(-pi) + i2*(-pi)
               pipi_x += xs[i1, i2]  * exp(-1j*k_dot_R)
               pipi_std += (xs[i1, i2])**2 * mystd[i1, i2]**2

     '''
     for ik1 in range(Nk):
         for ik2 in range(Nk):
             for i1 in range(Nk):
                 for i2 in range(Nk):
                     k_dot_R = i1*(-pi + 2*pi/Nk*ik1) + i2*(-pi + 2*pi/Nk*ik2)
                     Xmom[ik1, ik2] += xs[i1, i2]  * exp(-1j*k_dot_R)

                     if ik1==0 and ik2==0:
                          pipi_std += (xs[i1, i2]  * exp(-1j*k_dot_R))**2 * mystd[i1, i2]**2
     '''

     return real(pipi_x), real(sqrt(pipi_std))

def get_xcdw_full(folder, myfiles, beta, N):
     Nk = int(sqrt(N))

     files = []
     for myfile in myfiles:
         if "uneqlt_nn_corr" in myfile:
             files.append(myfile)

     print('len files', len(files))

     xs = zeros((len(files), Nk/2+1, Nk/2+1))

     ct = 0
     for myfile in files:

          x = fromfile(dirpath+folder+'/'+myfile)
          L = len(x)//N          
          #x = reshape(x, (Nk,Nk,L))
          #print shape(x)

          ct2 = 0
          x_mat = zeros([Nk,Nk,L+1])
          for il in range(L):
              for ik2 in range(Nk):
                  for ik1 in range(Nk):
                      x_mat[ik1,ik2,il] = x[ct2]
                      ct2 += 1

          #x = sum(x_mat, axis=2)*beta/L     

          # add symmetric end point at tau=beta
          x_mat[:,:,L] = x_mat[:,:,0]
                      
          #now do simpson's rule:
          weights = zeros(L+1)
          for i in range(L+1):
               weights[i] = 2.* (i%2 + 1) /3.
          weights[0]  = 1./3
          weights[-1] = 1./3

          x = np.einsum('ijk,k->ij', x_mat, weights) * beta/L
          
          #xs[ct,:,:] = x
          xs[ct,:,:] = real(fft.fft2(x)[Nk/2::-1,Nk/2::-1])

          ct += 1

     # now do Fourier transform

     return mean(xs, axis=0), std(xs, axis=0)

     '''
     cs = xs.copy()
     xs  = average(cs, axis=0)
     mystd = std(cs, axis=0)
     
     Xmom = zeros([Nk,Nk], dtype=complex)
     Xmom_std = zeros([Nk,Nk], dtype=complex)


     for ik1 in range(Nk/2+1):
         for ik2 in range(Nk/2+1):
             for i1 in range(Nk):
                 for i2 in range(Nk):
                     k_dot_R = i1*(-pi + 2*pi/Nk*ik1) + i2*(-pi + 2*pi/Nk*ik2)
                     Xmom[ik1, ik2] += xs[i1, i2]  * exp(-1j*k_dot_R)
                     #Xmom_std[ik1,ik2] += (xs[i1, i2]  * exp(-1j*k_dot_R))**2 * mystd[i1, i2]**2
                     Xmom_std[ik1,ik2] += xs[i1, i2]**2 * mystd[i1, i2]**2

     print real(Xmom[:Nk/2+1,:Nk/2+1])
     print ' '
     print real(fft.fft2(xs)[Nk/2::-1,Nk/2::-1])
     1/0
      
     return real(Xmom[:Nk/2+1,:Nk/2+1]), real(sqrt(Xmom_std[:Nk/2+1,:Nk/2+1]))
     '''



for folder in folders:

  [i1,i2,i3] = [pos for pos,char in enumerate(folder) if char=='_']

  i = int(folder[i1+1:i2])
  j = int(folder[i2+1:i3])
  k = int(folder[i3+1:])

   
  #if i=='0' and j=='7' and k=='7':
  #  print 'ahh'
  #  continue

  print(folder)
  files = os.listdir(dirpath+folder)
  
  #x, xstd = get_xsc(folder,files, beta, N, dens[i,j,k])
  x, xstd = get_xcdw_full(folder,files,betas[j],N)
  #print 'x, xstd',x,xstd
 
  #x, xstd = get_xcdw2(folder,files,beta,N)
  #print 'x, xstd',x,xstd
  #1./0

  x_ogm[:,:,i,j,k]     = x
  x_ogm_std[:,:,i,j,k] = xstd


print('saving files')
save('../results/xcdw_full_ogm', x_ogm)
save('../results/xcdw_full_ogm_std', x_ogm_std)
