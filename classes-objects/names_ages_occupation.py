''' Write a function that maps a string into a dictionary of name, string, and 
    occupation pairs.'''


def organize(txt):
    new_obj = {}
    new_lst = txt.split(',')
    new_obj["name"] = new_lst[0].strip(' ')
    new_obj["age"] = new_lst[1].strip(' ')
    new_obj["occupation"] = new_lst[2].strip(' ')
    return new_obj


def organize_b(s):
    if not s:
        return {}
    d = dict(zip(('name', 'age', 'occupation'), s.split(', ')))
    d['age'] = int(d['age'])
    return d


print(organize("Jameel Saeb, 15, CEO of facebook"))
print(organize_b("John Mayer, 41, Singer, Emily Blunt, 36, Actor"))
