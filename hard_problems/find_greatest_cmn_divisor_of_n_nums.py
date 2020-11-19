''' Create a function that takes a list of numbers and returns the greatest common factor 
    of those numbers. '''


def gcd(lst):
    result = 0
    new_lst = []
    for i in range(1, max(lst)):
        for j in lst:
            if j % i == 0:
                new_lst.append(i)
    repeat_lst = []
    for i in new_lst:
        if new_lst.count(i) == len(lst):
            repeat_lst.append(i)
    return max(repeat_lst)


print(gcd([84, 70, 42, 56]))
# print(gcd([19, 38, 76, 133]))
print(gcd([120, 300, 95, 425, 625]))