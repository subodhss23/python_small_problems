''' Create a function that takes in two words as input and returns a list of three elements, in the following order:

        1. Shared letters between two words.
        2. Letters unique to word 1
        3. Letters unique to word 2

        Each element should have unique letters, and have each letter be alphabetically sorted. '''


# def letters(words1, words2):
#     new_lst = []
#     one = ''
#     two = ''
#     three = ''
#     for i in words1:
#         if i in words2:
#             one+=i
#     one = sorted(set(one))
#     new_lst.append(('').join(one))
#     for i in words1:
#         if i not in words2:
#             two+=i
#     two = sorted(set(two))
#     new_lst.append(('').join((two)))
#     for i in words2:
#         if i not in words1:
#             three+=i
#     three = sorted(set(three))
#     new_lst.append(('').join(three))
#     return new_lst

def letters(words1, words2):
    one = ''
    two =  ''
    three = ''
    wd1 = sorted(list(set(words1)))
    wd2 = sorted(list(set(words2)))

    for i in wd2:
        if i in wd1:
            one+=i
        else:
            two+=i
    for j in wd1:
        if j not in wd2:
            three+=j
    return [one, three, two]

    
print(letters("sharp", "soap"))
print(letters("board", "bored"))
print(letters("happiness", "envelope"))
print(letters("kerfuffle", "fluffy"))
print(letters('match', 'ham'))