''' Create a function which calculates how many numbers are missing from an ordered number line. The number line
    starts at the first value of the list, and increases by 1 to the end of the number line, ending at the last
    value of the list.'''

def how_many_missing(lst):
    count = 0
    if len(lst) < 1:
        return 0
    else:
        for i in range(lst[0], lst[-1]):
            if i not in lst:
                count+=1
        return count

print(how_many_missing([1, 3]))
print(how_many_missing([7, 10, 11, 12]))
print(how_many_missing([1, 3, 5, 7, 9, 11]))
print(how_many_missing([5, 6, 7, 8]))