''' Write a function that, given the start start_num and end end_num values,
    return a list containing all the numbers inclusive to that range. 
    
    Note:- if start_num is greater than end_num, return a list with higher value.
    '''

def inclusive_list(start_num, end_num):
	new_lst = []
	if start_num > end_num:
		return [start_num]
	else:
		for i in range(start_num, end_num+1):
			new_lst.append(i)
		return new_lst

print(inclusive_list(1,5))
print(inclusive_list(17,3))
print(inclusive_list(10, 50))
