import sys, os
from numpy import *
import read_autocor as rc


dirpath = sys.argv[1]
quantity = sys.argv[2]
folders = os.listdir(dirpath)
#txtf = open('dirpath_output.txt', 'r')
#dirpath = txtf.readline()
#txtf.close()
#folders = os.listdir(dirpath)

mu_map = load('../mu_map.npy')
auto_ogm = zeros(shape(mu_map))

[d1,d2,d3] = shape(mu_map)


if len(sys.argv)>3:
  print 'auto checkpoint is already complete'  
  with open('auto_checkpoint.txt','r') as f:
    for line in f:
      mysplit = line.split()
      i1,i2,i3,a = int(float(mysplit[0])),int(float(mysplit[1])),int(float(mysplit[2])),float(mysplit[3])
      auto_ogm[i1,i2,i3] = a

  print 'saving files'
  save('../results/auto_ogm_'+quantity, auto_ogm)
  exit()


start = (0,0,-1)
if os.path.exists('auto_checkpoint.txt'):
  # read in where we finished
  with open('auto_checkpoint.txt', 'r') as f:
    lines = f.read().splitlines()
    last_line = lines[-1]
    #print last_line
    mysplit = last_line.split()
    start = (int(float(mysplit[0])),int(float(mysplit[1])),int(float(mysplit[2])))


print start

print d1,d2,d3

#if start[0]==d1 and start[1]==d2 and start[2]==d3:
if start==(d1-1,d2-1,d3-1):
  print 'auto checkpoint is already complete'
  
  with open('auto_checkpoint.txt','r') as f:
    for line in f:
      mysplit = line.split()
      i1,i2,i3,a = int(float(mysplit[0])),int(float(mysplit[1])),int(float(mysplit[2])),float(mysplit[3])
      auto_ogm[i1,i2,i3] = a

  print 'saving files'
  save('../results/auto_ogm_'+quantity, auto_ogm)
  exit()

print 'making new auto_checkpoint.txt'
    
for i in range(d1):
    with open('auto_checkpoint.txt','a+') as f:

      for j in range(d2):
        for k in range(d3):

          if i*d1*d3+j*d3+k<=start[0]*d1*d3+start[1]*d3+start[2]:
            continue

          print i,j,k
          folder = dirpath + 'output_%d'%i+'_%d'%j+'_%d'%k + '/'
          a = rc.read_X(folder, quantity)

          try:
              if not isnan(a):
                  auto_ogm[i,j,k] = a
                  string = '%d'%i+' %d'%j+' %d'%k+' %.15f'%a+'\n'
                  f.write(string)
          except:
              print "error ", a, type(a)
              auto_ogm[i,j,k] = 0.
              string = '%d'%i+' %d'%j+' %d'%k+' 0.'+'\n'
              f.write(string)


    f.close()

      

'''

for folder in folders:

  [i1,i2,i3] = [pos for pos,char in enumerate(folder) if char=='_']

  i = folder[i1+1:i2]
  j = folder[i2+1:i3]
  k = folder[i3+1:]


  print i,j,k
  auto_ogm[i,j,k] = rc.read_X(dirpath+folder+'/')
'''

