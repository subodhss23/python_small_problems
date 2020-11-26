''' Write a function that will return the longest word in a sentence. In cases where more than one word
    is found, return the first one. '''

def find_longest(sentence):
    sentence = sentence.replace("'", " ")
    sentence = sentence.replace('.', ' ')
    sentence = sentence.replace('"', ' ')
    new_lst = sentence.split(' ')
    result =  sorted(new_lst, key=len)
    return result[-1].lower()

# from re import split
# def find_longest(sentence):
#     return max(split("\W", sentence.lower()), key=len)

print(find_longest("A thing of beauty is a joy forever."))
print(find_longest("Forgetfulness is by all means powerless!"))
print(find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel."))