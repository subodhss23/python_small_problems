'''Create a function that flips a horizonal list into a vertical list, and vertical list into a horizonal list.

    In other words, take an 1 x n (1 row + n columns) and flip it into a n x 1 list(n rows and 1 column),
    and vice versa.'''

def flip_list(lst):
    new_lst = []
    if lst == []:
        return lst
    elif type(lst[0]) == int:
        for i in lst:
            new_lst.append([i])
        return new_lst
    elif type(lst[0]) == list:
        for i in lst:
            for j in i:
                new_lst.append(j)
        return new_lst


print(flip_list([1, 2, 3, 4]))
print(flip_list([[5], [6], [9]]))