#!/usr/bin/env python3
import sys

n = len(sys.argv) - 1
i = 1
if n == 0:
	print("none")
else:
	print(f"parameters: {n}")
# for i = 1, i <= n, i += 1:
	for i in range(1, n + 1):
		print(f"{sys.argv[i]}: {len(sys.argv[i])}")
