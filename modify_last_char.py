# create a function which makes the last character of a string erpeat n number of times.

def modify_last(txt, n):
    lst_char = txt[-1]
    return txt + lst_char * (n - 1)


print(modify_last("whatup", 5))
print(modify_last('fuck', 10))