''' Create a function that builds a word from the scrambled letters contained
    in the first list. Use the second list to establish each position of the letters
    in the first list. Return a string from the unscrambled letters (that made-up the word).
'''

def word_builder(ltr, pos):
    new_lst = []
    for i in pos:
        new_lst.append(ltr[i])
    return ('').join(new_lst)

# print(word_builder(["g", "e", "o"], [1, 0, 2]))
print(word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]))
# print(word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2]))