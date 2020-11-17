''' A number is said to be Harshad it it's exactly divisible by the sum of its digits. Create
    a funtion that determines whether a number is a Harshad or not'''

def is_harshad(n):
    new_num = str(n)
    sum = 0
    for i in new_num:
        sum+=int(i)
    return n % sum == 0

print(is_harshad(75))
print(is_harshad(171))
print(is_harshad(481))