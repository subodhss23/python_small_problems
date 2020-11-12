'''Create afunction that takes in an array and returns True if all its values
    are even, and False otherwise.'''

def check_all_even(lst):
    for i in lst:
        if i % 2 != 0:
            return False
    return True


print(check_all_even([1, 2, 3, 4]))
print(check_all_even([2, 4, 6]))
print(check_all_even([5, 6, 8, 10]))
print(check_all_even([-2, 2, -2, 2]))