''' Create a function that takes a list of numbers and return "Boom!" if the
    number 7 appears in the list. Otherwise, return "there is no 7 in the list."'''

def seven_boom(lst):
    new_lst = []
    for i in lst:
        new_lst.append(list(str(i)))
    for i in new_lst:
        if '7' in i:
            return 'Boom!'
    return 'there is no 7 in the list'

print(seven_boom([2, 6, 7, 9, 3]))
print(seven_boom([33, 68, 400, 5]))
print(seven_boom([86, 48, 100, 66]))
print(seven_boom([76, 55, 44, 32]))
print(seven_boom([35, 4, 9, 37]))