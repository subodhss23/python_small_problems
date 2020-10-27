# create a function that returns the number of hashes and pluses in a strin.

def hash_plus_count(txt):
    hash = 0
    plus = 0
    for i in txt:
        if i == '#':
            hash+=1
        elif i == '+':
            plus+=1
    return [hash, plus]

print(hash_plus_count("####"))
print(hash_plus_count("#"))
print(hash_plus_count("+++++++"))