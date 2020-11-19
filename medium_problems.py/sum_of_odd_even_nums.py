''' Write a function that takes al ist of numbers and returns a list with two elements:

    1. The first element should be the sum of all even numbers in the list.
    2. The second element should be the sum of all odd numbers in the list.


'''

def sum_odd_and_even(lst):
    odd = 0
    even = 0
    for i in lst:
        if i % 2 == 0:
            even+=i
        else:
            odd+=i
    return [even, odd]

print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))
print(sum_odd_and_even([0, 0]))