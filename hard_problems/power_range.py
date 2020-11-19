''' Create a function that takes in n, a, b and returns the number of positive values raised
    to the nth power that lie in the range [a, b], inclusive.'''

def power_ranger(power, minimum, maximum):
    check = 0
    for i in range(maximum + 1):
        if minimum <= (i ** power) <= maximum:
            check += 1
    return check

print(power_ranger(2, 49, 65))
print(power_range(3, 1, 27))
print(power_ranger(10, 1, 5))
print(power_ranger(5, 31, 33))
print(power_ranger(4, 250, 1300))