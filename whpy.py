#! /bim/usr/python

import whois

f = open("file","r")
fr = open("res_file","w")
lines = f.read()
wh = whois.whois(lines.replace('\n',''))
print wh
fr.write(str(wh))

f.close()
fr.close()
