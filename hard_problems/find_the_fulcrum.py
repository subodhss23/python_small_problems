''' A fulcrum of a list is an integer such that all elements to the left of it and all
    elements to the right of it sum to the same value. Write a function that finds 
    the fulcrum of a list. '''

import math
def find_fulcrum(lst):
    mid = math.ceil(len(lst)/2)
    for i in range(len(lst)):
        if sum(lst[:i]) == sum(lst[i:]):
            return sum(lst[:i])
    return -1

print(find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3]))
print(find_fulcrum([9, 1, 9]))
print(find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3]))
print(find_fulcrum([8, 8, 8, 8]))