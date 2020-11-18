''' Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive
    sequence is a sequence without any gaps in the integer, e.g. 1,2,3,4,5 is a consecutive sequence, but 1,2,3,4,5
    is not.'''


def consecutive_combo(lst1, lst2):
    new_lst = sorted(lst1 + lst2)
    test_lst = []
    for i in range(new_lst[0], new_lst[-1]+1):
        test_lst.append(i)
    return new_lst == test_lst

    # lst3 = lst1 + lst2
    # return max(lst3) - min(lst3) == len(lst3) - 1


print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
# print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
# print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
# print(consecutive_combo([44, 46], [45]))
