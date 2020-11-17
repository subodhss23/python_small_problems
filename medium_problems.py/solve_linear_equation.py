''' Create a function that returns the value of x (the 'unknown' in the equation). Each equation will
    be formatted like this:

    x + 6 = 12 '''

def solve(eq):
    new_lst = eq.split(' ')
    print(new_lst)
    if '+' in eq:
        return int(new_lst[4]) - int(new_lst[2])
    elif '-' in eq:
        return int(new_lst[4]) + int(new_lst[2])


# print(solve("x + 43 = 50"))
# print(solve("x - 9 = 10"))
# print(solve("x + 300 = 100"))
print(solve("x - 9 = 10"))