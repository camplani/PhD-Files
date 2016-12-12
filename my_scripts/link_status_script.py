# Alessandra Camplani - link status script
###########################################
# The files "ABBA_Controller_pc-lar-mon-01.cern.ch_*.out" can be found on
# pc-lar-mon-01 machine in folder /logs/tdaq-06-01-01/LArABBA
#
# To download the file on your laptop 
# On pc-lar-mon-01 machine:
# scp ABBA_Controller_pc-lar-mon-01.cern.ch_1474646229.out /atlas-home/1/youruser/Public
# On lxplus:
# scp youruser@atlasgw.cern.ch:/atlas-home/1/youruser/Public/ABBA_Controller_pc-lar-mon-01.cern.ch_1474646229.out public/
# From your laptop:
# scp youruser@lxplus.cern.ch:/afs/cern.ch/user/y/youruser/public/ABBA_Controller_pc-lar-mon-01.cern.ch_1474704257.out /home/yourlaptop/yourfolder
###########################################

import re
import os

# input file: change the name accordingly
inputfile = open("ABBA_Controller_pc-lar-mon-01.cern.ch_1474704257.out", "r")
# intermediate file (deleted at the end)
outfile = open("tmp_info.txt", "w")

previous_line = ''

for line in inputfile:
	if re.match("(.*)runNumber  =(.*)", line):
		print >> outfile, line,
	if re.match("(.*)fibres are locked in Ppod(.*)", line):
		print >> outfile, line,
	if re.match("(.*)lost locked state(.*)", line):
		print >> outfile, "TIMESTAMP: " + previous_line,
		print >> outfile, line,
	previous_line = line 

outfile.close()
inputfile.close()

inputfile = open("tmp_info.txt", "r")
# output file: change the name accordingly
outfile = open("link_status_RunTime_1474704257.txt", "w")

for line in inputfile:
	if re.match("TIMESTAMP: virtual bool Abba", line):
		print >> outfile, " ",
	else:
		print >> outfile, line,

outfile.close()
inputfile.close() 
os.remove("tmp_info.txt")