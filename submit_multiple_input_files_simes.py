from numpy import *
import subprocess, time, os
import sys
import glob

def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])


#existing_files = os.listdir('outputfiles1/')
submit_ct = 0

    
#last_submitted = [0,0,0]
#last_submitted = loadtxt('last_submitted')
#print 'last_submitted ',last_submitted

#[i0,j0,k0]

skip = False


mu_map = load('../mu_map.npy')

#y = raw_input('confirm: did you copy multiple submit to bin directory? (y/n)')
y = raw_input('confirm: did make changes to multiple_submit.sh to run from scripts dir? (y/n)')
y = raw_input('confirm: are you running submission in scripts dir?   (y/n)')
if y!='y':
    1/0

for i,blist in enumerate(mu_map):
    for j,mulist in enumerate(blist):
        for k,mu in enumerate(mulist):

            
            label = '_%d'%i+'_%d'%j+'_%d'%k
            
            
            input_file_name = '../'+sys.argv[1]+'input'+label
            output_folder_name = '../'+sys.argv[2]+'output'+label
            
            if os.path.exists(output_folder_name):
                files = glob.glob(output_folder_name+'/*Gtau0_u.dat')
                #print output_folder_name+'len ',len(files)
                if len(files)<14:
                    print output_folder_name+' len ',len(files),' submitting'
                else:
                    continue
            
     
            '''    
            if j>1:
                continue
            '''

            print 'submitting ',label
            
            bash_command('./multiple_submit '+input_file_name+' '+output_folder_name)
            
            submit_ct += 1
            
            #last_submitted = [i,j,k]
            #savetxt('last_submitted', last_submitted)
            
            time.sleep(0.08)

            

print submit_ct
