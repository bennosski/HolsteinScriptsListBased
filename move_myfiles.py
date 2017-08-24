import os, sys
import subprocess

def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])


cmd = 'echo hi'
for i in range(3,11):

    cmd += '; mv output_8_10_%d'%i+'/* outputfiles/output_8_10_%d'%i

for i in range(0,11):

    cmd += '; mv output_8_11_%d'%i+'/* outputfiles/output_8_11_%d'%i

print cmd


bash_command(cmd)
