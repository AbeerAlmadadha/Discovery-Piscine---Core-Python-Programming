#!/usr/bin/env python3

user_input_float = float(input("Give me a number: "))
user_input_int = int(user_input_float)
if user_input_float - user_input_int == 0:
	print("This number is an integer.")
else:
	print("This number is a decimal.")
