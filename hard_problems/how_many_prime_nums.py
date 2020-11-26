'''Create a function that tinds how many prime numbers there are, up to the given integer. '''

def prime_numbers(num):
    count = 0
    prime_list = []
    for i in range(2,10+1):
        for j in range(1, i+1):
            if i % j == 0:
                prime_list.count(j)
    return prime_list

print(prime_numbers(10))
print(prime_numbers(20))
print(prime_numbers(30))