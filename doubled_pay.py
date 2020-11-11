''' An employee working at a very bizzare company, earns one penny on their first day.
    However, for every day that passes, their base amount doubles, so they earn two
    pennies on the second day and four pennies on the third day (totalling 7 pennies).
    Given a number of days, return how many pennies the employee accumulates.'''


def double_pay(n):
    return 2 ** n - 1


print(double_pay(1))
print(double_pay(2))
print(double_pay(3))
print(double_pay(4))
print(double_pay(5))
print(double_pay(6))
print(double_pay(7))