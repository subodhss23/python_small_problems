''' Given an integer, return "odd" if the sum of all odd digits is greater than the sum of all 
    even digits. Return "even" if the sum of even digits is greater than the sum of odd digits, 
    and "equal" if both sum are the same.'''


def odds_vs_evens(num):
    new_str = str(num)
    odd = 0
    even = 0
    for i in new_str:
        if int(i) % 2 == 0:
            even+=int(i)
        elif int(i) % 2 != 0:
            odd+=int(i)
    if odd > even:
        return 'odd'
    elif even > odd:
        return 'even'
    elif even == odd:
        return 'equal'

print(odds_vs_evens(97428))
print(odds_vs_evens(81961))
print(odds_vs_evens(54870))