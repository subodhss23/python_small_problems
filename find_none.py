''' create a function to find None in a list of numbers. The return value should be the index
where None is found. If None is not found in the list, then return -1'''

def find_none(lst):
    if None  in lst:
        print('found')
        return lst.index(None)
    else:
        return -1

print(find_none([1,2, None]))
print(find_none([None, 1, 2, 3, 4]))
print(find_none([0,1,2,3,4]))
