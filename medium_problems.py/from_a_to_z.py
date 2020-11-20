''' Given a string indicating a range of letters, return a string which includes all
    the letters in that range, including the last letter. Note that if the range is
    given in capital letters, return the string in capitals also!
'''

def gimme_the_letters(spectrum):
    new_str = ''
    new_lst = spectrum.split('-')
    if new_lst[0] == new_lst[1]:
        return new_lst[0]
    else:
        for i in range(ord(new_lst[0]), ord(new_lst[1])+1):
            new_str+=chr(i)
        return new_str


print(gimme_the_letters("a-z"))
print(gimme_the_letters("h-o"))
print(gimme_the_letters("Q-Z"))
print(gimme_the_letters("J-J"))