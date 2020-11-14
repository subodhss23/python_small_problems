''' Create a function that squares every digit of a number.'''

def square_digits(n):
    result = ''
    new_str = str(n)
    for i in new_str:
        result += str(int(i) ** 2)
    return result

print(square_digits(9119))
print(square_digits(2483))
print(square_digits(3212))