# given a list and an integer n, return the sum of the first n numbers in the list.

def sum_first_n_nums(lst, n):
    total = 0
    i = 0
    if n <= len(lst):
        while(i < n):
            total = total + lst[i]
            i += 1
    else:
        while(i < len(lst)):
            total = total + lst[i]
            i+= 1
    return total



print(sum_first_n_nums([1, 3, 2], 2))
print(sum_first_n_nums([4, 2, 5, 7], 4))
print(sum_first_n_nums([3, 6, 2], 0))