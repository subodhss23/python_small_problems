''' Create a function that takes three arguments a,b,c and returns the sum of the
    numbers that are evenly divided by c from the range a, b inclusive. '''

def evenly_divisible(a, b, c):
    sum = 0
    for i in range(a, b+1):
        if i % c == 0:
            sum += i
    return sum


print(evenly_divisible(1, 10, 20))
print(evenly_divisible(1, 10, 2))
print(evenly_divisible(1, 10, 3))