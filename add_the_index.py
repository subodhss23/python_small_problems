# add element and its index in a new list

def add_indexes(lst):
    new_lst = []
    index = 0
    for i in lst:
        new_lst.append(i + index)
        index += 1
    return new_lst

print(add_indexes([0, 0, 0, 0, 0]))
print(add_indexes([1, 2, 3, 4, 5]))
print(add_indexes([5, 4, 3, 2, 1]))