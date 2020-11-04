''' create a function which returns a list of booleans, from a given number. Iterating through
    the number one digit at a time, append True if the digit if the digit is 1 and False if it is 0. '''


def integer_boolean(n):
    new_lst = []
    for i in n:
        new_lst.append(bool(int(i)))
    return new_lst

print(integer_boolean('100101'))
# print(integer_boolean('10'))
# print(integer_boolean('001'))