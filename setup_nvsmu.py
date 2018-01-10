import sys
import os
import subprocess
import make_mu_map_Holstein8b8Lambda_bigOmega_auto as mmm


# folder 7/8 = 0.45

def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])

def confirm():
    y = raw_input("confirm?")
    if y!='y':
        quit()

folder = int(sys.argv[1])
lamb_str = sys.argv[2]
    
print "folder number = ",folder
print "lambda = ",lamb_str
confirm()

os.mkdir('../inputfiles_nvsmu_'+lamb_str+'_bigOmega/')
os.mkdir('../outputfiles_nvsmu_'+lamb_str+'_bigOmega/')
print '\nmade directories'

mmm.main(folder, lamb_str)

bash_command('python create_multiple_input_files.py ../inputfiles_nvsmu_'+lamb_str+'_bigOmega/')

print 'testing if continue before finishing making input files'





