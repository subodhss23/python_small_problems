''' write a function that takes the last number of a consecutive list of nubmers
    and returns the totla of all nubmer up to and including it.'''


def add_up_to(n):
    sum = 0
    for i in range(0, n + 1):
        sum += i
    return sum

print(add_up_to(3))
# print(add_up_to(10))
# print(add_up_to(7))
