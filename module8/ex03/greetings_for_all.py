#!/usr/bin/env python3

def	greetings(name=''):
	if isinstance(name, str):
		if name:
			print(f"Hello, {name}.")
		else:
			print("Hello, noble stranger")
	else:
		print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
