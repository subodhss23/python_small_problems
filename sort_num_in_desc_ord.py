''' Create a function that takes any non-negative number as an argument and returns it with its digits in 
descending order. Descending order is when you sort from highest to lowest.'''


def sort_descending(num):
    sorted_lst = sorted(str(num), reverse=True)
    result =  int(('').join(sorted_lst))
    return result

print(sort_descending(123))