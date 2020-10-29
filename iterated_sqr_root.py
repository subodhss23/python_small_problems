''' The iterated square root of a number is the number of times the square
    root function must be applied to bring the number strictly under 2

    Given an integer, return its iterated square root. Return "invalid" if it is negative. '''

def i_sqrt(n):
    counter = 0
    if n <= 0:
        return 'invalid'
    else:
        while (n >= 2):
            n = n ** 0.5
            counter += 1
        return counter
      


# print(i_sqrt(1))
#print(i_sqrt(2))
# print(i_sqrt(7))
print(i_sqrt(27))
# print(i_sqrt(256))
# print(i_sqrt(-1))