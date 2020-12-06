''' Create a function that tests whether or not an integer is a perfect number. A perfect number
    is a number that can be written as a sum of its factors, excluding the number itself.

    For example, 6 is a perfect number, since 1+2+3=6, where 1,2 and 3 are all factors
    of 6. Similarly, 28 is a perfect number, since 1+2+4+7+14=28'''

def check_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum+=i
    return sum == num

print(check_perfect(6))
print(check_perfect(28))
print(check_perfect(496))
print(check_perfect(12))
print(check_perfect(97))