''' Make a function that encrypts a given input with these steps:
    Input:"apple"
    Step 1: Reverse the input: "elppa"
    Step 2: Replace all vowels using the following chart:
        a => 0
        e => 1
        i => 2
        o => 2
        u => 3

        # 1lpp0

    Step 3: Add "aca" to the end of the word: "1lpp0aca"
    Output: "1lpp0aca"'''


def encrypt(word):
    vowel = 'aeiou'
    reversed_word = word[::-1]
    encrypted = ' '
    vowels_keys = {
        'a': '0',
        'e': '1',
        'i': '2',
        'o': '2',
        'u': '3'
    }
    for letter in reversed_word:
        if letter in vowel:
            encrypted+= vowels_keys[letter]
        else:
            encrypted+= letter
    return encrypted + 'aca'

print(encrypt('apple'))
print(encrypt("banana"))
print(encrypt("karaca"))
print(encrypt("burak"))
print(encrypt("alpaca"))
print(encrypt('hello'))