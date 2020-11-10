''' Create a function that remove the letters 'a','b' and 'c' fromt he given string
    and return the modified version. If the given string does not contain 'a','b','c',
    return None.'''

def remove_abc(txt):
	text = ""
	count = 0
	for i in txt:
		if i == "a" or i == "b" or i == "c":
			count += 1
	if count > 0:
		for i in txt:
			if i != "a" and i != "b" and i != "c":
				text += i
		return text
	else:
		return None

print(remove_abc("This might be a bit hard"))
print(remove_abc("hello world!"))
print(remove_abc(""))