''' Given a list of numbers, create a function that remove 25% from every number
    in the list except the small number, and adds the total amount remoed to the
    smallest number. '''

def show_the_love(lst):
	m = min(lst)
	mi = lst.index(m)
	a = 0
	for i in range(len(lst)):
		if lst[i] != m:
			a += .25*lst[i]
			lst[i] = .75*lst[i]
	lst[mi] += a
	return lst

print(show_the_love([4, 1, 4]))
print(show_the_love([16, 10, 8]))
print(show_the_love([2, 100]))
print(show_the_love([2, 100]))