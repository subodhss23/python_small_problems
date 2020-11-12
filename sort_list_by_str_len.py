''' Create a function that takes a list of strings and return a list,
    sorted from shortest to longest.'''

def sort_by_length(lst):
    lst.sort(key=len)
    return lst

print(sort_by_length(["Google", "Apple", "Microsoft"]))
print(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]))
print(sort_by_length(["Turing", "Einstein", "Jung"]))