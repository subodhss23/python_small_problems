''' create a function that keeps only strings with repeating identical
    characters(in other words, it has a set size of 1). '''


def identical_filter(lst):
    new_lst = []
    temp_lst = []
    for i in lst:
        if len(set(i)) == 1:
            new_lst.append(i)
    return new_lst 
            
    
    
print(identical_filter(["aaaaaa", "bc", "d", "eeee", "xyz"]))
# print(identical_filter(["88", "999", "22", "545", "133"]))
# print(identical_filter(["xxxxo", "oxo", "xox", "ooxxoo", "oxo"]))