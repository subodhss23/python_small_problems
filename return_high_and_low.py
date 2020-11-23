''' Create a function that accepts a string of space separated integers and returns the highest and 
    lowest integers(as a string). '''


def high_low(txt):
    new_lst = txt.split()
    int_lst = []
    for i in new_lst:
        int_lst.append(int(i))
    return max(int_lst), min(int_lst)

# print(high_low("1 2 3 4 5"))
# print(high_low("1 2 -3 4 5"))
# print(high_low("13") )

print(high_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))