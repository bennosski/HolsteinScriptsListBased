from numpy import *

N = 64
W = 8.


folder = 3

if folder==1:
    omegas = [0.4, 1.2, 2.0, 2.8, 3.6]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.2

if folder==2:
    omegas = [0.4, 1.2, 2.0, 2.8, 3.6]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.1
   
if folder==3: #outputfiles_l0p2
    omegas = [0.4, 1.2, 2.0, 2.8, 3.6]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.2



save('../omegas',omegas)
save('../betas',betas)
save('../lamb', lamb)
save('../N',N)


mu_map = []
if folder==1 or folder==2:
    for iomeg,omeg in enumerate(omegas):
        mu_map.append([])
        for ibeta,beta in enumerate(betas):
            mu_map[iomeg].append([])
            for imu,mu in enumerate(linspace(-lamb*W-5, -lamb*W, 21)):
                mu_map[iomeg][ibeta].append(mu)

if folder==3:
    mu_map = load('mu_map_interpolatedl0p2_nvsmu.npy')

   
save('../mu_map', mu_map)
print 'done saving mu map'
print shape(mu_map)


for iomeg,blist in enumerate(mu_map):
    for ibeta,mulist in enumerate(blist):
        for imu,mu in enumerate(mulist):
            print iomeg,ibeta,imu,mu
