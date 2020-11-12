''' Something which is not true is false, but something which is not not true is true! Create
    a function where given n number of "not", evaluate whether it's True or False.'''

def not_not_not(n, b):
    result = b
    for i in range(n):
        result = not result
    return result

print(not_not_not(1, True))
print(not_not_not(2, False))
print(not_not_not(6, True))