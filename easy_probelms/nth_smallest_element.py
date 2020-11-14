''' Given an unsorted list, create a function that returns the nth smallest element(the smallest)
    element is the first smallest, the second smallest element is the second smallest, etc).'''

def nth_smallest(lst, n):
    if n <= len(lst):
        new_sorted = sorted(lst)
        return new_sorted[n-1]
    return None

print(nth_smallest([1, 3, 5, 7], 1))
print(nth_smallest([1, 3, 5, 7], 3))
print(nth_smallest([1, 3, 5, 7], 5))
print(nth_smallest([7, 3, 5, 1], 2))
print(nth_smallest([5, 4, 3, 2, 1, -3],1))