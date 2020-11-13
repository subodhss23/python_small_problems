''' Create a function that takes a list of nubemrs and return the nubmer
    that's unique.'''

# def unique(lst):
#     new_set = set(lst)
#     new_lst = []
#     for i in new_set:
#         new_lst.append(i)
#     if lst.count(new_lst[0]) > lst.count(new_lst[1]):
#         return new_lst[1]
#     return new_lst[0]


def unique(lst):
    for i in lst:
        if lst.count(i) == 1:
            return i
        


print(unique([3, 3, 3, 7, 3, 3]))
print(unique([0, 0, 0.77, 0, 0]))
print(unique([0, 1, 1, 1, 1, 1, 1, 1]))