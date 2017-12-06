from numpy import *
import os

def get_color(i,N):
    i = N-1-i
    r = 1.-1.*i/N
    c1 = 1. - 0.8*(exp(4.*r)-1.)/exp(4.)
    c2 = 0.2 + 0.7*(exp((1.-r)/1.*4.)-1.)/exp(4.)
    c3 = exp(-27.*(r-0.76)**2)
    return [c1,c2,c3]

def get_lin_interp_factors(i,j,density, mydens):
    c = 0
    d = mydens[i][j][c]
    while d<density and c<len(mydens[i][j])-1:
        c+=1
        d = mydens[i][j][c]
        
    if c==0:
        print "low density"
        c = 1
        
    d0 = mydens[i][j][c-1]
    d1 = mydens[i][j][c]
    
    if density<d0:
        pass
        #print 'warning extrapolating for omega ',i,' beta ',j
        
    #print 'd0,d1',d0,d1

    return (density-d1)/(d0-d1), (density-d0)/(d1-d0), c

def interp_z(z, i, j, desired_fill, mydens):
    a,b,c = get_lin_interp_factors(i,j,desired_fill, mydens)
    out = z[i][j][c-1]*a + z[i][j][c]*b     
    return out

def loadData(folder, xcdw_order='kkobm', xcdw_flip='y'):
    omegas    = load(folder+'omegas.npy')
    betas     = load(folder+'betas.npy')
    Ts        = 1./betas
    dens      = load(folder+'dens_ogm.npy')
    dens_std  = load(folder+'dens_ogm_std.npy')
    mu_map    = load(folder+'mu_map.npy')
    
    try:
        x         = load(folder+'x_ogm.npy')
        x_std     = load(folder+'x_ogm_std.npy')
        xcdw      = load(folder+'xcdw_full_ogm.npy')
        xcdw_std  = load(folder+'xcdw_full_ogm_std.npy')

        xcdw2 = []
        xcdw_std2 = []
        Nk = len(xcdw)
        if xcdw_order=='kkobm':
            for iomeg,blist in enumerate(mu_map):
                xcdw2.append([])
                xcdw_std2.append([])
                for ibeta,mulist in enumerate(blist):
                    xcdw2[iomeg].append([])
                    xcdw_std2[iomeg].append([])
                    for imu,mu in enumerate(mulist):
                        #xcdw2[iomeg][ibeta].append([])
                        #xcdw_std2[iomeg][ibeta].append([])

                        MomentumData = zeros([Nk,Nk])
                        MomentumData_std = zeros([Nk,Nk])
                        for in1 in range(Nk):
                            for in2 in range(Nk):
                                MomentumData[in1,in2]     = xcdw[in1,in2,iomeg,ibeta,imu]
                                MomentumData_std[in1,in2] = xcdw_std[in1,in2,iomeg,ibeta,imu]
                        xcdw2[iomeg][ibeta].append(MomentumData)
                        xcdw_std2[iomeg][ibeta].append(MomentumData_std)
        else:
            xcdw2    = xcdw
            xcdw_std2 = xcdw_std

        if(xcdw_flip=='y'):
            for iomeg,blist in enumerate(mu_map):
                for ibeta,mulist in enumerate(blist):
                    for imu,mu in enumerate(mulist):
                        xcdw2[iomeg][ibeta][imu] = xcdw2[iomeg][ibeta][imu][::-1,::-1]
                        xcdw_std2[iomeg][ibeta][imu] = xcdw_std2[iomeg][ibeta][imu][::-1,::-1]

        auto_Xavg = load(folder+'auto_ogm_X_avg.npy')
        auto_X0   = load(folder+'auto_ogm_X0.npy')
    except:
        x         = []
        x_std     = []
        xcdw2      = []
        xcdw_std2  = []
        auto_Xavg = []
        auto_X0   = []
    return omegas,betas,Ts,dens,dens_std,mu_map,x,x_std,xcdw2,xcdw_std2,auto_Xavg,auto_X0




#assuming same number of omegas and betas
def myConcatMus(a, b):
    c = []
    indices = []
    for iomeg,blist in enumerate(a):
        c.append([])
        indices.append([])
        for ibeta,mulist in enumerate(blist):
            #print iomeg,ibeta,'shape a b',shape(a),shape(b)
            mylist = list(a[iomeg][ibeta])+list(b[iomeg][ibeta])
            c[iomeg].append(mylist)
            indices[iomeg].append(argsort(mylist))
    return c, indices


def loadDataCombined2(folders, xcdw_orders, xcdw_flips):
    omegas,betas,Ts,dens,dens_std,mu_map_concat,x,x_std,xcdw,xcdw_std,auto_Xavg,auto_X0 = loadData(folders[0], xcdw_orders[0], xcdw_flips[0])
    
    for i in range(1, len(folders)):
        omegas2,betas2,Ts2,dens2,dens_std2,mu_map2,x2,x_std2,xcdw2,xcdw_std2,auto_Xavg2,auto_X02 = loadData(folders[i], xcdw_orders[i], xcdw_flips[0])    
    
        mu_map_concat, indices = myConcatMus(mu_map_concat, mu_map2)
        mu_map = list(mu_map_concat)

        dens,_     = myConcatMus(dens, dens2)
        dens_std,_ = myConcatMus(dens_std, dens_std2)
        try:
            auto_Xavg,_ = myConcatMus(auto_Xavg, auto_Xavg2)
            auto_X0,_   = myConcatMus(auto_X0, auto_X02)
        except:
            pass
        x,_         = myConcatMus(x, x2)
        x_std,_     = myConcatMus(x_std, x_std2)
        xcdw,_      = myConcatMus(xcdw, xcdw2)
        xcdw_std,_  = myConcatMus(xcdw_std, xcdw_std2)

    for i,blist in enumerate(mu_map_concat):
        for j,_ in enumerate(blist):
        
            mu_map[i][j]   = [mu_map_concat[i][j][k] for k in indices[i][j]]
            dens[i][j]     = [dens[i][j][k] for k in indices[i][j]]
            try:
                auto_Xavg[i][j]     = [auto_Xavg[i][j][k] for k in indices[i][j]]
                auto_X0[i][j]       = [auto_X0[i][j][k] for k in indices[i][j]]
            except:
                pass
            x[i][j]         = [x[i][j][k] for k in indices[i][j]]
            x_std[i][j]     = [x_std[i][j][k] for k in indices[i][j]]
            xcdw[i][j]      = [xcdw[i][j][k] for k in indices[i][j]]
            xcdw_std[i][j]  = [xcdw_std[i][j][k] for k in indices[i][j]]

    return omegas,betas,Ts,dens,dens_std,mu_map,x,x_std,xcdw,xcdw_std,auto_Xavg,auto_X0




#lamb = 'nvsmu_l0p55'
#lamb = 'nvsmu_l0p45'
#lamb = 'nvsmu_l0p35'

figs = ''

if True:
    #folder = '../outputfiles_nvsmu_l0p55/'
    #folder = '../outputfiles_nvsmu_l0p45/'

    folder = '../results/'
    figs    = '../figs'
    if not os.path.exists(figs):
        os.mkdir(figs)
    Nk   = 8
    mydata = loadData(folder, 'obmkk', 'n')



    
omegas,betas,Ts,dens,dens_std,mu_map,x,x_std,xcdw,xcdw_std,auto_Xavg,auto_X0 = mydata


#setting up mu map for Holstein l0p5 omega=6.8 run on sherlock
#based on data from n_vs_mu on SIMES for 

Nmu = 21
fills = linspace(0.0, 1, Nmu) 
mu_map_interpolated = []

for iomeg,blist in enumerate(mu_map):
    mu_map_interpolated.append([])
    for ibeta,mulist in enumerate(blist):
        mu_map_interpolated[iomeg].append([])
        for ifill, fill in enumerate(fills):
            #v = interp_z(mu_map, iomeg, ibeta, fill, dens)
            #print dens[iomeg][ibeta], v, fill
            #print mu_map[iomeg][ibeta]
            mu_map_interpolated[iomeg][ibeta].append(interp_z(mu_map, iomeg, ibeta, fill, dens))
                
#save('mu_map_interpolated_nvsmu_l0p55.npy', mu_map_interpolated)
#save('mu_map_interpolated_nvsmu_l0p45.npy', mu_map_interpolated)
#save('mu_map_interpolated_nvsmu_l0p35.npy', mu_map_interpolated)
save('mu_map_interpolated_nvsmu_l0p25.npy', mu_map_interpolated)
print mu_map_interpolated
print shape(mu_map_interpolated)

print mu_map_interpolated



