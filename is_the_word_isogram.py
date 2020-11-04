''' An isogram is a word that has no duplicate letters. Create a function that takes a string and
    returns either True or False depending on whether or not it's an "isogram". '''

def is_isogram(txt):
    new_set = set(txt.lower())
    if len(txt) == len(new_set):
        return True
    return False
        


print(is_isogram("Algorism"))
print(is_isogram("PasSword"))
print(is_isogram("Consecutive"))