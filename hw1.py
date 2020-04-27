#!/usr/bin/python

import sys

argLen = len(sys.argv)

for i in range(1,argLen):
	with open(sys.argv[i],'r') as file:
		print(file.read())
		
