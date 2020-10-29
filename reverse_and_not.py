''' write a function that takes an integer i and returns an integer with the integer
    backwards followed by the original integer.'''

def reverse_and_not(i):
    result = ''
    int_str = str(i)
    reversed = int_str[::-1]
    result = reversed + int_str
    return int(result)

print(reverse_and_not(123))
print(reverse_and_not(152))
print(reverse_and_not(123456789))