#!/usr/bin/env python3

Original_array = [2, 8, 9, 48, 8, 22, -12, 2]
New_array = Original_array.copy()
c = 0

while c < len(New_array):
	New_array[c] = New_array[c] + 2
	c += 1

print("Original array:", Original_array)
print("New array:", New_array)
