''' Write a program that returns a list of all the number from 1 to an integer argument. But for
    multiples of three use "Fizz" instead of the number and for the multiples of five use "Buzz".
    For numbers which are multiples of both three and five use "FizzBuzz".'''

def fizz_buzz(maximum):
    result_lst = []
    for i in range(1, maximum+1):
        if i % 5 == 0 and i % 3 == 0:
            result_lst.append("FizzBuzz")
        elif i % 5 == 0:
            result_lst.append("Buzz")
        elif i % 3 == 0:
            result_lst.append("Fizz")
        else:
            result_lst.append(i)
    return result_lst

print(fizz_buzz(10))
print(fizz_buzz(15))