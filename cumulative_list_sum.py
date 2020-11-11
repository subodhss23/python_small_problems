''' Create a function that takes a list of numbers and returns a list where each
    number is the sum of itself + all previous numbers in the list. '''

def cumulative_sum(lst):
    new_lst = []
    sum = 0
    for i in lst:
        sum+= i
        new_lst.append(sum)
    return new_lst


print(cumulative_sum([1,2,3]))
print(cumulative_sum([1, -2, 3]))
print(cumulative_sum([3, 3, -2, 408, 3, 3]))