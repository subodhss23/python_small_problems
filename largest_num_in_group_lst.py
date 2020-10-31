''' create a function that takes a list of lists with integers or floats.
    Return a new(single) list with the largest numbers from each. '''

def findLargestNums(lst):
    new_lst = []
    temp = 0
    for i in lst:
        new_lst.append(max(i))
    return new_lst

print(findLargestNums([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]]))