''' Create a function, that will for a given a,b,c, do the following:
    1. Add a to iteself b times
    2. check if the result is divisible by c
'''

def abcmath(a, b, c):
    sum = a * 2 ** b
    return sum % c == 0

print(abcmath(42, 5, 10))
# print(abcmath(5,2,1))
# print(abcmath(1,2,3))