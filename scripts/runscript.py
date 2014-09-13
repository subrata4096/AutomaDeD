#!/usr/local/bin/python
#Author: Subrata Mitra (mitra4@purdue.edu)

import sys
import os
import subprocess as sub
""" When callpath library is used, this script will convert the output into filename:line number format.
    Following env variable should be set:
    callpath_DIR=<call path installation dir>
    
    The script should be run as:
    ./runscripts.py <Prodometer so path> mpiexec <other related args>
    
    It will printout the outpot with file name line number info on std-out    

"""
if __name__ == "__main__":
	print sys.argv
	prodometerLIb = sys.argv[1]
	othercommands = str(' '.join(sys.argv[2:]))
	print prodometerLIb
	print othercommands
	runCommand = "LD_PRELOAD=" + prodometerLIb + " " + othercommands + " > out.txt"
	os.system(runCommand)
	callpath_translate= os.environ['callpath_DIR'] + "/bin/translate"
        call_command = callpath_translate + " < " + "out.txt"
	os.system(call_command)
	p = sub.Popen('date',stdout=sub.PIPE,stderr=sub.PIPE)
        output, errors = p.communicate()
        print output

