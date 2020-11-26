''' A fulcrum of a list is an integer such that all elements to the left of it and all
    elements to the right of it sum to the same value. Write a function that finds 
    the fulcrum of a list. '''


def find_fulcrum(lst):
	s = sum(lst)
	running = 0
	for i in lst:
		if running == (s-i)//2:
			return i
		running += i
	return -1

print(find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3]))
print(find_fulcrum([9, 1, 9]))
print(find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3]))
print(find_fulcrum([8, 8, 8, 8]))