''' Write a function that returns True if there exists at least one number that is larger 
    than or equal to n.'''

def exists_higher(lst, n):
    for i in lst:
        if i >= n:
            return True
    return False

print(exists_higher([5, 3, 15, 22, 4], 10))
print(exists_higher([1, 2, 3, 4, 5], 8))
print(exists_higher([4, 3, 3, 3, 2, 2, 2], 4))
print(exists_higher([], 5) )