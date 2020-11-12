''' Create a function that filters out a list to include nubmers which only have
    a certain number of digits.'''

def filter_digit_length(lst, num):
    new_lst = []
    for i in lst:
        if len(str(i)) == num:
            new_lst.append(i)
    return new_lst


print(filter_digit_length([88, 232, 4, 9721, 555], 3))
print(filter_digit_length([2, 7, 8, 9, 1012], 1))
print(filter_digit_length([32, 88, 74, 91, 300, 4050], 1))
print(filter_digit_length([5, 6, 8, 9], 1))