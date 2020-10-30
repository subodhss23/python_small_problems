# check if the string is palindrome

def is_palindrome(txt):
    new_str = ""
    for i in txt:
        new_str = i + new_str
    return txt == new_str

print(is_palindrome('bob'))
print(is_palindrome('cat'))