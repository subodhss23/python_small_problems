''' Given a simple math expression as a string, neatly format it as an equation.'''

def format_math(expr):
    new_lst = expr.split()
    if new_lst[1] == '+' or new_lst[1] == '-':
        return expr + ' = ' + str(eval(expr))
    elif new_lst[1] == 'x':
        return expr + ' = ' + str(int(new_lst[0]) * int(new_lst[2]))
    elif new_lst[1] == '/':
        return expr + ' = ' + str(int(new_lst[0]) // int(new_lst[2]))

print(format_math("3 + 4"))
print(format_math("3 - 2"))
print(format_math("4 x 5"))
print(format_math("6 / 3"))