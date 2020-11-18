''' Write a function that takes a positive integer and calculates how many dots exist in a pentagonal
    shape around the center dot on the Nth iteration.

    In the image below you can see the first iteration is only a single dot. On the second, there are 6 dots.
    On the third, there are 16 dots, and on the fourth there are 31 dots.
    
    Return the number of dots that exist in the whole pentagon on the Nth iteration.
    '''

def pentagonal(num):
    return (5 * num ** 2 - 5 * num + 2)/2


print(pentagonal(1))
print(pentagonal(2))
print(pentagonal(3))
print(pentagonal(8))