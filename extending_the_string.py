''' make two functions:
1. consonants(word) which returns the number of consonants in a word when
called.
2. vowels(word) which return the number of vowels in a word when called.
'''


def consonants(word):
    counter = 0
    for i in word:
        if i.lower() in 'bcdfghjklmnpqrstvwxyz':
            counter += 1
    return counter



def vowels(word):
    counter = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    for i in word:
        if i.lower() in vowel:
            counter += 1
    return counter 

print(consonants('Jameel SAEB'))
print(consonants('Peter PANS'))
#print(vowels('Jameel SAEB'))
#print(vowels('Smithsonian'))
