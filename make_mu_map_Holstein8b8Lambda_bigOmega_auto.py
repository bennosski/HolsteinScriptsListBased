from numpy import *
import sys


def main(folder, lamb_str):

    N = 64
    W = 8.


    #folder = int(sys.argv[1])
    #lamb_str = sys.argv[2]
    i1 = lamb_str.index('p')
    lamb = float(lamb_str[i1+1:])

    y = raw_input("assert lamb = "+lamb_str)
    if y!='y':
        quit()

    omegas = [10.0, 15.0]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]

    if folder%2==1:
        nsampl = 2000
        nequil = 2000
        uneq_meas = False
    else:
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
    else:
        num = str(lamb)
        i1 = num.index('.')
        num = num[i1+1:]

        myfile = 'mu_map_interpolated_nvsmu_'+lamb_str+'_bigOmega.npy'
        mu_map = load(myfile)


    save('../mu_map', mu_map)
    print 'done saving mu map'
    print shape(mu_map)
