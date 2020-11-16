'''Given a list of nubmers, return a list which contains all the even
    numbers in the original list, which also have even incices.'''

def get_only_evens(lst):
    new_lst = []
    for i in lst:
        if i % 2 == 0 and lst.index(i) % 2 == 0:
            if i not in new_lst:
                new_lst.append(i)
    return new_lst


# def get_only_evens(nums):
# 	l = []
# 	for n in range(0, len(nums)):
# 		if n % 2 == 0 and nums[n] % 2 == 0:
# 			l.append(nums[n])
# 	return l

print(get_only_evens([1, 3, 2, 6, 4, 8]))
print(get_only_evens([0, 1, 2, 3, 4]))
print(get_only_evens([1, 2, 3, 4, 5]))
print(get_only_evens([47, 31, 24, 37, 29, 41, 31, 49, 4, 24]))