''' A palindrome is a word, phrase, number of other sequence of characters which reads the same
    backward or forward, such as madam or kayak.

    Write a function that takes a string and determines whether it\'s a palindrome or not.
    The function should return a boolean(True or False value).'''


def is_palindrome(txt):
    new_string = ''
    for i in txt:
        if i.isalpha():
            new_string+=i.lower()
    return new_string == new_string[::-1]

print(is_palindrome("Neuquen"))
print(is_palindrome("Not a palindrome"))
print(is_palindrome("A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!"))