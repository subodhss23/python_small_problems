# multiply 'o' with given number in a string
    # note :- if n is equal to or less than 1, return invalid

def googlify(n):
    if n > 1:
        return 'G' + 'o'*n + 'gle'
    else:
        return 'invalid'

print(googlify(10))
print(googlify(23))
print(googlify(2))
