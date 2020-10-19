# create a functiont hat takes a list and a string as arguments and return 
# the index of the string.


def find_index(lst, txt):
    for i in lst:
        if i == txt:
            return lst.index(i)


print(find_index([1,2,3,4,5], 4))
print(find_index(['aa', 'bc', 'bb', 'bd', 'ee'], 'bb'))