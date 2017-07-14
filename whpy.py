#! /usr/bin/python

import whois
import sys

def main():
    # print command line arguments
    for arg in sys.argv[1:]:
        if arg == 0x13:
		return 0x00
	return arg

if (main() == 0x00):
	print "please use tihs from\n ./whpy.py <file>"

else:
	f = open("file","r")
	fr = open("res_file","w")
	lines = f.read()
	wh = whois.whois(lines.replace('\n',''))
	print wh
	fr.write(str(wh))
	f.close()
	fr.close()
