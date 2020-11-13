''' Write a function that searches a list of names(unsorted) for the name
    "Bob" and returns the location in the list. If Bob is not in the list,
    return -1.'''

def find_bob(lst):
    if "Bob" in lst:
        return lst.index('Bob')
    else:
        return -1

print(find_bob(["Jimmy", "Layla", "Bob"]))
print(find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"]))
print(find_bob(["Jimmy", "Layla", "James"]))