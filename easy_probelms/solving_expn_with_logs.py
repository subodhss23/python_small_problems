''' Solving a function that takes a number a and finds the missing exponent
    x so that a when raised to the power of x is equal to b. '''

import math
def solve_for_exp(a, b):
    return math.ceil(math.log(b) / math.log(a))

print(solve_for_exp(4, 1024))
print(solve_for_exp(2, 1024))
print(solve_for_exp(9, 3486784401))