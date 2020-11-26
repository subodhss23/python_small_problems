''' Write a function that pairs the first number in an array with the last, the second number with the second 
    to last, etc.'''


def pairs(lst):
    new_lst = []
    if len(lst) % 2 == 0:
        for i in range(len(lst)//2):
            new_lst.append([lst[i], lst[-i-1]])
        return new_lst
    else:
        for i in range(len(lst)//2):
            new_lst.append([lst[i], lst[-i-1]])
        new_lst.append([lst[len(lst)//2], lst[len(lst)//2]])
    return new_lst


print(pairs([1, 2, 3, 4, 5, 6, 7]))
print(pairs([1, 2, 3, 4, 5, 6]))
print(pairs([5, 9, 8, 1, 2]))
print(pairs([]))