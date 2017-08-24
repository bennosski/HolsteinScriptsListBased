import sys, os
from numpy import *

folder = sys.argv[1]

files = os.listdir(folder)

du = []
dd = []
for myfile in files:
    if 'density_u.dat' in myfile:
        du.append(mean(fromfile(folder+myfile)))
    if 'density_d.dat' in myfile:
        dd.append(mean(fromfile(folder+myfile)))

du = asarray(du)
dd = asarray(dd)
dens = du + dd

print mean(dens)
print std(dens)
print len(dens)
