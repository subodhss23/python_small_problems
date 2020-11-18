''' Given a list of words in the singular form, return a set of those words in the
    pularal form if they appear more than once in the list.'''

def pluralize(lst):
    new_lst = []
    for i in lst:
        if lst.count(i) > 1:
            new_lst.append(i + 's')
        else:
            new_lst.append(i)
    return set(new_lst)

print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))
print(pluralize(["chair", "pencil", "arm"]))