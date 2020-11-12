''' Create a function that takes a string and returns a string in which each
    character is repeated once. '''

def double_char(str):
    new_str = ''
    for i in str:
        new_str += i*2
    return new_str

print(double_char("String"))
print(double_char("Hello World!"))
print(double_char("1234!_ "))