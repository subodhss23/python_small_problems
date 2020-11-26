''' Create a function that subtracts one positive integer from another, without using any arithmetic operators 
    such as -, %, /, +, etc. 
    
    Use bitwise operations ony: <<, |, ~, &, etc.
    '''

def my_sub(a, b):
    while (a != 0):
        borrow = (~b) & a
        b = b ^ a
        a = borrow << 1
    return b

print(my_sub(5, 9))
# print(my_sub(10, 30))
# print(my_sub(0, 0))