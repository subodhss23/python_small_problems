''' Write a function that takes a string and calculates the number of letters
    and digits within it. Return the result in a dictionary. '''


def count_all(txt):
    result = {
        "LETTERS": 0,
        "DIGITS": 0
    }
    for i in txt:
        if i.isdigit():
            result["DIGITS"]+=1
        elif i.isalpha():
            result["LETTERS"]+=1
    return result

print(count_all("Hello World"))
print(count_all("H3ll0 Wor1d"))
print(count_all("149990"))