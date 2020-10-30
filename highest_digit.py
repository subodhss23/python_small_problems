''' Create a function that takes a number as an argement
    and returns the highest digit in that number.'''

# def highest_digit(num):
#     new_str = str(num)
#     new_list = []
#     for i in new_str:
#         new_list.append(i)
#     return max(new_list)

# def highest_digit(num):
#     new_str = str(num)
#     new_lst = list(new_str)
#     return max(new_lst)

def highest_digit(num):
    return int(max(str(num)))

print(highest_digit(379))
print(highest_digit(2))
print(highest_digit(377401))