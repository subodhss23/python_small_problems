'''Create a function that takes a list of numbers and returns the sum
    of the two lowest positive numbers.'''


def sum_two_smallest_nums(lst):
    sorted_lst = sorted(lst)
    new_lst = []
    for i in sorted_lst:
        if i > 0:
            new_lst.append(i)
    return new_lst[0] + new_lst[1]


print(sum_two_smallest_nums([19, 5, 42, 2, 77]))
print(sum_two_smallest_nums([10, 343445353, 3453445, 3453545353453]))
print(sum_two_smallest_nums([2, 9, 6, -1]))
print(sum_two_smallest_nums([879, 953, 694, -847, 342, 221, -91, -723, 791, -587]))
print(sum_two_smallest_nums([3683, 2902, 3951, -475, 1617, -2385]) )