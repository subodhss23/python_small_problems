'''Create a function that takes a list of items, removes all duplicates items
    and returns a new list in the same sequential order as the old list(minus
    duplicates).'''


def remove_dups(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst

print(remove_dups([1, 0, 1, 0]) )
print(remove_dups(["The", "big", "cat"]))
print(remove_dups(["John", "Taylor", "John"]) )