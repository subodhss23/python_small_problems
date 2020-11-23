''' Write a function that finds the sum of a list. Make your function recursive. '''

def sum_recursively(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_recursively(lst[1:])


print(sum_recursively([1, 2, 3, 4]))