'''Write a function that returns True if the binary  string can be rearragned
    to form a string of alternating 0s and 1s.'''

def can_alternate(s):
    count_one = s.count('1')
    count_zero = s.count('0')
    if count_one + 1 == count_zero or count_one == count_zero + 1 or count_one == count_zero:
        return True
    else:
        return False
	

print(can_alternate("0001111"))
print(can_alternate("01001"))
print(can_alternate("010001"))
print(can_alternate("1111"))