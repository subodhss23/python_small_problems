''' A salesman has a number of cities to visit. They want to calcualte the total 
    number of possible paths they could take, visiting each city once before
    returning home. Return the total number of possible paths a salesman can travel,
    given n cities.

    If we have cities A, B and C, possible paths would be: 6
'''

# def path(n):
#     if n == 0 or n == 1:
#         return n
#     return n * path(n -1)

def path(n):
    factorial = 1
    if n == 0:
        return 1
    else:
        fact = 1
        while n > 1:
            fact *= n
            n-=1
        return fact

print(path(4))
print(path(1))
print(path(0))
print(path(9))