import sys
import os
import subprocess
import make_mu_map_Holstein8b8Lambda_bigOmega_auto as mmm
import make_dens_vs_ogm_auto as mdvo
import interp_auto as ia

# folder 7/8 = 0.45

def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])

def confirm():
    y = raw_input("confirm?")
    if y!='y':
        quit()
    
if not os.path.exists('../results/'):
    os.mkdir('../results/')

# lamb_str  e.g. l0p45

folder = 2
lamb_str = sys.argv[1]

print "lambda = ",lamb_str
confirm()



os.mkdir('../inputfiles_'+lamb_str+'_bigOmega/')
os.mkdir('../outputfiles_'+lamb_str+'_bigOmega/')
print '\nmade directories'

# collect the densities from nvsmu run
mdvo.main('../outputfiles_nvsmu_'+lamb_str+'_bigOmega/')

# now do the interpolation
ia.main('mu_map_interpolated_nvsmu_'+lamb_str+'_bigOmega.npy')

# make the new mu map
mmm.main(folder, lamb_str)

# make the new input files
bash_command('python create_multiple_input_files.py ../inputfiles_'+lamb_str+'_bigOmega/')

print 'done'




