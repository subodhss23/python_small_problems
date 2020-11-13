''' Create a function that returns True if a string only contains number or alphabet,
    else return False. If string contains spaces or is empty should return False'''

def alphanumeric_restriction(str):
    return str.isalpha() or str.isdigit()

print(alphanumeric_restriction("Bold"))
print(alphanumeric_restriction("123454321"))
print(alphanumeric_restriction("H3LL0"))
print(alphanumeric_restriction("ed@bit"))