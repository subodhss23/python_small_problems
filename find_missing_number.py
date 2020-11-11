''' Create a function that takes a list of nubmers between 1 and 10 (excluding one number)
    and returns the missing nubmer.'''

def missing_num(lst):
    missing_num = 0
    for i in range(1, 11):
        if i not in lst:
            missing_num = i
    return missing_num

print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))
print(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]))
print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]))
