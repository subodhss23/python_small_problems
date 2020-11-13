''' Write a function that return the lexicographically first and lexicographically
    last rearrangements of a string. Output the results in the follwing manner:'''


def first_and_last(string):
    string_one = sorted(string)
    string_two = string_one[::-1]
    return [('').join(string_one), ('').join(string_two)]

print(first_and_last("marmite"))
print(first_and_last("bench"))
print(first_and_last("scoop"))