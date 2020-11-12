''' Count the amount of ones in the binary representation of an integer.
    For example, since 12 is 1100 in binary, the return value should be 2.'''

def count_ones(num):
    new_str =  str(bin(num))
    count = 0
    for i in new_str:
        if i == '1':
            count +=1
    return count

'''
def count_ones(num):
    return bin(num).count("1")
'''
print(count_ones(0))
print(count_ones(100))
print(count_ones(999))