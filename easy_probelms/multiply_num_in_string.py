'''Given a string of nubmers separated by a comma and space, return the product of the nubmers.'''

def multiply_nums(nums):
    new_lst = nums.split(',')
    product = 1
    for i in new_lst:
        product *= int(i)
    return product

print(multiply_nums("2, 3"))
print(multiply_nums("1, 2, 3, 4"))
print(multiply_nums("54, 75, 453, 0"))
print(multiply_nums("10, -2"))