''' Write a function that finds the sum of the first n natrual numbers in recursive method'''

def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n-1)

print(sum_numbers(5))
print(sum_numbers(1))
print(sum_numbers(12))