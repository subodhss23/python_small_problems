''' Return True if the sum of ASCII values of the first string is same as the sum
    of ASCII values of the second string, otherwise return False.'''

def same_ascii(a, b):
    sum_a = 0
    sum_b = 0
    for i in a:
        sum_a+=ord(i)
    for j in b:
        sum_b+=ord(j)
    return sum_a == sum_b


print(same_ascii("a", "a"))
print(same_ascii("AA", "B@"))
print(same_ascii("EdAbIt", "EDABIT"))