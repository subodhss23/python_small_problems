''' Create a function that takes two strings and returns either True or False
    depending on whether they're anagrams or not.'''

def is_anagram(s1, s2):
    lst_one = list(s1.lower())
    lst_two = list(s2.lower())
    return sorted(lst_one) == sorted(lst_two)

print(is_anagram("cristian", "Cristina"))
print(is_anagram("Dave Barry", "Ray Adverb"))
print(is_anagram("Nope", "Note"))