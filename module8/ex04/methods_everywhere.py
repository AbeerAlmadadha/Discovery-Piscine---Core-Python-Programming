#!/usr/bin/env python3
import	sys

def	shrink(str):
	i = 0
	while i < 8:
		print(str[i], end="")
		i += 1
	print()

def enlarge(str):
	i = len(str)
	while i < 8:
		str += 'Z'
		i += 1
	print(str)

i = 1
if len(sys.argv) == 1:
	print("none")
else:
	while i < len(sys.argv):
		if len(sys.argv[i]) < 8:
			enlarge(sys.argv[i])
		elif len(sys.argv[i]) > 8:
			shrink(sys.argv[i])
		else:
			print(sys.argv[i])
		i += 1
