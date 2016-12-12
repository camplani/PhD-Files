##!/usr/bin/env python
## 
#import re
#
#inputfile = open("wssnt10.txt", "r")
#
#for line in inputfile:
#    if re.match("(.*)(L|l)ove(.*)", line ):
#        print line,
#inputfile.close()

		
##!/usr/bin/env python
# import re
# 
# shakes = open("wssnt10.txt", "r")
# love = open("love.txt", "w")
# 
# for line in shakes:
#     if re.match("(.*)(L|l)ove(.*)", line):
## >> is needed if you print in a file
#         print >> love, line,

##########################################################################################
import re

inputfile = open("ABBA_Controller_pc-lar-mon-01.cern.ch_1474704257.out", "r")
outfile = open("info.txt", "w")
lines = open("ABBA_Controller_pc-lar-mon-01.cern.ch_1474704257.out", "r").read().splitlines() 

previous_line = ''

for line in inputfile:
	if re.match("(.*)runNumber  =(.*)", line):
		print >> outfile, line,
	if re.match("(.*)lost locked state(.*)", line):
		print >> outfile, "TIMESTAMP: " + previous_line,
		print >> outfile, line + "\n"
	previous_line = line 


outfile.close()
inputfile.close()
###########################################################################################

#for eachLine in dataFile:
#    if "(.*)lost locked state(.*)" in Line:
#            tmpStr = ' '
#            for char in eachLine:
#                tmpStr += char
#            s = tmpStr.split()
#            print '\t'.join((s[0], s[3], s[4]))
#    else next(iter)
		
# text = "Denver.dwg Group Layer\\Denver.dwg Annotation"
# ext = ".dwg"
# 
# fileNameOnly = text[:text.find(ext) + len(ext)]
# print fileNameOnly
		

# text = "hello world in the new file"
# ext = "in"
# 
# fileNameOnly = text[:text.find(ext) + len(ext)]
# print fileNameOnly

		
#
#string = "abcdefgh"
#
## Two-character substring.
#two = string[0:2]
## Three-character substring.
#three = string[0:3]
## Four-character substring.
#four = string[0:4]
## Five-character substring.
#five = string[0:5]
#print(two)
#print(three)
#print(four)
#print(five)

		
#string = "abcdefgh"
#
## Three characters starting at index 2.
#offset = 2
#length = 3
#sliced = string[offset:offset+length]
#print(sliced)

#def first_words(input, words):
#    for i in range(0, len(input)):
#        # Count spaces in the string.
#        if input[i] == ' ':
#            words -= 1
#        if words == 0:
#            # Return the slice up to this point.
#            return input[0:i]
#    return ""
#
## Test our method.
#test = "Stately, plump Buck Mulligan came from the stairhead."
#result = first_words(test, 4)
#print(result)

#lines = open("love.txt", "r").read().splitlines() 
#
#previous_line = '' 
#for line in lines: 
# if "love" in line:
#  print "Trying to set the timestamp: " + previous_line 
# previous_line = line 