''' Write a function that takes a two-digit number and determines if it's the
    largest of two possible digit swaps. '''

def largest_swap(num):
    new_num = str(num)[::-1]
    return int(new_num) <= num

print(largest_swap(14))
print(largest_swap(53)) 
print(largest_swap(99))