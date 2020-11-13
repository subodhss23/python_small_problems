''' Create a function that takes a string and returns a new string with all 
    vowels removed.'''


# def remove_vowels(str):
#     new_str = ''
#     for i in str:
#         if i.lower() != 'a' and i.lower() != 'e' and i.lower() != 'o' and i.lower() != 'u' and i.lower() != 'i':
#             new_str += i
#     return new_str

def remove_vowels(str):
    new_str = ''
    # vowel = 'aeiouAEIOU'
    for i in str:
        if i not in 'aeiouAEIOU':
            new_str += i
    return new_str

print(remove_vowels("I have never seen a thin person drinking Diet Coke."))
print(remove_vowels("We're gonna build a wall!"))
print(remove_vowels("Happy Thanksgiving to all--even the haters and losers!"))
