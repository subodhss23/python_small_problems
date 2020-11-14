''' Create a function that takes a word and returns True if the word has two consecutive
    identical letters.'''

def double_letters(word):
    temp = ''
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False

print(double_letters("loop"))
print(double_letters("yummy"))
print(double_letters("orange"))
print(double_letters("munchkin"))