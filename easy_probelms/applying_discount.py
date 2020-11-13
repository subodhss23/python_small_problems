''' Create a function that applies a discount d to every number in the list.'''


# def get_discounts(nums, d):
# 	new_lst = []
# 	percent = 0
# 	if len(d) == 3:
# 		percent = d[0] + d[1]
# 	elif len(d) == 2:
# 		percent = d[0]
# 	for i in nums:
# 		new_lst.append(i * int(percent)/100)
# 	return new_lst

def get_discounts(nums, d):
    discount = int(d.strip('%')) / 100
    new_price = []
    for i in nums:
        new_price.append(i * discount)
    return new_price

print(get_discounts([2, 4, 6, 11], "50%") )
print(get_discounts([100], "45%"))
# print(get_discounts([20], "1%"))
