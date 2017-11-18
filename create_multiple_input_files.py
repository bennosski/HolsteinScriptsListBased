from numpy import *
import subprocess, os, time, sys

##first get a sense of where mu is with sdev
#apparently mu should be around -lambda*W = -N*g^2/omega^2  where N is the total N

N = load('../N.npy')
print 'N ',N

W = 8.

omegas = load('../omegas.npy')
betas  = load('../betas.npy')
mu_map = load('../mu_map.npy')
l      = load('../lamb.npy')

nsampl = load('../nsampl.npy')
nequil = load('../nequil.npy')

print 'len omegas ',len(omegas)
print 'len betas ',len(betas)
print 'mu map shape ',shape(mu_map)

dirpath = sys.argv[1]

#raw_input("remember to set L in the file 'input' \n and 5000 measurement sweeps")
#beta = float(raw_input('input beta: '))

def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])

def myreplace(key, rep, label):
    mystr = '; cp temp2'+label+' '+'temp1'+label
    mystr += """; sed "/""" + key + "/c\\" + rep + "\" temp1" + label + ' > temp2' + label 
    return mystr

y = raw_input('nuneqult = 0!!!!!!!! (y/n)?')
if y!='y':
    1/0

for i,blist in enumerate(mu_map):
#for i in range(2):
    omega = omegas[i]
    #for j in range(2):
    for j,mulist in enumerate(blist):
    
        #holstein code definition
        g = sqrt(l * omega**2 * W)
  
        for k,mu in enumerate(mulist):
             
            print i,j,k

            bw = 19.2/omega/betas[j] # a guess for bw

            L = int(round(betas[j]/0.1))

            if L==8:
                prodBlen = 4
            else:
                prodBlen = 8
            #prodBlen = 5

            neqlt   =  L

            nuneqlt = 0
            #nuneqlt = L

            label = '_%d'%i+'_%d'%j+'_%d'%k
            
            input_file_name    = dirpath+'input'+label
            #output_folder_name = 'output'+label
            
            cmd = 'cp input temp1'+label
            cmd += """; sed "/chemical/c\mu %1.15f"""%mu+""" # chemical potential" temp1"""+label+' > temp2'+label
            cmd += '; cp temp2'+label+' '+'temp1'+label
            cmd += """; sed "/phonon coupling/c\phonon_g %1.15f"""%g+""" # phonon coupling" temp1"""+label+' > temp2'+label

            cmd += '; cp temp2'+label+' '+'temp1'+label
            cmd += """; sed "/beta/c\L      %d"""%L+""" # sets beta (num imag time steps)" temp1"""+label+' > temp2'+label
            cmd += '; cp temp2'+label+' '+'temp1'+label
            cmd += """; sed "/prodBlen/c\prodBlen  %d"""%prodBlen+""" # number of B matrices to multiply before QR stuff" temp1"""+label+' > temp2'+label

            cmd += myreplace('between equal','neqlt    %d'%neqlt+'   # number of imag. time steps between equal time measurements.',label) 
            cmd += myreplace('nuneqlt','nuneqlt    %d'%nuneqlt+'   # number of sweeps between unequal time measurements; 0 to diable',label) 

            cmd += myreplace('nequil','nequil %d'%nequil+'    # number of warmup/equilibration sweeps',label)
            cmd += myreplace('nsampl','nsampl %d'%nsampl+'    # number of measurement/sampling sweeps',label)
            
            #cmd += '; cp temp2'+label+' '+'temp1'+label
            #cmd += """; sed "//c\L      %d"""%L+""" # sets beta (num imag time steps)" temp1"""+label+' > temp2'+label

            cmd += '; cp temp2'+label+' '+'temp1'+label
            cmd += """; sed "/phonon_block_box_width/c\phonon_block_box_width %1.2f"""%bw+""" # above for block updates" temp1"""+label+' > temp2'+label
            cmd += '; cp temp2'+label+' '+'temp1'+label
            cmd += """; sed "/phonon_omega/c\phonon_omega %1.3f"""%omega+""" # phonon coupling" temp1"""+label+' > temp2'+label
            cmd += '; cp temp2'+label+' '+input_file_name
            cmd += '; rm temp2'+label+'; rm temp1'+label

            bash_command(cmd)
            
            time.sleep(0.1)
            

#save mumap....

