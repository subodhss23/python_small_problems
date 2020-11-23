''' Given two unique integer lists a and b, and an integer target value v, create a function to determine
    whether there is a pair of numbers that add up to the target value v, where one number comes from one list
    a and the other comes from the second list b.
    
    Return True if there is a pair that adds up to the target value and False otherwise.
'''

def sum_of_two(a, b, v):
    sum = 0
    for i in a:
        for j in b:
            if i + j == v:
                return True
    return False

print(sum_of_two([1, 2], [4, 5, 6], 5))
print(sum_of_two([1, 2], [4, 5, 6], 8))
print(sum_of_two([1, 2], [4, 5, 6], 3))
print(sum_of_two([1, 2], [4, 5, 6], 9))