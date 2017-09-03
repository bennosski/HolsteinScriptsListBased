from numpy import *
import subprocess, time, os
import sys
import glob

def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])

submit_ct = 0
skip = False

mu_map = load('mu_map.npy')

bash_command('cp HolsteinScriptsListBased/make_mu_map.py .')

def get_count(i,j,k):
    return i*d2*d3 + j*d3 + k

def get_ijk(c):
    i = c/(d2*d3)
    
    r = c%(d2*d3)
    j = r/d3

    k = (c%(d2*d3))%d3

    return i,j,k



y = raw_input('confirm: all temp? \n  and did you create submit scripts \n  DID YOU RUN MAKE MU_MAP AGAIN? (y/n)')
if y!='y':
    1/0

#for count in range(start, end):
#            [i,j,k] = get_ijk(count)            

for i, blist in enumerate(mu_map):
    for j, mulist in enumerate(blist):
        for k, mu in enumerate(mulist):

            print i, j, k
            
            #if j!=6:
            #    continue
            
            label = '_%d'%i+'_%d'%j+'_%d'%k
                        
            input_file_name = sys.argv[1]+'input'+label
            output_folder_name = sys.argv[2]+'output'+label

            runjob = False
            if os.path.exists(output_folder_name):
                #files = glob.glob(output_folder_name+'/*Gtau0_u.dat')
                files = glob.glob(output_folder_name+'/*')
                #print output_folder_name+'len ',len(files)
                if len(files)<250:
                    runjob = True
                    print output_folder_name+' len ',len(files),' submitting'

            else:
                runjob = True

            if runjob:
                print output_folder_name+' len ',0,' submitting'

                print('submitting ',label)                
                bash_command('sbatch submit_sherlock%d'%j + ' ' + input_file_name+' '+output_folder_name)
            
                submit_ct += 1
                
                time.sleep(0.05)

    


print(submit_ct)
