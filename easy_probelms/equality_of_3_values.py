''' Create a function that takes three integer argument (a,b,c) and returns 
    the amount of integers which are of equal value.'''

def equal(a,b,c):
    lst = [a,b,c]
    new_set = set(lst)
    if len(new_set) == 3:
        return 0
    elif len(new_set) == 2:
        return 2
    elif len(new_set) == 1:
        return 3

print(equal(3, 4, 3))
print(equal(1, 1, 1) )
print(equal(3, 4, 1))