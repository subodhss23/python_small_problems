''' Write a function that takes a list of two nubmers and determines if the sum of the digits in each number
    are equal to each other.'''

def is_equal(lst):
    one = str(lst[0])
    two = str(lst[1])
    one_result = 0
    two_result = 0
    for i in one:
        one_result+=int(i)
    for i in two:
        two_result+=int(i)
    return one_result == two_result

print(is_equal([105, 42]))
print(is_equal([21, 35]))
print(is_equal([0,0]))
