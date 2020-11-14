''' Create a function that returns a list of strings sorted by length in ascending order.'''

def sort_by_length(lst):
    return (sorted(lst, key=len))


print(sort_by_length(["a", "ccc", "dddd", "bb"]))
print(sort_by_length(["apple", "pie", "shortcake"]))
print(sort_by_length(["may", "april", "september", "august"]) )
print(sort_by_length([]))