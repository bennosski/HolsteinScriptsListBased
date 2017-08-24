import os, sys
import glob

folder = sys.argv[1]

files = os.listdir(folder)

logs = glob.glob(folder+'*.log')
print 'len logs',len(logs)
xscs = glob.glob(folder+'*uneqlt_sc_c_sw.dat')
print 'len xscs',len(xscs)

eqlt   = {}
uneqlt = {}
L      = {}

def increment_dict(myd, key):
    if key in myd:
        myd[key] += 1
    else:
        myd[key] = 1


for myfile in files:
    
    if 'log' in myfile:
        
        with open(folder+myfile,'r') as f:
            line = f.readline()


            while line != '':
                
                #if 'L' in line:
                #    print line

                #if 'measurement iterations' in line:
                #    print line
                if 'equal time measurements' in line:
                    #print line
                    i1 = line.index('every')+5
                    mysplit = line[i1:].split()
                    c = int(float(mysplit[0]))
                    increment_dict(eqlt, c)

                    line = f.readline()    
                    #print line
                    i1 = line.index('every')+5
                    mysplit = line[i1:].split()
                    c = int(float(mysplit[0]))
                    increment_dict(uneqlt, c)

                    break
            
                line = f.readline()

            

print ' eqlt '
print eqlt
print ' uneqlt '
print uneqlt
