''' The code tab has code which attempts to add a lcone of a list to itself.
    There is no error message, but the results are not as intended. Can you
    fix the code?'''

def clone(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i)
    lst.append(new_lst)
    return lst

print(clone([1,1]))

