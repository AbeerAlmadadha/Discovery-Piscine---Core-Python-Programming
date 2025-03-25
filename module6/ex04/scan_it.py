#!/usr/bin/env python3
import sys
import re

i = len(sys.argv) - 1
if i < 2:
	print("none")
else:
	matches = re.findall(sys.argv[1], sys.argv[2])
	if len(matches) == 0:
		print("none")
	else:
		print(len(matches))
