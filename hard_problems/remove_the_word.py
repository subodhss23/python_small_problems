''' Create a function that takes a list and string. The function should remove the letters in the string from the list,
    and return the list. '''

def remove_letters(letters, word):
    new_lst = []
    for i in word:
        if i in letters:
            letters.remove(i)
    return letters

print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))
print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))
print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit"))