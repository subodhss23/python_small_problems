''' A quadratic equation a x^2 + b x + c = 0 has either 0, 1, or 2 distinct
    colutions for real values of x. Given a, b and c, you should return the
    number of solutions to the equation.'''


def solutions(a, b, c):
    result = b ** 2 - 4 * a * c
    if result > 0:
       return 2
    elif result == 0:
        return 1
    elif result < 0:
        return 0 


print(solutions(1, 0, -1))
print(solutions(1, 0, 0))
print(solutions(1, 0, 1))