''' create a function that return the minimum number of elements removed
    to make the sum of all elements in a list even. '''


def minimum_removals(lst):
    if sum(lst) % 2 == 0:
        return 0
    else:
        return 1

print(minimum_removals([1, 2, 3, 4, 5]))
print(minimum_removals([5, 7, 9, 11]))
print(minimum_removals([5, 7, 9, 12]))