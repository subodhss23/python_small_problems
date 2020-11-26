''' Given a list of integers, return the smallest positive integer not present in the list.

    Here is a representative example. Consider the list:
        [-2, 6, 4, 5, 7, -1, 7, 1, 3, 6, 6, -2, 9, 10, 2, 2]

    After reordering, the list becomes:
        [-2, -2, -1, 1, 2, 2, 3, 4, 5, 6, 6, 6, 7, 7, 9, 10]

    ... from which we see that the smallest missing positive integer is 8. '''

# def min_miss_pos(lst):
#     new_lst= sorted(lst)
#     if max(new_lst) == 0:
#         return 1
#     else:
#         for i in range(1, max(new_lst)):
#             if i not in new_lst:
#                 return i
#         return i + 2    # hack


def min_miss_pos(lst):
    i = 1
    while True:
        if not i in lst:
            return i
        i += 1

print(min_miss_pos([-2, 6, 4, 5, 7, -1, 1, 3, 6, -2, 9, 10, 2, 2]) )
# print(min_miss_pos([0, -4, -4, -1, -9, -4, -5, -2, -10, -7, -6, -3, -10, -9]))
# print(min_miss_pos([7, 6, 5, 4, 3, 2, 1]))