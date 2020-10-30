# create a function that finds the index of a given item.

def search(lst, item):
    for i in lst:
        if i == item:
            return lst.index(item)
    return -1

print(search([5,8,6,2], 2))