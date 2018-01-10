from numpy import *
import sys

N = 64
W = 8.


folder = int(sys.argv[1])
    
if folder==1:
    omegas = [10.0, 15.0]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.6
    nsampl = 2000
    nequil = 2000
    uneq_meas = False
if folder==2:
    omegas = [10.0, 15.0]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.6
    nsampl = 100000
    nequil = 100000
    uneq_meas = True
if folder==3:
    omegas = [10.0, 15.0]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.55
    nsampl = 2000
    nequil = 2000
    uneq_meas = False
if folder==4:
    omegas = [10.0, 15.0]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.55
    nsampl = 100000
    nequil = 100000
    uneq_meas = True
if folder==5:
    omegas = [10.0, 15.0]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.5
    nsampl = 2000
    nequil = 2000
    uneq_meas = False
if folder==6:
    omegas = [10.0, 15.0]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.5
    nsampl = 100000
    nequil = 100000
    uneq_meas = True
    
try:
    save('../nsampl', nsampl)
    save('../nequil', nequil)
    save('../uneq_meas', uneq_meas)
except:
    print 'nsampl and nequil not defined'

save('../omegas',omegas)
save('../betas',betas)
save('../lamb', lamb)
save('../N',N)

    
if folder%2==1:
    mu_map = []
    for i,omega in enumerate(omegas):
        mu_map.append([])
        for j in range(len(betas)):
            mu_map[i].append([])

            mu_list = linspace(-4.0-lamb*W, -lamb*W, 21)
            for k in range(21):
                mu_map[i][j].append(mu_list[k])


if folder==2:
    mu_map = load('mu_map_interpolated_nvsmu_l0p6_bigOmega.npy')
if folder==4:
    mu_map = load('mu_map_interpolated_nvsmu_l0p55_bigOmega.npy')
if folder==6:
    mu_map = load('mu_map_interpolated_nvsmu_l0p5_bigOmega.npy')

    
save('../mu_map', mu_map)
print 'done saving mu map'
print shape(mu_map)
