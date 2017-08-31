from numpy import *

N = 64
W = 8.


folder = 5

# new set of omegas
if folder==5:
    omegas = [2.8, 3.6]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.3


    
save('../omegas',omegas)
save('../betas',betas)
save('../lamb', lamb)
save('../N',N)


if folder==5:
    mu_map = load('../mu_map_interpolated_nvsmu_l0p3_8b8.npy')
    
    
save('../mu_map', mu_map)
print 'done saving mu map'
print shape(mu_map)
