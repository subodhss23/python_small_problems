''' given two strings, create a function that returns the total number 
    number of unique characters from the combined string. '''

# def count_unique(s1, s2):
#     new_str = s1 + s2
#     new_lst = list(new_str)
#     new_set = set(new_lst)
#     return len(new_set)


def count_unique(s1, s2):
    return len(set(s1+s2))

print(count_unique("apple", "play"))
print(count_unique("sore", "zebra"))
print(count_unique("a", "soup"))