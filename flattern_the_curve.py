# Given a list of integers, replace every number with the mean of all numbers.

def flatten_the_curve(lst):
    if lst == []:
        return []
    new_lst = []
    mean = sum(lst)/len(lst)
    for i in range(len(lst)):
        new_lst.append(round(mean, 1))
    return new_lst


print(flatten_the_curve([1, 2, 3, 4, 5]))
print(flatten_the_curve([0, 0, 0, 2, 7, 3]))
print(flatten_the_curve([4]))
print(flatten_the_curve([]))
print(flatten_the_curve([7, 4, 2, 1]))
print(flatten_the_curve([-13, 0, -18]))