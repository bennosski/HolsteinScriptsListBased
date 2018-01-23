import sys
import os
import subprocess
import make_mu_map_Holstein8b8Lambda_bigOmega_auto as mmm


def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])

def confirm():
    y = raw_input("confirm?")
    if y!='y':
        quit()

folder = 1
lamb_str = sys.argv[1]
    
#print "folder number = ",folder
print "lambda = ",lamb_str
confirm()

assert folder%2==1

os.mkdir('../inputfiles_nvsmu_'+lamb_str+'_bigOmega/')
os.mkdir('../outputfiles_nvsmu_'+lamb_str+'_bigOmega/')
print '\nmade directories'

mmm.main(folder, lamb_str)

bash_command('python create_multiple_input_files.py ../inputfiles_nvsmu_'+lamb_str+'_bigOmega/')

print 'testing if continue before finishing making input files'





