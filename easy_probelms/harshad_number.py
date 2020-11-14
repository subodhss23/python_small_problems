''' A number n is a Harshad (also called Niven) number if it is divisible by the sum
    of its digits. For example, 666 is divisible by 6+6+6, so it is a Harshad number.

    Write a function to determine whether the given number is a Harshad number.'''


def is_harshad(num):
    if num == 0:
        return False
    else:
        sum = 0
        div = 0
        new_str = str(num)
        for i in new_str:
            sum += int(i)
        return num % (sum) == 0 


print(is_harshad(209))
print(is_harshad(41))
print(is_harshad(12255))