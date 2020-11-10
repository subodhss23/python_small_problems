''' Write a function that returns the longest sequence of consecutive zeros
    in a binary string. '''


def longest_zero(s):
	new_lst = s.split('1')
	size = []
	for i in new_lst:
		size.append(len(i))
	return max(size) * '0'
    

print(longest_zero("01100001011000"))
print(longest_zero("100100100"))
print(longest_zero("11111"))