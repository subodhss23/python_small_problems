''' Programmer Pete is trying to turn two lists inside one list into one without messing the order of the list
    nor the type and becuase he's pretty advanced he made it without blinking but I want you to make it too.'''

# def one_list(lst):
#     new_lst = []
#     for i in lst:
#         for j in range(len(i)):
#             new_lst.append(i[j])
#     return new_lst

# def one_list(lst):
#     return lst[0]+ lst[1]

def one_list(lst):
    return sum(lst, [])

print(one_list([[1, 2], [3, 4]]))
print(one_list([["a", "b"], ["c", "d"]]))
print(one_list([[True, False], [False, False]]))