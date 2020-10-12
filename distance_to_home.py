''' you will be given a list, showing how far James travels away from his home
for each day. He may choose to travel towards or away from his house, so negative
values are to be expected. '''

# create a function which calculates how far James must walk to get back home


def distance_home(lst):
    sum = 0
    for i in lst:
        sum+=i
    if sum < 0:
        return - sum
    return sum

print(distance_home([2, 4, 2, 5]))
print(distance_home([-1, -4, -3, -2]))
print(distance_home([3, 4, -5, -2]))