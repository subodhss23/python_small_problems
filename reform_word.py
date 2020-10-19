# a word has been split into a left part and a right part. Re-form the
# word by adding both halves together, changing the first char to an uppercase letter.

def get_word(left, right):
    new_word = left + right
    return new_word


print(get_word("wel", "come"))
print(get_word("lang", "uage"))
