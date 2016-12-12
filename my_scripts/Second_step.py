import re

inputfile = open("info.txt", "r")
outfile = open("link_status.txt", "w")

for line in inputfile:
	if re.match("TIMESTAMP: virtual bool Abba", line):
		print >> outfile, "\n",
	else:
		print >> outfile, line,


outfile.close()
inputfile.close()