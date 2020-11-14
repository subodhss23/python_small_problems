''' Create a function which validates whether a 3 character string is a vowel
    sandwich. In order to have a valid sandwich, the string must satisfy the
    following rules:
        - The first and last characters must be a consonant
        - The character in the middle must be a vowel. '''
        
def is_vowel_sandwich(s):
    if len(s) == 3:
        vowel = 'aeiou'
        if s[1] in vowel and s[0] not in vowel and s[2] not in vowel:
            return True
        return False
    return False

print(is_vowel_sandwich("cat"))
# print(is_vowel_sandwich("ear"))
# print(is_vowel_sandwich("bake"))
# print(is_vowel_sandwich("try"))