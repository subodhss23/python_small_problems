 # Given a list, transform it into a mirror.

def mirror(lst):
    return lst[:-1] + lst[::-1]

print(mirror([0, 2, 4, 6]))