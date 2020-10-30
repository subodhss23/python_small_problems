''' The goal is to measure the depth of this list, where [] has depth of 1,
    [[]] has depth of 2, [[[[]]]] has depth 3, etc. '''

def measure_the_depth(lst):
    counter = 0
    new_lst = str(lst)
    return new_lst.count("[")

print(measure_the_depth([]))
print(measure_the_depth([[]]))
print(measure_the_depth([[[]]]))


