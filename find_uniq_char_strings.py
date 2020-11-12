# create a function that returns only strings with unique characters.

def filter_unique(lst):
    new_lst = []
    for i in lst:
        if len(i) == len(set(i)):
            new_lst.append(i)
    return new_lst

print(filter_unique(["abb", "abc", "abcdb", "aea", "bbb"]))
print(filter_unique(["88", "999", "989", "9988", "9898"]))
print(filter_unique(["ABCDE", "DDEB", "BED", "CCA", "BAC"]))
