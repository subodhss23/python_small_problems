''' Given an integer, create a function that returns the next prime. If the number is prime, return the number iteself.'''


def next_prime(num):
    new_lst = []
    temp = num

    for i in range(2, temp+1):
        for i in range(2, num):
            if i == num - 1:
                return num
            if num%i == 0:
                return next_prime(num+1)


print(next_prime(12))
print(next_prime(24))
print(next_prime(11))