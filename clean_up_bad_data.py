import sys, os
from glob import glob
from numpy import *

#dirpath_inputfiles = sys.argv[1]
dirpath = sys.argv[1]


#mu_map = load('../results/mu_map.npy')
omegas = load('../results/omegas.npy')

for folder in os.listdir(dirpath):
    myfiles = glob(dirpath+folder+'/*.log')

    #print folder

    i1 = folder.index('_')+1
    i2 = folder.index('_',i1)+1
    i3 = folder.index('_',i2)+1

    #print i1, i2, i3
    i = int(folder[i1:i2-1])
    j = int(folder[i2:i3-1])
    k = int(folder[i3:])

    #print folder, i, j, k
    
    for myfile in myfiles:
        g = 0.
        with open(myfile,'r') as f:
            for line in f:
                if 'electron-phonon g:' in line:
                    ind = line.index('electron-phonon g:')
                    g = float(line[ind+19:])
                    break

        # now compare to the correct g:
        '''
        g2 = 0.
        with open(dirpath_inputfiles+'input_%d'%i+'_%d'%j+'_%d'%k) as f:
            for line in f:
                if 'electron-phonon g:' in line:
                    ind = line.index('electron-phonon g:')
                    g2 = float(line[ind+19:])
                    break
        '''

        
        g2 = sqrt(0.5 * omegas[i]**2 * 8.)

        if g!=g2:
            print 'g1 g2', g, g2
            ind = myfile.index('sim')+4
            ind2 = myfile.index('sim',ind)-1
            ID = myfile[ind:ind2]
            print ID
        
            filesToDelete = glob(dirpath+folder+'/*'+ID+'*')
            #print 'files to delete'
            #print filesToDelete

            for afile in filesToDelete:
                print 'del ',afile
                os.remove(afile)
            
            
