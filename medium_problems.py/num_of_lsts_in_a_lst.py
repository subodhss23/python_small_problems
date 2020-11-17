# Return the total number of lists inside a given list.

def num_of_sublists(lst):
    count = 0
    for i in lst:
        if type(i) == type([]):
            count+=1
    return count


print(num_of_sublists([[1, 2, 3]]))
print(num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) )
print(num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]))
print(num_of_sublists([1, 2, 3]))