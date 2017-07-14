#! /usr/bin/python

import whois
import sys

if (str(sys.argv[1:])== '[]'):
	print "please use tihs from\n ./whpy.py <file>"

else:
	a = str(sys.argv[1]).replace('[',"").replace(']',"").replace('\n',"")
	f = open(a,"r")
	fr = open("res_file","w")
	lines = f.read()
	wh = whois.whois(lines.replace('\n',''))
	print wh
	fr.write(str(wh))
	f.close()
	fr.close()
