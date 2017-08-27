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
auto_ogm = []


for i,blist in enumerate(mu_map):
  auto_ogm.append([])
  for j,mulist in enumerate(blist):
    auto_ogm[i].append([])
    for k,mu in enumerate(mulist):

      folder = dirpath + 'output_%d'%i+'_%d'%j+'_%d'%k + '/'
      a = rc.read_X(folder, quantity)

      try:
        if not isnan(a):
          auto_ogm[i][j].append(a)
          string = '%d'%i+' %d'%j+' %d'%k+' %.15f'%a+'\n'
      except:
        print "error ", a, type(a)
        auto_ogm[i][j].append(0.)

                
print 'saving files'
save('../results/auto_ogm_'+quantity, auto_ogm)
exit()

