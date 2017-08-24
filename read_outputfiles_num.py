import sys, os


folders = os.listdir('outputfiles')


for folder in folders:

    #if 't_9_' in folder:

     files = os.listdir('outputfiles/'+folder)

     if len(files)/58 > 20:

         ct = 0
         for myfile in files:
             if '.log' in myfile:
                 ct += 1

         print folder,ct
     
         
