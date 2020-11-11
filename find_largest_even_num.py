''' Write a function that finds the largest even number in a list. Return -1 
    if not found. The use of build-in function max() and sorted() are prohibited.
'''

def largest_even(lst):
    res = -1
    for x in lst:
        if not x % 2 and x > res:
            res = x
    return res

print(largest_even([3, 7, 2, 1, 7, 9, 10, 13]))
print(largest_even([1,3,5,7]))
print(largest_even([0,19,18984350]))