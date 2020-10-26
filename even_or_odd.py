# given a string, return true if its length is even or false if the length is odd.


def odd_or_even(words):
    counter = 0
    for i in words:
        counter += 1
    return counter % 2 == 0

print(odd_or_even('apples'))
print(odd_or_even('pears'))
print(odd_or_even('cherry'))