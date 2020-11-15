''' Write a function that takes a sting, breaks it up and returns it with vowels
    first, consonants second. For any character that's not a vowel (like special
    characters or spaces), treat them like consonants.'''

def split(txt):
    vowel = 'aeiou'
    vowel_str = ''
    cons_str = ''
    for i in txt:
        if i in vowel:
            vowel_str+=i
        else:
            cons_str+=i
    return vowel_str+cons_str


print(split("abcde"))
print(split("Hello!"))
print(split("What's the time?"))