''' Create a function that takes a nubmer as an argument and returns True or False
    depending on whether the number is symmetical or not. A number is symmetrical
    when it is the same as its reverse'''

def is_symmetrical(n):
    new_n = str(n)[::-1]
    return int(new_n) == n


print(is_symmetrical(7227))
print(is_symmetrical(12567))