# create a function that returns True if the first list is a subset of the
# second. Return False otherwise

def is_subset(lst1, lst2):
	len_lst1 = len(lst1)
	counter = 0
	for i in lst2:
		for j in lst1:
			if i == j:
				counter += 1
	return counter == len_lst1


print(is_subset([3, 2, 5], [5, 3, 7, 9, 2]))
print(is_subset([8, 9], [7, 1, 9, 8, 4, 5, 6]))
print(is_subset([1, 2], [1, 2, 3]))
print(is_subset([0,1,2,3],[4,5,6,7]))

