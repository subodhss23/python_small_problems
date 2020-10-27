''' create a function that returns the next element in an arithmetic sequence.
    In an arithmetic sequence, each element is formed by adding the same constant
    to the previous element. '''

def next_element(lst):
    return lst[-1] + (lst[1] - lst[0])

print(next_element([3, 5, 7, 9]))
print(next_element([-5, -6, -7])
print(next_element([2, 2, 2, 2, 2])
