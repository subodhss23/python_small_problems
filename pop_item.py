''' suppose I want to define a function that removes the last element of a list
    each time I call it, but does not mutate the original list. Fix the code so that
    the results are no longer mutaing the list.'''


def minus_one(lst):
    arr = lst.copy()
    arr.pop()
    return arr

print(minus_one([1,2,3,4,5]))