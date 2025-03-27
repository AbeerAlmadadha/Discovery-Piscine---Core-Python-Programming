#!/usr/bin/env python3

def	array_of_names(persons):
	p_list = []
	for key, value in persons.items():
		p_list.append(f"{key.capitalize()} {value.capitalize()}")
	return p_list
	
persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))
