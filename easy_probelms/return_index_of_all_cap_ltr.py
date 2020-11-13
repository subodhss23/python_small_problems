''' Create a function that takes a single string as arguement and returns an 
    ordered list containing the indices of all capital letters in the string.'''


def index_of_caps(word):
    new_lst = []
    for i in word:
        if i.isupper():
            new_lst.append(word.index(i))
    return new_lst

print(index_of_caps("eDaBiT"))
print(index_of_caps("eQuINoX"))
print(index_of_caps("determine"))
print(index_of_caps("STRIKE"))
print(index_of_caps("sUn"))