#!/usr/bin/env python3

c1 = 0
c2 = 0
while c1 <= 10:
	print(f"Table of {c1}: ", end="")
	c2 = 0
	while c2 <= 10:
		print(f"{c1 * c2 } ", end="")
		c2 += 1
	print()
	c1 += 1
