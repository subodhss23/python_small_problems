# Create a function that returns the smaller number.

# def smaller_num(n1, n2):
#     if int(n1) > int(n2):
#         return n2
#     return n1

def smaller_num(n1, n2):
    return str(min(eval(n1), eval(n2)))

# print(smaller_num("21", "44"))
print(smaller_num("1500", "1"))
# print(smaller_num("5", "5"))
print(smaller_num("1500", "16"))
print(smaller_num('9999', '22'))
print(smaller_num("1500", "2"))
