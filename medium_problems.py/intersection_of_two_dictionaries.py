''' Write a function that takes as input two different dictionaries and filter the keys in each dictionary
    to only keep keys that exist in both dictionaries. Store your result as a list with two dicitonaries.'''

def intersection(h1, h2):
    new_lst = []
    counter = 0
    for key in h1:
        if key in h2:
            new_lst.append({key: h1[key]})
            new_lst.append({key: h2[key]})
            counter+=1
            print(counter)
    return new_lst


dict1 = {"a": 5, "b": 13, "c": 7}
dict2 = {"b": 5, "c": 8, "d": 91, "e": 99}
dict3 = {"a": 1, "b": 34}
dict4 = {"c": 9, "d": 8}


print(intersection(dict1, dict2))
print(intersection(dict1, dict4))
print(intersection(dict3, dict4))