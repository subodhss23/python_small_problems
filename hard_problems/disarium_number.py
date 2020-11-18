''' A number is said to be Disarium if the sum of its digits raised to their respective positions is 
    the number itself.

    Create a function that determines whether a number is a Disarium or not.'''


def is_disarium(n):
    n_to_str = str(n)
    result = 0
    count = 1
    for i in n_to_str:
        result += int(i) ** count
        count+=1
    return str(result) == n_to_str

print(is_disarium(75))
print(is_disarium(135))
print(is_disarium(518))
print(is_disarium(8))