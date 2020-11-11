''' There's a great war between the even and odd nubmers. Many numbers already lost
    their life in this war and it's your task to end this. You have to determine
    which group sums large: the even, or the odd. The large group wins.

    Create a function that takes a list of integers, sums the even and odd
    numbers separately, then return the difference between sum of even and odd
    numbers.'''


def war_of_numbers(lst):
    odd = 0
    even = 0
    for i in lst:
        if i % 2 == 0:
            even+=i
        else:
            odd+=i
    if even > odd:
        return even - odd
    return odd - even

print(war_of_numbers([2, 8, 7, 5]))
print(war_of_numbers([12, 90, 75]))
print(war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))