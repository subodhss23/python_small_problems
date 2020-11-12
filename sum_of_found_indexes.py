'''Create a function which takes in a list of number and a number to find. Return
    the sum of every index in the list which matches the chosen number.'''

def sum_found_indexes(lst,n):
    sum = 0
    indexes_lst = []
    for i in lst:
        if i == n:
            indexes_lst.append(lst.index(i))
    return indexes_lst
  

print(sum_found_indexes([0, 3, 3, 0, 0, 3], 3))
# print(sum_found_indexes([1, 2, 3, 4, 5, 6], 3))
# print(sum_found_indexes([100, 100, 100, 100, 100], 100))
# print(sum_found_indexes([5, 10, 15, 20], 2) )