#Given a number n, write a function that returns PI to n decimal places.

import math
def my_pi(n):
    return round(math.pi, n)

print(my_pi(2))