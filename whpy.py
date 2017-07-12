#! /bim/usr/python

import whois

f = open("file","r")
lines = f.readline()
try:
	wh = whois.whois(lines)
	print wh
	print lines
except:
	print "err in file or output!!"
	print lines
