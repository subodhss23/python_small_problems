''' A number added with its additive inverse equals zero. 
    Create a function that returns a list of additive inverses. '''

def additive_inverse(lst):
    new_lst = []
    for i in lst:
        new_lst.append(-i)
    return new_lst

print(additive_inverse([5, -7, 8, 3]))
print(additive_inverse([1, 1, 1, 1, 1]))
print(additive_inverse([-5, -25, 35]))