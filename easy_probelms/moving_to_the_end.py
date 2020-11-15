''' Write a function that moves all elements of one type to the end of the list.'''

def move_to_end(lst, el):
    new_lst = []
    lst_two = []
    for i in lst:
        if i != el:
            new_lst.append(i)
        else:
            lst_two.append(i)
    return new_lst + lst_two

print(move_to_end([1, 3, 2, 4, 4, 1], 1))
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))
print(move_to_end(["a", "a", "a", "b"], "a"))


