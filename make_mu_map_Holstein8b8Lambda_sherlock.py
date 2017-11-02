from numpy import *

N = 64
W = 8.


folder = 7

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


if folder==5:
    omegas = [2.8, 3.6]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.5
if folder==6:
    omegas = [2.8, 3.6]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.6

if folder==7:
    omegas = [6.8]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.1
if folder==8:
    omegas = [6.8]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.2
if folder==9:
    omegas = [6.8]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.3
if folder==10:
    omegas = [6.8]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.4
if folder==11:
    omegas = [6.8]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.5
if folder==12:
    omegas = [6.8]
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
    
if folder==5:
    mu_map = load('../mu_map_interpolated_l0p5_8b8_omega2p83p6.npy')
if folder==6:
    mu_map = load('../mu_map_interpolated_l0p6_8b8_omega2p83p6.npy')

    
if folder==7 or folder==8 or folder==9 or folder==10 or folder==11 or folder==12:
    mu_map = []
    for i,omega in enumerate(omegas):
        mu_map.append([])
        for j in range(len(betas)):
            mu_map[i].append(j)

            mu_list = linspace(-4.0-lamb*W, -lamb*W, 21)
            for k in range(21):
                mu_map[i][j].append(mu_list[k])

    
save('../mu_map', mu_map)
print 'done saving mu map'
print shape(mu_map)
