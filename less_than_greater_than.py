''' create a function that takes two numbers num1, num2, and a list lst
    and returns a list containing all the numbers in lst greater than num1
    and less than num2 '''

def list_between(num1, num2, lst):
    new_lst = []
    for i in lst:
        if i > num1 and i < num2:
            new_lst.append(i)
    return new_lst


print(list_between(3, 8, [1, 5, 95, 0, 4, 7]))
print(list_between(1, 10, [1, 10, 25, 8, 11, 6]))
print(list_between(7, 32, [1, 2, 3, 78]))