''' Create a function that finds a target number in a list of prime numbers.
    Implement a binary search algorithm in your function. The target number 
    will be from 2 through 97. If the target is prime then return "yes" else 
    return "no".'''


def is_prime(primes,num, left=0, right=None):
    right = len(primes)-1
    while left <= right:
        middle = left+(right-left)//2
        print(middle)
        if primes[middle] == num:
            return 'yes'
        elif primes[middle]>num:
            right=middle - 1
        else:
            left=middle+1
    return 'no'



primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print(is_prime(primes, 3))
# print(is_prime(primes, 4))
# print(is_prime(primes, 67))
# print(is_prime(primes, 36))