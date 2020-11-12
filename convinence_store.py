'''Given a total due and a list representing the amount of change in your pocket, determine
    whether or not you are able to pay for the item. Change will always be represented in the
    following order: quarters, dimes, nickels, pennies.

    To illustrat: change_enough([25, 20, 5, 0], 4.25) should yield True, since having 25
    qurters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50'''


def change_enough(change, amount_due):
    # print(change[0]/4)
    # print(change[1]/10)
    # print(change[2]/20)
    # print(change[3]/100)
    return change[0]/4 + change[1]/10 + change[2]/20 + change[3]/100 >= amount_due


print(change_enough([2, 100, 0, 0], 14.11))
print(change_enough([0, 0, 20, 5], 0.75))
print(change_enough([30, 40, 20, 5], 12.55))
print(change_enough([10, 0, 0, 50], 3.85) )
print(change_enough([1, 0, 5, 219], 19.99))
print(change_enough([1, 5, 5, 219], 19.99))