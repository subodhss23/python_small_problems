# create a function that return the index of the first vowel in a string.


def first_vowel(txt):
    lower_txt = txt.lower()
    vowel = 'aeiou'
    for i in lower_txt:
        if i in vowel:
            return lower_txt.index(i)

print(first_vowel("hello"))
print(first_vowel("STRAWBERRY"))
print(first_vowel("pInEaPPLe"))
