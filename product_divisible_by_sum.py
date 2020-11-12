''' Write a function that returns True if the product of a list is divisible
    by the sum of that same list. Otherwise, return False.'''

def divisible(lst):
    product = 1
    sum = 0
    for i in lst:
        product*= i
        sum += i
    result = product / sum
    return result == round(result)

print(divisible([3,2,4,2]))
print(divisible([4,2,6]))
print(divisible([3,5,1]))