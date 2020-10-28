# create a function that validates whether a number n is within the bounds
# of lower and upper. Return False if n is not an integer.

def int_within_bounds(n, lower, upper):
    if n == int(n):
        if n >= lower and n < upper:
            return True
        else:
            return False
    return False

print(int_within_bounds(3, 1, 9))
print(int_within_bounds(6, 1, 6))
print(int_within_bounds(4.5, 3, 8))