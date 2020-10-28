''' create a function that takes two numbers as arguments (num, length)
    and returns a list of multiples of num until the list length reaches length. '''


def list_of_multiples(num, length):
    new_list = []
    i = 1
    multiple = 0
    while (i <= length):
        multiple = i * num
        new_list.append(multiple)
        i += 1
    return new_list

print(list_of_multiples(7, 5))
print(list_of_multiples(12, 10))
print(list_of_multiples(17, 6))
