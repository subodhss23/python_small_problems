''' Create a function that takes a number num and returns its double fraction. Mathematically,
    the forumlas for double factorial are as follows:

    if num is even :
        num !! = num ( num - 2)( num - 4)( num - 6) ... (4)(2)

    if num is odd:
       num !! = num ( num - 2)(num - 4)(num - 6) ... (3)(1) 

    if num = 0 or num = -1, then num!!= 1 by convention.'''


def double_factorial(num):
    if num<=0:
        return 1
    else:
        return num * double_factorial(num-2)

print(double_factorial(0))
print(double_factorial(2))
print(double_factorial(9))
print(double_factorial(14))