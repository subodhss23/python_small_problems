'''Write a function that takes three string arguments (first, last, and word)
    and returns True if word is found between first and last in the list, otherwise False.'''

def is_between(first, last, word):
    new_lst = [first, last, word]
    new_sorted = sorted(new_lst)
    supposed_lst = [first, word, last]
    return new_sorted == supposed_lst

''' one liner
def is_betwee(first, last, word):
    return [first, word, last] == sorted([first, word, last])'''

print(is_between("apple", "banana", "azure"))
print(is_between("bookend", "boolean", "boost"))