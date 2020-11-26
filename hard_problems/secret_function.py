''' Create a function based on the input and output. Look at the examples, 
    there is a pattern. '''

def secret(num):
    new_str = str(num)
    first = int(new_str[0])
    second = int(new_str[1])
    one = first ** second
    two = first * second
    result = one - two
    return result
    

print(secret(24))
print(secret(42))
print(secret(15))
print(secret(52))