''' Create a function that will handle simple math expresssions. The input is an expression in the form 
    of a string, and the result is returned in the form of a float.'''

def calculator(txt):
    return eval(txt)


print(calculator("23+4"))
print(calculator("45-15"))
print(calculator("13+2-5*2"))
print(calculator("49/7*2-3"))