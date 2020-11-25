''' Write a function that returns True if a given name can generate an array of words. '''

# def anagram(name, words):
#     new_name = list(name.lower())
#     new_name.remove(' ')
#     new_str = ''
#     for i in words:
#         for j in i:
#             new_str+=j
#     new_lst = list(new_str)
#     return len(new_lst) == len(new_name)
    
def anagram(name, words):
    return sorted(''.join(words)+ ' ') == sorted(name.lower())


print(anagram("Justin Bieber", ["injures", "ebb", "it"]))
print(anagram("Natalie Portman", ["ornamental", "pita"]))
print(anagram("Chris Pratt", ["chirps", "rat"]))
print(anagram("Jeff Goldblum", ["jog", "meld", "bluffs"]) )
