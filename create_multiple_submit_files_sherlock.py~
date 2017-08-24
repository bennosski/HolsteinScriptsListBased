from numpy import *
import subprocess, os, time, sys

##first get a sense of where mu is with sdev
#apparently mu should be around -lambda*W = -N*g^2/omega^2  where N is the total N

walltimes = load('../walltimes.npy')
betas = load('../betas.npy')

def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])

def myreplace(key, rep, j):
    mystr = """; sed "/""" + key + "/c\\" + rep + "\" temp1" + ' > ../submit_sherlock%d'%j  
    return mystr

for j,ib in enumerate(betas):
    t = int(walltimes[j])

    cmd = 'cp ../submit_sherlock temp1'
    cmd += myreplace('#SBATCH --time', '#SBATCH --time=%d'%t+':00:00', j)

    bash_command(cmd)
    time.sleep(0.1)

