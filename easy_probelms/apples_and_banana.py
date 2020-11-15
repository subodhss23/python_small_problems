''' Write a function, that replaces all vowels in a sting with a specified vowel.'''

def vow_replace(word, vowel):
    vowel_const = 'aeiou'
    new_str = ''
    for i in word:
        if i in vowel_const:
            i = vowel
            new_str+=i
        else:
            new_str+=i
    return new_str

print(vow_replace("apples and bananas", "u"))
print(vow_replace("cheese casserole", "o"))
print(vow_replace("stuffed jalapeno poppers", "e"))