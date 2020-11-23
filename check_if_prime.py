''' Create a function that returns True if a number is prime, and False otherwise. A prime number is any 
    positive integer that is evenly divisible by only two divisors: 1 and itself.

    the first ten prime numbers are:
    2,3,5,7,11,13,17,19,23,29'''

def is_prime(num):
    new_lst = []
    for i in range(1, num+1):
        new_lst.append(num/i)
    return new_lst

print(is_prime(31))
print(is_prime(18))
print(is_prime(11))