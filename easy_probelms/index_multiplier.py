'''Return the sum of all items in a list, where each item is multiplied by its
    index(zero-based). for empty lists, return 0.'''

def index_multiplier(lst):
    sum = 0
    for i in range(len(lst)):
        sum += i *lst[i]
    return sum

# print(index_multiplier([1, 2, 3, 4, 5]))
# print(index_multiplier([-3, 0, 8, -6]))
print(index_multiplier([1,1,2,3,4]))