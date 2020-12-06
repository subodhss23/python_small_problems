''' Write a function that transform a list of characters into a list of dictionaries,
    where:
    1. The keys are the characters themselves.
    2. The values are the ASCII codes of those characters.
'''

def to_dict(lst):
    new_lst = []
    for i in lst:
        result ={}
        result.update({i: ord(i)})
        new_lst.append(result)
    return new_lst


print(to_dict(["a", "b", "c"]))
print(to_dict(["^"]))