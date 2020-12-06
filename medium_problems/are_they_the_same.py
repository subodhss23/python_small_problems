''' Create a function that takes three arguments(first dictionary, second dictionary, key) in order to:
    1. Return the boolean True if both dictionaries have the same values for the same keys.
    2. If the dictionaries don't match, return the string "Not the same", or the string "One's empty"
        if only one of the dictionaries contains the given key.'''

def check(d1, d2, k):
    d1_bool = False
    d2_bool = False

    for i, j in d1.items():
        if i == k:
            d1_bool = True

    for key, value in d2.items():
        if key == k:
            d2_bool = True

    if d1_bool == d2_bool:
        if d1[k] == d2[k]:
            return True
        elif d1[k] != d2[k]:
            return 'Not the same'
    else:
        return 'One\'s empty'
    
    if d1[k] != d1[k]:
        return 'Not the same'

# def check(d1, d2, k):
#     try:
#         return d1[k] == d2[k] or 'Not the same'
#     except:
#         return 'one\'s empty'

dict_first = { "sky": "temple", "horde": "orcs", "people": 12, "story": "fine", "sun": "bright" }
dict_second = { "people": 12, "sun": "star", "book": "bad" }

print(check(dict_first, dict_second, "horde"))
print(check(dict_first, dict_second, "people"))
print(check(dict_first, dict_second, "sun"))