from numpy import *

N = 64
W = 8.


folder = 8

# new set of omegas
if folder==5:
    omegas = [2.8, 3.6]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.3
if folder==6:
    omegas = [2.8, 3.6]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.4
if folder==7:
    omegas = [2.8, 3.6]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.5
if folder==8:
    omegas = [2.8, 3.6]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.6


    
save('../omegas',omegas)
save('../betas',betas)
save('../lamb', lamb)
save('../N',N)


if folder==5:
    mu_map = load('../mu_map_interpolated_nvsmu_l0p3_8b8.npy')
if folder==6:
    mu_map = load('../mu_map_interpolated_nvsmu_l0p4_8b8.npy')
if folder==7:
    mu_map = load('../mu_map_interpolated_nvsmu_l0p5_8b8.npy')
if folder==8:
    mu_map = load('../mu_map_interpolated_nvsmu_l0p6_8b8.npy')
    
    
save('../mu_map', mu_map)
print 'done saving mu map'
print shape(mu_map)
