''' Given a number, return the difference between the maximum and minmum nubmers that can be
    formed when the digits are rearranged.'''

def rearranged_difference(num):
    new_lst = list(str(num))
    asscending = (sorted(new_lst))
    descending = (sorted(new_lst, reverse=True))
    return int(('').join(descending)) - int(('').join(asscending))

print(rearranged_difference(972882))
print(rearranged_difference(3320707))
print(rearranged_difference(90010))