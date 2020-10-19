# create a function that counts the number of syllables a word has.
# Each syllable is separated with a dash -.

def number_syllables(word):
    counter = 0
    for i in word:
        if i == '-':
            print('found -')
            counter += 1
    return counter + 1


print(number_syllables("buf-fet"))
print(number_syllables("beau-ti-ful"))
