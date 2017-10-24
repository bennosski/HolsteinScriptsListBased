from numpy import *



folder = 4

# attempting to get fig 1a in Phys Rev Lett 66, 1990
if folder==2 or folder==3:
    N = 16
    W = 8.
    Us     = [4.0]
    betas  = [2.0, 4.0, 6.0, 8.0, 10.0]
    nsampl = 50000
    nequil = 50000


# for quick dens vs mu run for lambdas = 0.6
if folder==4:
    N = 64
    W = 8.
    Us = [0.8, 1.6, 2.4, 3.2, 4., 4.8]
    betas = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    nsampl = 2000
    nequil = 2000

    
save('../betas',betas)
save('../Us', Us)
save('../N',N)
save('../nequil',nequil)
save('../nsampl',nsampl)


if folder==2:
    mu_map = load('../mu_map_interpolated_negU_8b8_benchmark.npy')

if folder==3 or folder==4:
    mu_map = []
    for iu in range(len(Us)):
        mu_map.append([])
        for ibeta in range(len(betas)):
            mu_map[iu].append(linspace(-4.0, 0.0, 21))
    
    
save('../mu_map', mu_map)
print 'done saving mu map'
print shape(mu_map)
