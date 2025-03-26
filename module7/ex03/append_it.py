#!/usr/bin/env python3
import sys

i = 1
if len(sys.argv) == 1:
	print("none")
else:
	while i < len(sys.argv):
		if not (sys.argv[i].endswith("ism")):
			print(sys.argv[i] + "ism")
		i += 1 
