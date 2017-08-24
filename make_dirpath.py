
from numpy import *

dirpath_input  = 'forward_inputfiles/'
dirpath_output = 'forward_outputfiles/'

text_file = open('dirpath_input.txt', "w")
text_file.write(dirpath_input)
text_file.close()

text_file = open('dirpath_output.txt', "w")
text_file.write(dirpath_output)
text_file.close()
