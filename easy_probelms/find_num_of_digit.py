''' Create a function that will return an integer number containing the amount of digits
    in the given integer num.'''


def num_of_digits(n):
    return len(str(abs(n)))

print(num_of_digits(1000))
print(num_of_digits(12))
print(num_of_digits(1305981031))
print(num_of_digits(0))