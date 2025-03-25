#!/usr/bin/env python3

Original_array = [2, 8, 9, 48, 8, 22, -12, 2]
New_array = []
c = 0
while c < len(Original_array):
	if Original_array[c] > 5:
		New_array.append(Original_array[c] + 2)
	c += 1
print(Original_array)
print(New_array)
