import os
import sys
import glob
from numpy import *

mydict = {}

dirpath = sys.argv[1]

files = glob.glob(dirpath+'/*')

for myfile in files:
    with open(myfile, 'r') as f:
        beta = None
        time = None
        for line in f:
            if('beta:') in line:
                i1 = line.index(':')+2
                beta = float(line[i1:])

            if('total wall time' in line):
                i1 = line.index('e')+1
                time = float(line[i1:])

        if time is None:
            continue
        if beta in mydict:
            mydict[beta].append(time)
        else:
            mydict[beta] = [time]


for beta in sorted(mydict):
    print beta,' ',mean(mydict[beta])/3600

save('../mydict', mydict)
