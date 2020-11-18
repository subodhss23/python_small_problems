''' Write a function that returns the greatest common divisor of all list elements. If the greatest common
    divisor is 1, return 1.'''


def GCD(lst):
    result = lst[0]
    for x in lst[1:]:
        if result < x:
            temp = result
            result = x
            x = temp
        while x != 0:
            temp = x
            x = result % x
            result = temp
    return result


print(GCD([10, 20, 40]))
print(GCD([1, 2, 3, 100]))
print(GCD([1024, 192, 2048, 512]))