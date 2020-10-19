# create function that takes two numbers and a mathematical operator and returns the result.

def calculate(num1, num2, op):
    return eval(str(num1) + op + str(num2))

print(calculate(4, 9, "+"))
print(calculate(12, 5, "-"))
print(calculate(6, 3, "*"))