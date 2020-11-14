# create a function that takes  a list of integers and removes the smallest value.

def remove_smallest(lst):
    if lst == []:
        return []
    else:
        min_val = min(lst)
        lst.remove(min_val)
        return lst
    

print(remove_smallest([2,3,4,1]))
print(remove_smallest([5, 3, 2, 1, 4]))
print(remove_smallest([2, 2, 1, 2, 1]))