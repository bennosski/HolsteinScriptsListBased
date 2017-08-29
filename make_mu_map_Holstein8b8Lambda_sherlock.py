from numpy import *

N = 64
W = 8.


folder = 1

if folder==1:
    omegas = [0.4,1.2,2.0]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.4
if folder==2:
    omegas = [0.4,1.2,2.0]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.5
if folder==3:
    omegas = [0.4,1.2,2.0]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.3
if folder==4:
    omegas = [0.4,1.2,2.0]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.6
    
    
save('../omegas',omegas)
save('../betas',betas)
save('../lamb', lamb)
save('../N',N)


if folder==1:
    mu_map = load('../mu_map_interpolated_fill_l0p4_8b8.npy')
if folder==2:
    mu_map = load('../mu_map_interpolated_fill_l0p5_8b8.npy')
if folder==3:
    mu_map = load('../mu_map_interpolated_fill_l0p3_8b8.npy')
if folder==4:
    mu_map = load('../mu_map_interpolated_fill_l0p6_8b8.npy')

    
save('../mu_map', mu_map)
print 'done saving mu map'
print shape(mu_map)
