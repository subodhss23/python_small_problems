'''Create a function which takes in a list of number and a number to find. Return
    the sum of every index in the list which matches the chosen number.'''

def sum_found_indexes(lst,n):
    new_lst = []
    for i in range(len(lst)):
        if lst[i] == n:
            new_lst.append(i)
    return sum(new_lst)
    # indices = [i for i, x in enumerate(lst) if x == n]
    # return sum(indices)

  

print(sum_found_indexes([0, 3, 3, 0, 0, 3], 3))
print(sum_found_indexes([1, 2, 3, 4, 5, 6], 3))
print(sum_found_indexes([100, 100, 100, 100, 100], 100))
print(sum_found_indexes([5, 10, 15, 20], 2) )