''' Create a function that takes two numbers and a mathmetical operation + - / *
    and will perform a calculation with the given numbers. '''


def calculator(num1, operator, num2):
    try:
        return eval(str(num1) + (operator) + str(num2))
    except ZeroDivisionError:
        return "Can't divide by 0!"

print(calculator(2, "+", 2))