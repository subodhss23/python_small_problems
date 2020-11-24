''' Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication, and dividion on a 
    string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

    Here, we have 1 followed  by a space, operator followed by another space and 2. For the challenge, we are going to have only two
    numbers between 1 valid operator. The return value should be a number. 

    eval() is not allowed. In case of diision, whenever the second number equals "0" return -1.'''


def arithmetic_operation(n):
    new_lst = n.split(' ')
    result= 0
    if '0' in new_lst:
        return -1
    else:
        if new_lst[1] == '+':
            result = int(new_lst[0]) + int(new_lst[2])
        elif new_lst[1] == '-':
            result = int(new_lst[0]) - int(new_lst[2])
        elif new_lst[1] == '*':
            result = int(new_lst[0]) * int(new_lst[2])
        elif new_lst[1] == '//':
            result = int(new_lst[0]) // int(new_lst[2])
    return result

print(arithmetic_operation("12 + 12"))
print(arithmetic_operation("12 - 12"))
print(arithmetic_operation("12 * 12"))
print(arithmetic_operation("12 // 0"))