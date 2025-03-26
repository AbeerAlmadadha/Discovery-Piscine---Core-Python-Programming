#!/usr/bin/env python3
import	sys

def	downcase_it(str):
	return str.lower()
i = 1
if len(sys.argv) == 1:
	print("none")
else:
	while i < len(sys.argv):
		print(downcase_it(sys.argv[i]))
		i += 1
