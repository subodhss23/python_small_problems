'''Create a function that takes a list and returns a new list containing only prime numbers. '''

import time 
start = time.process_time()
def filter_primes(num):
    new_lst = []
    prime_lst = []
    for i in (num):
        for j in range(2, i+1):
            if i % j == 0:
                new_lst.append(i)
    for i in new_lst:
        if new_lst.count(i) == 1:
            prime_lst.append(i)
    return prime_lst
print(time.process_time() - start)


print(filter_primes([7, 9, 3, 9, 10, 11, 27]))
print(filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]))