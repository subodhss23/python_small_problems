# negates numbers in list

def negate(lst):
    new_lst = []
    for i in lst:
        new_lst.append(-i)
    return new_lst


print(negate([1, 2, 3, 4]))
print(negate([-1, 2, -3, 4]))
print([])