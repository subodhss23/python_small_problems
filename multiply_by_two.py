''' create a function that takes a list with numbers and return a list with
    the lements multiplied by two. '''

def get_multiplied_list(lst):
    new_lst = []
    for i in lst:
        i*=2
        new_lst.append(i)
    return new_lst

print(get_multiplied_list([2, 5, 3]))
print(get_multiplied_list([1, 86, -5]))
print(get_multiplied_list([5, 382, 0]))