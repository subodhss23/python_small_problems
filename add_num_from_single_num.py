''' Create a function that takes a number as an argument. Add up all the
    numbers from 1 to the number you passed to the function. For example,
    if the input is 4 then your function should return 10 because 1+2+3+4=10'''


def add_up(num):
    result = 0
    for i in range(num+1):
        result+=i
    return result

print(add_up(4))
print(add_up(13))
print(add_up(600))