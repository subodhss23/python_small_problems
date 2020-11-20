''' Create a function that takes a string and censors word over four characters with *'''

def censor(s):
    new_lst = s.split()
    lst_two = []
    for i in new_lst:
        if len(i) > 4:
            lst_two.append('*'* len(i))
        else:
            lst_two.append(i)
    return (' ').join(lst_two)


print(censor("The code is fourty"))
print(censor("Two plus three is five"))
print(censor("aaaa aaaaa 1234 12345"))