''' Write a function that partitions the list into two sublists: one with all even
    integers, and the other with all odd integers. Return your result in the following
    format:'''

def even_odd_partition(lst):
    even_lst = []
    odd_lst = []
    for i in lst:
        if i % 2 == 0:
            even_lst.append(i)
        elif i % 2 != 0:
            odd_lst.append(i)
    return [even_lst, odd_lst]

print(even_odd_partition([5, 8, 9, 2, 0]))
print(even_odd_partition([1, 0, 1, 0, 1, 0]))
print(even_odd_partition([1, 3, 5, 7, 9]))
print(even_odd_partition([]))