#!/usr/bin/env python3
import sys

i = 0
x = 0
if len(sys.argv) != 2:
	print("none")
else:
	while x < len(sys.argv[1]):
		if sys.argv[1][x] == 'z':
			i += 1
		x += 1
	if i != 0:
		print("z" * i)
	else:
		print("none")
