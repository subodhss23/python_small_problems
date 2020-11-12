''' Write two functions:
    1. to_list(), which converts a number to an integer list of its digits.
    2. to_number(), which converts a list of integers back to its number.
'''

def to_list(num):
    new_str = str(num)
    new_lst = []
    for i in new_str:
        new_lst.append(int(i))
    return new_lst

def to_number(lst):
    new_str = ''
    for i in lst:
        new_str+= str(i)
    return int(new_str)        

print(to_list(235))
print(to_list(0))
print(to_number([2, 3, 5]))
print(to_number([0]))