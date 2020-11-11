'''Write a function that takes a list and returns a new list with unique positive
    (more than 0) numbers.
    
    Note:-
    .Return the elements in the order that they are found in the list.
    .Your function should also work for empty list.'''

def unique_lst(lst):
    new_lst = []
    for i in lst:
        if i > 0:
            if i not in new_lst:
                new_lst.append(i)
    return new_lst

print(unique_lst([-5, 1, -7, -5, -2, 3, 3, -5, -1, -1]))
print(unique_lst([3, -3, -3, 5, 5, -6, -2, -4, -1, 3]))
print(unique_lst([-5, 3, 2, -4, 3, -1, -7, 2, 4, 4]))