''' Create a function that takes a list of integers and strings. Convert integers to strings and return the
    new list.'''

def parse_list(lst):
    new_lst = []
    for i in lst:
        if type(i) == int:
            new_lst.append(str(i))
        else:
            new_lst.append(i)
    return new_lst

print(parse_list([1, 2, "a", "b"]))
print(parse_list(["abc", 123, "def", 456]))
print(parse_list([1, 2, 3, 17, 24, 3, "a", "123b"]))
print(parse_list([]))