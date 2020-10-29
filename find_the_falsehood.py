''' write a function that, given a list of values, returns the list of the
    values that are False '''

def find_the_falsehoods(lst):
    new_arr = []
    for i in lst:
        if bool(i) == False:
            new_arr.append(i)
    return new_arr

print(find_the_falsehoods([0, 1, 2, 3]))
print(find_the_falsehoods(["", "a", "ab"]))
print(find_the_falsehoods([]))