''' Create a function that takes a list of numbers and returns the sum of all prime numbers in the list.'''

def sum_primes(lst):
    sum = 0
    for i in lst:
        c = 0
        for j in range(1, i):
            print('this is i and j', i, j)
            if i%j == 0:
                c+=1
                print('this is c ',c)
        if c == 1:
            sum+=i
    if sum== 0:
        return None
    return sum

print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(sum_primes([2, 3, 4, 11, 20, 50, 71]))
# print(sum_primes([]))