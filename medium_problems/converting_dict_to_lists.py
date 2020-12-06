''' Write a function that converts a dictionary into a list, where each element represents a key-value pair
    in the form of a list. Sort the list alphabetically be key.'''

def to_list(dct):
    new_lst = []
    for i in dict.keys(dct):
        new_lst.append([i, dct[i]])
    return sorted(new_lst)

print(to_list({ "a": 1, "b": 2 }))
print(to_list({ "shrimp": 15, "tots": 12 }))
print(to_list({}))