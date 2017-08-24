from numpy import *
import subprocess, os, time

##first get a sense of where mu is with sdev
#apparently mu should be around -lambda*W = -N*g^2/omega^2  where N is the total N

N = 64
W = 8.

##############
#for holstein#
##############
#omegas = linspace(0.1,1.9,10)
#lambdas = linspace(0.1,1.2,12)
#bws    = [40,20,8,7,5,3,2.75,2.5,2.25,2] # a function of omega


omegas = linspace(0.1,1.9,10)
lambdas = arange(0.02,0.46,0.04)

save('omegas',omegas)
save('lambdas',lambdas)

#mu_map = zeros([len(omegas), len(lambdas), 11])
#bw_map = zeros([len(omegas), len(lambdas), 11])
mu_map = load('mu_map2.npy')
bw_map = load('bw_map2.npy')

dirpath = 'forward_inputfiles/'

#raw_input("remember to set L in the file 'input' \n and 5000 measurement sweeps")
#beta = float(raw_input('input beta: '))

def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])

    
istart = 0
jstart = 0
kstart = 0

for i in range(len(omegas)):
    omega = omegas[i]
    for j in range(len(lambdas)):
        l = lambdas[j]

        g = sqrt(l * omega**2 * W / N) 
        #mus = linspace(-l*W-4., -l*W+4., 11)

        for k in range(shape(mu_map)[2]):
            #mu_map[i,j,k] = mus[k]

            
            if k + j*shape(mu_map)[2] + i*shape(mu_map)[2]*len(lambdas) < kstart + jstart*shape(mu_map)[2] + istart*shape(mu_map)[2]*len(lambdas):
                continue


            mu = mu_map[i,j,k]
            bw = bw_map[i,j,k]

            label = '_%d'%i+'_%d'%j+'_%d'%k
            
            input_file_name    = dirpath+'input'+label
            #output_folder_name = 'output'+label
            
            cmd = 'cp input temp1'+label
            cmd += """; sed "/chemical/c\mu %1.15f"""%mu+""" # chemical potential" temp1"""+label+' > temp2'+label
            cmd += '; cp temp2'+label+' '+'temp1'+label
            cmd += """; sed "/phonon coupling/c\phonon_g %1.15f"""%g+""" # phonon coupling" temp1"""+label+' > temp2'+label
            cmd += '; cp temp2'+label+' '+'temp1'+label
            cmd += """; sed "/phonon_block_box_width/c\phonon_block_box_width %1.2f"""%bw+""" # above for block updates" temp1"""+label+' > temp2'+label
            cmd += '; cp temp2'+label+' '+'temp1'+label
            cmd += """; sed "/phonon_omega/c\phonon_omega %1.3f"""%omega+""" # phonon coupling" temp1"""+label+' > temp2'+label
            cmd += '; cp temp2'+label+' '+input_file_name
            cmd += '; rm temp2'+label+'; rm temp1'+label

            bash_command(cmd)
            
            time.sleep(0.1)
            

#save mumap....
