''' Create a function that takes a string and returns a new  string with each
    character accumulating by +1. Separate each set with a dash. '''

def accum(txt):
    lst = []
    for i in range(len(txt)):
        lst.append(txt[i].capitalize() +txt[i].lower() * i)
    new_txt = "-".join(lst)
    return new_txt

print(accum('abcd'))
print(accum("RqaEzty"))
print(accum("cwAt"))