from numpy import *

N = 144
W = 8.


folder = 1

if folder==1:
    omegas = [0.1, 1.0]
    betas  = [1.0, 3.0, 5.0, 8.0, 12.0]
    lamb   = 0.5


save('../omegas',omegas)
save('../betas',betas)
save('../lamb', lamb)
save('../N',N)


if folder==1:
    mu_map = load('../mu_map_interpolated_nvsmu_l0p5_12b12.npy')

    
save('../mu_map', mu_map)
print 'done saving mu map'
print shape(mu_map)
