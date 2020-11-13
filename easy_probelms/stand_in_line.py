''' Write a function that takes a list and a number as arguments. Add the nubmer
    to the end of the list, then remove the first element of the list. The function
    should then return the updated list. '''

# def next_in_line(lst, num):
#     if lst == []:
#         return 'No list has been selected'
#     else:
#         lst.append(num)
#         return lst[1:]


def next_in_line(lst, num):
    if lst == []:
        return 'No list has been selected'
    else:
        lst.append(num)
        lst.pop(0)
        return lst

print(next_in_line([5, 6, 7, 8, 9], 1))