''' Create a function that replaces all the vowels in a string with
    a specified character. '''

def replace_vowels(txt, ch):
    new_str = ''
    vowel = 'aeiou'
    for i in txt:
        if i in vowel:
            new_str+=ch
        else:
            new_str+=i
    return new_str

print(replace_vowels("the aardvark", "#"))
print(replace_vowels("minnie mouse", "?"))
print(replace_vowels("shakespeare", "*"))