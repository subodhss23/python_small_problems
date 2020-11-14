'''Write a function that retrives the last n elements from a list.'''

def last(a, n):
    if n > len(a):
        return 'invalid'
    elif n == 0:
        return []
    else:
        return a[-n:]

print(last([1, 2, 3, 4, 5], 1))
print(last([4, 3, 9, 9, 7, 6], 3))
print(last([1, 2, 3, 4, 5], 7))
print(last([1, 2, 3, 4, 5], 0))