''' The right shift operation is similar to floow division by powers of two.

    Write a function that mimics(wihtout the use of >>) the right shift operator
    and returns the result fromt he two given integers. '''
import math
def shift_to_right(x, y):
    return math.floor(x/ 2** y)

# print(shift_to_right(80, 8))
# print(shift_to_right(-24, 4))
# print(shift_to_right(-5, 2))
print(shift_to_right(80, 3))
print(shift_to_right(-24, 2))
print(shift_to_right(-5, 1))
print(shift_to_right(4666, 6))
print(shift_to_right(3777, 6))
print(shift_to_right(-512, 10))