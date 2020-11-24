''' Write three functions:
    1. boolean_and
    2. boolean_or
    3. boolean_xor

    These functions should evaluate a list of True and False values, starting from the leftmost element and evaluating pariwise.'''


def boolean_and(lst):
	for i in range(1,len(lst)):
		if lst[i-1] and lst[i]:
			lst[i] = True
		else:
			lst[i] = False
	return lst[-1]

def boolean_or(lst):
	for i in range(1,len(lst)):
		if lst[i-1] or lst[i]:
			lst[i] = True
		else:
			lst[i] = False
	return lst[-1]

def boolean_xor(lst):
	for i in range(1,len(lst)):
		if lst[i-1] != lst[i]:
			lst[i] = True
		else:
			lst[i] = False
	return lst[-1]

    
print(boolean_and([True, True, False, True]))
print(boolean_or([True, True, False, False]))
print(boolean_xor([True, True, False, False]))
