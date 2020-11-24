''' A number/string is a palindrome if the digits/characters are the same when read both forward and backward. Examples
    include "racecar" and 12321. Given a positive number n, check if n or the binary represnetation of n is palindromic.
    Return the following:

    - "Decimal only." if only n is a palindrome
    - "Binary only." if only the binary representation of n is a palindrome.
    - "Deciaml and binary." if both are palindromes
    - "Neither!" if neither are palindrome.
    '''

def palindrome_type(n):
    dec = str(n)
    new_bin = str(bin(n)[2:])
    if dec == dec[::-1] and new_bin == new_bin[::-1]:
        return 'Decimal and binary.'
    elif dec == dec[::-1]:
        return 'Decimal only.'
    elif new_bin == new_bin[::-1]:
        return "Binary only."
    else:
        return "Neither!"


print(palindrome_type(1306031))
print(palindrome_type(427787))
print(palindrome_type(313))
print(palindrome_type(934))