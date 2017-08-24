import os, sys
from glob import glob
from numpy import *

dirpath = sys.argv[1]


folders = os.listdir(dirpath)

for folder in folders:
    myfiles = glob(dirpath+folder+'/*')
    
    print folder,len(myfiles)
    
