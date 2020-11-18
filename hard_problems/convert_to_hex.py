''' Create a function that takes a string characters as ASCII and returns each characters hexadecimal
    value as a string.'''


def convert_to_hex(txt):
    result = ''
    lst = []
    for i in txt:
        lst.append(hex(ord(i)))
    new_str = (' ').join(lst)
    last_lst =  new_str.split('0x')
    for i in last_lst:
        result+=i
    return result

print(convert_to_hex("hello world"))
# print(convert_to_hex("Big Boi"))
# print(convert_to_hex("Marty Poppinson"))