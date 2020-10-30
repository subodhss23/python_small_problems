# given a string of letters, how many capital letters are there?

def capital_letters(txt):
    counter = 0
    for i in txt:
        if i.isupper():
            counter+=1
    return counter


print(capital_letters("fvLzpxmgXSDrobbgMVrc"))