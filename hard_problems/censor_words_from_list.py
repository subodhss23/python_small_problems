''' Create a function that takes a string txt and censors any word from a given list lst. The text
    retmoved must be replaced by the given character char.'''

def censor_string(txt, lst, char):
    txt_lst = txt.split(' ')
    new_lst = []
    for i in txt_lst:
        if i in lst:
            i = char*len(i)
            new_lst.append(i)
        else:
            new_lst.append(i)
    return (' ').join(new_lst)

print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))
print(censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*"))