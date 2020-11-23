''' Create a function that takes a list of nubmers and return its median. If the input list is even length,
    take the average of the two medians, else, take the single median. '''


def median(lst):
    mid = len(lst) // 2
    lst_sorted = sorted(lst)
    if len(lst) % 2 == 0:
        return round((lst_sorted[mid-1] + lst_sorted[mid])/2, 1)
    else:
        return lst_sorted[mid]



# print(median([2, 5, 6, 2, 6, 3, 4]))
# print(median([21.4323, 432.54, 432.3, 542.4567]))
# print(median([-23, -43, -29, -53, -67]))

print(median([342, 98, 5456, 32, 786, 432, 890, 321]))