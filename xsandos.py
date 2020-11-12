''' Create a function taht takes a string, checksif it has the same number of "x"s
    and "o"s and returns either True or False.

        - Return a boolean vale(True or False)
        - The string can contain any character.
        - When "x" and "o" are not in the string, return True.'''

# def XO(txt):
#     count_x = 0
#     count_o = 0
#     for i in txt:
#         if i.lower() == 'x':
#             count_x+=1
#         elif i.lower() == 'o':
#             count_o+=1
#     return count_x == count_o or count_x == 0 and count_o == 0

# print(XO("ooxx"))
# print(XO("xooxx"))
# print(XO("ooxXm"))
# print(XO("zpzpzpp"))
# print(XO("zzoo"))


def XO(txt):
    new_txt = txt.lower()
    count_x = new_txt.count('x')
    count_o = new_txt.count('o')
    return count_x == count_o
    

print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))
print(XO("zpzpzpp"))
print(XO("zzoo"))

