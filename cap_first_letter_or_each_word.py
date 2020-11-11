''' Create a function that takes a string as an arguement and converts
    the first character of each word to uppercase. Return the newly 
    formatted string. '''

def make_title(txt):
    new_str = ''
    new_lst = txt.split(' ')
    print(new_lst)
    for i in new_lst:
        if i != new_lst[-1]:
            new_str = new_str + i[0].title() + i[1:] + ' '
        elif i == new_lst[-1]:
            new_str = new_str + i[0].title() + i[1:]
    return new_str


print(make_title("This is a Title"))
print(make_title("capitalize every word"))
print(make_title("I Like Pizza"))
print(make_title("PIZZA PIZZA PIZZA"))