''' Create a function which takes in a word and spells it out, by consecutively
    adding letters until the full word is completed.'''

def spelling(txt):
    new_lst = []
    new_str = ""
    for i in txt:
       new_str+=i
       new_lst.append(new_str)
    return new_lst


print(spelling("bee"))
print(spelling("happy"))
print(spelling("eagerly"))