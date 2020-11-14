''' Imagine a school that kids attend for 6 years. In each year, there are five groups started,
    marked with the letters a,b,c,d,e. For the first year, the groups are 1a, 1b, 1c, 1d, 1e and 
    for the lst year, the group are 6a, 6b, 6c, 6d, 6e.

    write a function that returns the groups in the school by year(as a string), separated with 
    comma and a space in the form of "1a, 1b, 1c, 1d, 1e, 2a, 2b (....) 5d, 5e, 6a, 6b, 6c, 6d, 6e".'''


def print_all_groups():
	result = []
	for i in '123456':
		for x in 'abcde':
			result.append(i+x)
	return ', '.join(result)

print(print_all_groups())