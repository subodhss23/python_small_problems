''' Create a function that returns "even" if a nubmer has an even number of factors
    and "odd" if a number has an odd number of factors.'''

def factor_group(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count+=1
    if count % 2 == 0:
        return 'even'
    return 'odd'


print(factor_group(33))
print(factor_group(36))
print(factor_group(7))
