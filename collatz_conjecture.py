''' Consider the following operation on an arbitrary positive integer:
    - If n is even -> n / 2
    - If n is odd -> n * 3 + 1

    Create a function to repeatedly evaluate these operations, until reaching 1.
    Return the number of steps it took.

    See the follwing example, using 10 as the input, with 6 steps:

    1. 10 is even - 10 / 2 = 5
    2. 5 is odd - 5 * 3 + 1 = 16
    3. 16 is even - 16 / 2 = 8
    4. 8 is even - 8 / 2 = 4
    5. 4 is even - 4 /2 = 2
    6. 2 is even - 2 / 2 = 1 -> Reached 1m so return 6'''

def collatz(n):
    count = 0
    while n > 1:
        # print(n)
        if n % 2 == 0:
            n = n / 2
            count+=1
        elif n % 2 != 0:
            n = n * 3 + 1
            count+=1
    return count
    


print(collatz(2))
print(collatz(3))
print(collatz(10))