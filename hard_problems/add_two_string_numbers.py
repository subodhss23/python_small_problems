''' Write a function that adds two numbers. The catch, however, is that the number will be strings. '''

def add_str_nums(num1, num2):
    result = 0
    if num1 == "":
        num1 = '0'
    if num2 == "":
        num2 = '0'
    try:
        result =  int(num1) + int(num2)
        return str(result)
    except:
        print('why are we here?')
        return str(-1)


print(add_str_nums("", ""))
print(add_str_nums("4", "5"))
print(add_str_nums("abcdefg", "3"))
print(add_str_nums("1", ""))
print(add_str_nums("1874682736267235927359283579235789257", "32652983572985729"))