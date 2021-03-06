from numpy import *

N = 64
W = 8.


folder = 1

if folder==1:
    omegas = [1.0]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.125    #1/8
    
    
save('../omegas',omegas)
save('../betas',betas)
save('../lamb', lamb)
save('../N',N)


mu_map = []
if folder==1:
    for iomeg in range(len(omegas)):
        mu_map.append([])
        for ibeta in range(len(betas)):
            mu_map[iomeg].append(linspace(-lamb*W-2.5, -lamb*W, 21))

    
save('../mu_map', mu_map)
print 'done saving mu map'
print shape(mu_map)
