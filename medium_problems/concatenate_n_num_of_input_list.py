# create a function that concatenates n input lists, where n is variable.

def concat(*args):
    new_lst = []
    for i in range(len(args)):
        new_lst += args[i]
    return new_lst

print(concat([1, 2, 3], [4, 5], [6, 7]))
print(concat([1], [2], [3], [4], [5], [6], [7]))
print(concat([1, 2], [3, 4]))
print(concat([4, 4, 4, 4, 4]))
