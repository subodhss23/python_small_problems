''' Write a function that takes three arguments (x, y, z) and returns a list containing
    x sublists (e.g. [[], [], []]), each containing y number of item z.

    - x Number of sublists contained within the main list.
    - y Number of items contained within each sublist.
    - z Item contained within each sublist. '''


def matrix(x, y, z):
    new_lst = []
    for i in range(x):
        new_lst.append([z]*y)
    return new_lst



print(matrix(3, 2, 3))
print(matrix(2, 1, "edabit"))
print(matrix(3, 2, 0))