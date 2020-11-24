''' Given a common phrase, return False if any individual word in the phrase contains duplicate letters.
    Return True otherwise. '''

def no_duplicate_letters(phrase):
    new_phrase = phrase.lower()
    list_phrase = new_phrase.split(' ')
    for word in list_phrase:
        if len(word) != len(set(word)):
            return False
    return True
        


print(no_duplicate_letters("Fortune favours the bold.")) #true
# print(no_duplicate_letters("You can lead a horse to water, but you can't make him drink."))
print(no_duplicate_letters("Look before you leap.")) #false
# print(no_duplicate_letters("An apple a day keeps the doctor away."))