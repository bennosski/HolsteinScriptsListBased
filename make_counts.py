import os
import glob
import sys

dirpath = sys.argv[1]
folders = os.listdir(dirpath)

for folder in folders:
    files = glob.glob(dirpath+folder+'/*')
    print folder,len(files)
