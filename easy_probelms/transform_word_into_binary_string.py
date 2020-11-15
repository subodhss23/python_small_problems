''' write a function that transforms all letters from [a, m] to 0 and letters from [n, z] to 1 
    in a string.'''


def convert_binary(string):
    zero = 'abcdefghijklm'
    one = 'nopqrstuvwxyz'
    new_string = ''
    for i in string:
        if i.lower() in zero:
            new_string+='0'
        elif i.lower() in one:
            new_string+='1'
    return new_string

print(convert_binary('aksldj'))
print(convert_binary("house"))
print(convert_binary("excLAIM"))
print(convert_binary("moon"))