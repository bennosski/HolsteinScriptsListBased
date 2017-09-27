from numpy import *

N = 16
W = 8.


folder = 2

# attempting to get fig 1a in Phys Rev Lett 66, 1990
if folder==2:
    Us     = [4.0]
    betas  = [2.0, 4.0, 6.0, 8.0, 10.0]
    nsampl = 50000
    nequil = 50000
    
save('../betas',betas)
save('../Us', Us)
save('../N',N)
save('../nequil',nequil)
save('../nsampl',nsampl)


if folder==2:
    
    mu_map = load('../mu_map_interpolated_negU_8b8_benchmark.npy')

    #mu_map = []
    #for iu,blist in enumerate(Us):
    #    mu_map.append([])
    #    for ibeta,mulist in enumerate(blist):
    #        mu_map[iu].append(linspace(
    
    
save('../mu_map', mu_map)
print 'done saving mu map'
print shape(mu_map)
