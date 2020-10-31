''' given a list of 10 numbers, return the maximum possible total made by summing just 5 of the 10 number '''

def max_total(nums):
    sorted_nums = sorted(nums)
    return sum(sorted_nums[5:])

print(max_total([1, 1, 0, 1, 3, 10, 10, 10, 10, 1]))
print(max_total([0, 0, 0, 0, 0, 0, 0, 0, 0, 100]))
print(max_total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))