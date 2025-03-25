#!/usr/bin/env python3

num1 = float(input("Enter the first number:\n").strip())
num2 = float(input("Enter the second number:\n").strip())
res = num1 * num2
print(f"{int(num1) if num1.is_integer() else num1} x {int(num2) if num2.is_integer() else num2} = {int(res) if res.is_integer() else res}")
if res < 0:
	print("The result is negative.")
elif res > 0:
	print("The result is positive.")
else:
	print("The result is positive and negative.")
