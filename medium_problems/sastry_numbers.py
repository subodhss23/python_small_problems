''' In this challenge, you have to establish if a given integer n is a Sastry
    number. If the number resulting from the concatenation of an integer n with
    successor is a perfect square, then n is a Sastry Number.

    Given a positive integer n, implement a function that returns True if n 
    is a Sastry number, or False if it's not.'''

import math
def is_sastry(n):
    new_n = n + 1
    new_num = int(str(n) + str(new_n))
    new_sqrt = math.sqrt(new_num)
    return new_sqrt == round(new_sqrt)

# def is_sastry(n):
#     concat = int(str(n) + str(n+1)) ** 0.5
#     return concat == int(concat)

print(is_sastry(183))
print(is_sastry(184))
print(is_sastry(106755))

