''' Given two integer a and b, return how many times a can be halved while still
    being greater than b. '''

def halve_count(one, two):
    count = 0
    while one > two:
        one = one / 2
        count+=1
        print('inside while loop')
    return count - 1

print(halve_count(1324, 98))
print(halve_count(624, 8))
print(halve_count(1000, 3))