'''Create a function that takes an initial word and extracts any words that
    start with the same letters as the initial word.'''

def dictionary(initial, words):
    new_lst = []
    for i in words:
        if i.startswith(initial):
            new_lst.append(i)
    return new_lst


print(dictionary("bu", ["button", "breakfast", "border"]))
print(dictionary("tri", ["triplet", "tries", "trip", "piano", "tree"]))
print(dictionary("beau", ["pastry", "delicious", "name", "boring"]))
print(dictionary('no', ['inferno', 'notion', 'nominate', 'note', 'fairy']))