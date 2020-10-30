''' create a function which returns the total of all odd numbers
    up to and including n. n will be given as an odd number. '''

def add_odd_to_n(n):
    sum = 0
    for i in range(0, n+1):
        if i % 2 != 0:
            sum += i
    return sum


print(add_odd_to_n(1))
print(add_odd_to_n(3))