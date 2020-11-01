# given a string of numbers separated by a comma and space, return the total of all the numbers.

def add_nums(nums):
    new_lst = nums.split(',')
    sum = 0
    for i in new_lst:
        sum += int(i)
    return sum        

print(add_nums("2, 5, 1, 8, 4"))
# print(add_nums("1, 2, 3, 4, 5, 6, 7"))
# print(add_nums("10") )