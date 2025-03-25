#!/usr/bin/env python3

num = int(input("Enter a number\n").strip())
c = 0
while c < 10:
	print(f"{c} x {num} = {c * num}")
	c += 1
