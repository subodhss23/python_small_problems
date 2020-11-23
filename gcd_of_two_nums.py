''' Write a function that returns the greatest common divisor(GCD) of two number.'''

def gcd(n1, n2):
    new_lst = []
    minm = min(n1, n2)
    for i in range(1, minm+1):
        if n1  % i == 0 and n2 % i == 0:
            new_lst.append(i)
    return max(new_lst)


print(gcd(32, 8))
print(gcd(8, 12))
print(gcd(17, 13))