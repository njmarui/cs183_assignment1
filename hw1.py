#!/usr/bin/python

import sys

iterFile = iter(sys.argv)
next(iterFile)

for x in iterFile:
	with open(x,'r') as file:
		print(file.read())
		
