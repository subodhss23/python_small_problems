# create a function that takes a list and finds the integer which appears an odd number of times.


def find_odd(lst):
    counter = 0
    new_set = set(lst)
    for i in new_set:
        counter = (lst.count(i))
        if counter % 2 != 0:
            return i



print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
# print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
# print(find_odd([10]))