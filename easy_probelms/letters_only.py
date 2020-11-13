''' Write a function that removes any non-letters from a string,
    returning a well-known film title.'''

def letters_only(str):
    new_str = ''
    for i in str:
        if i.isalpha():
            new_str+=i
    return new_str

print(letters_only("R!=:~0o0./c&}9k`60=y"))
print(letters_only("^,]%4B|@56a![0{2m>b1&4i4"))
print(letters_only("^U)6$22>8p)."))