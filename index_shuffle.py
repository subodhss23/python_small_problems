''' Write a function that takes all even-indexed characters and odd-indexed
    characters from a string and concatenates them together. '''

def index_shuffle(txt):
    even = ''
    odd = ''
    for i in range(len(txt)):
        if i % 2 == 0:
            even += txt[i]
        else:
            odd += txt[i]
    return even+odd

# print(index_shuffle('abcd'))
print(index_shuffle("it was a beautiful day"))
# print(index_shuffle("01 234 5 67"))
# print(index_shuffle("it was a beautiful day"))