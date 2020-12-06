''' Create a function that takes two parameters and, if both parameters are string,
    add them as if they were  integers or if the two parameters are intergers,
    concatenate them.'''

def stupid_addition(a, b):
    if type(a) == int and type(b) == int:
        return str(a) + str(b)
    elif type(a) == str and type(b) == str:
        return int(a) + int(b)
    else:
        return None


# def stupid_addition(a, b):
#     if type(a) == type(b):
#         if type(a) == int:
#             return str(a) + str(b)
#         return int(a) + int(b)

print(stupid_addition(1, 2))
print(stupid_addition("1", "2"))
print(stupid_addition("1", 2))