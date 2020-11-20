''' Given a two digit number, return True if that number contains one even and one odd digit.'''

def one_odd_one_even(n):
    new_val = str(n)
    return (int(new_val[0]) + int(new_val[1])) % 2 != 0


print(one_odd_one_even(12))
print(one_odd_one_even(55))
print(one_odd_one_even(22))