import os, sys
from glob import glob
from numpy import *

dirpath = sys.argv[1]


myfiles = glob(dirpath+'*.log')

print len(myfiles)


myfiles = glob(dirpath+'*phonon_iteration_X_avg.dat')
x = fromfile(myfiles[0])
print 'len of phonon file ',shape(x)


myfiles = glob(dirpath+'*uneqlt_G0tau_u.dat')
x = fromfile(myfiles[0])
print 'len of Gtau file ',shape(x)

