''' Your function will be passed tow function, f and g, that don't take
    any parameters. Your function has to call them, and return a string which 
    indicates which function returns the larger number. 

        - If f returns the larger number, return the string f.
        - If g returns the larger number, return the string g.
        - If the function return the same number, return the string neither.

'''

def which_is_larger(f, g):
    if f()>g():
        return 'f'
    elif g()>f():
        return 'g'
    else:
        return 'neither'


print(which_is_larger(lambda: 5, lambda: 10))
print(which_is_larger(lambda: 25,  lambda: 25))
print(which_is_larger(lambda: 505050, lambda: 5050))

